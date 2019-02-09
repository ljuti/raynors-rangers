import socketio

from bot.uplink.namespaces import CommandUplink, ActionUplink, GameStateUplink

class Uplink():
  def __init__(self):
    self.server_hostname = "localhost"
    self.server_port = 25000
    self.sio = socketio.AsyncClient()

  async def connect(self):
    self.sio.register_namespace(CommandUplink("/commands"))
    self.sio.register_namespace(ActionUplink("/actions"))
    self.sio.register_namespace(GameStateUplink("/game"))

    await self.sio.connect(f"http://{self.server_hostname}:{self.server_port}")

  async def disconnect(self):
    await self.sio.disconnect()