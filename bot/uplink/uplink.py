import socketio
import json

from bot.uplink.namespaces import CommandUplink, ActionUplink, GameStateUplink, UnitUplink

class Uplink():
  def __init__(self):
    self.server_hostname = "localhost"
    self.server_port = 8080
    self.sio = socketio.AsyncClient()

  async def connect(self):
    self.sio.register_namespace(CommandUplink("/commands"))
    self.sio.register_namespace(ActionUplink("/actions"))
    self.sio.register_namespace(UnitUplink("/units"))
    self.sio.register_namespace(GameStateUplink("/game"))

    await self.sio.connect(f"http://{self.server_hostname}:{self.server_port}")

  async def disconnect(self):
    await self.sio.disconnect()

  async def relay(self, action):
    """ Relays action information via Uplink """
    await self.sio.emit("action", { "ability": action.ability.name, "actor": action.unit.tag, "actor_type": action.unit.type_id.name, "target": action.target, "queued": action.queue }, namespace="/actions")

  async def unit(self, unit):
    """ Submits unit status report via Uplink """
    await self.sio.emit("unit", { "type": unit.type_id.name, "tag": unit.tag, "position": unit.position }, namespace="/units")

  async def structure(self, structure):
    await self.sio.emit("structure", { "type": structure.type_id.name, "tag": structure.tag, "position": structure.position }, namespace="/units")