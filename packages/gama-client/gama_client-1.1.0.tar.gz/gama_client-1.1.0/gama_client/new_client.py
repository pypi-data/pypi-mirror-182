import json
import sys
import threading
from asyncio import Future

import websockets
import asyncio
from typing import List, Dict, Union
import uuid

from gama_client.base_client import GamaBaseClient
from gama_client.command_types import CommandTypes
from gama_client.message_types import MessageTypes


class GamaSyncClient(GamaBaseClient):


    running_commands: Dict[str, Future]

    def __init__(self, url: str, port: int):
        GamaBaseClient.__init__(self, url, port, self.sync_message_handler)
        self.running_commands = {}

    async def sync_message_handler(self, message: Dict):
        pass

    async def start_listening_loop(self):
        print("start listening")
        while True:
            try:
                mess = await self.socket.recv()
                try:
                    js = json.loads(mess)
                    if "type" in js and "content" in js:
                        content = js["content"]
                        if "command" in js and "wrapper_id" in js["command"]:
                            wrapper_id = js["command"]["wrapper_id"]
                            if wrapper_id in self.running_commands.keys():
                                self.running_commands[wrapper_id].set_result(js)
                        else:
                            match js["type"]:

                                case MessageTypes.ConnectionSuccessful.value:
                                    print("connection successful")
                                    self.connection_future.set_result(content)
                                case MessageTypes.SimulationStatus.value, MessageTypes.SimulationStatusInform.value, MessageTypes.SimulationStatusError.value, MessageTypes.SimulationStatusNeutral.value:
                                    self.status_handler(js)
                                case MessageTypes.SimulationOutput.value, MessageTypes.SimulationDebug.value:
                                    self.console_handler(js)
                                case MessageTypes.SimulationDialog.value, MessageTypes.SimulationErrorDialog.value:
                                    self.dialog_handler(js)
                                case MessageTypes.SimulationError.value, MessageTypes.RuntimeError.value, MessageTypes.GamaServerError.value:
                                    self.error_handler(js) #dans un premier temps, TODO: changer
                                case MessageTypes.CommandExecutedSuccessfully.value:
                                    print("impossible to find the associated command")
                                case MessageTypes.MalformedRequest.value, MessageTypes.SimulationEnded.value, MessageTypes.UnableToExecuteRequest.value:
                                    print("problem", js)

                    else:
                        print("Gama-server message is missing its 'type' field", js)

                except Exception as js_ex:
                    print("unable to unpack gama-server messages as a json", js_ex)
            except Exception as sock_ex:
                print("Error while waiting for a message from gama-server. Exiting", sock_ex)
                sys.exit(-1)


    async def message_handler(self, message: Dict):
        pass

    async def load(self, file_path: str, experiment_name: str, console: bool = False, status: bool = False, dialo: bool = False, parameters: ) -> dict:
        cmd_id = str(uuid.uuid4())
        self.running_commands[cmd_id] = self.event_loop.create_future()
        cmd = { #TODO
            "type": CommandTypes.Load.value,
            "socket_id": self.socket_id,
            "model": file_path,
            "experiment": experiment_name,
            "console": console,
            "status": False,
            "dialog": False,
            #"parameters": "<params>", // optional
           # "until": "<end_condition>", // optional
            "wrapper_id": cmd_id,
        }
        await self.socket.send(json.dumps(cmd))
        return await self.running_commands[cmd_id]


async def test_main():
    client = GamaClient("localhost", 6868)
    #client.event_loop.call_soon_threadsafe(client.start_listening_loop())
    await client.connect()
    await asyncio.sleep(3)

    response = await client.load(r"C:\Users\baptiste\Gama_Workspace2\test de trucs\models\test memorize.gaml", "weightperagents")
    print(response)

if __name__ == "__main__":
    asyncio.run(test_main())


