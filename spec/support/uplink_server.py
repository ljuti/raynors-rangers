from socketio import AsyncServer, AsyncNamespace
from aiohttp import web
import asyncio

class CommandUplink(AsyncNamespace):
  async def on_connect(self, sid, environment):
    print("[commands] Client connection: ", sid)
    await asyncio.sleep(0)

  async def on_disconnect(self, sid):
    print("[commands] Client disconnected: ", sid)
    await asyncio.sleep(0)

class ActionUplink(AsyncNamespace):
  async def on_connect(self, sid, environment):
    print("[actions] Client connection: ", sid)
    await asyncio.sleep(0)

  async def on_disconnect(self, sid):
    print("[actions] Client disconnected: ", sid)
    await asyncio.sleep(0)

  async def on_message(self, sid, data):
    print(f"[actions] Message received from: {sid} - Data: {data}")
    await asyncio.sleep(0)

  async def on_action(self, sid, data):
    print(f"[actions] Action received from: {sid} - Data: {data}")
    await asyncio.sleep(0)

class UnitUplink(AsyncNamespace):
  async def on_connect(self, sid, environment):
    print("[units] Client connection: ", sid)
    await asyncio.sleep(0)

  async def on_disconnect(self, sid):
    print("[units] Client disconnected: ", sid)
    await asyncio.sleep(0)

  async def on_unit(self, sid, data):
    print(f"[units] Unit reported in: {sid} - Data: {data}")
    await asyncio.sleep(0)

  async def on_action(self, sid, data):
    print(f"[actions] Action received from: {sid} - Data: {data}")
    await asyncio.sleep(0)

class GameStateUplink(AsyncNamespace):
  async def on_connect(self, sid, environment):
    print("[game] Client connection: ", sid)
    await asyncio.sleep(0)

  async def on_disconnect(self, sid):
    print("[game] Client disconnected: ", sid)
    await asyncio.sleep(0)

sio = AsyncServer()

@sio.on("connect")
async def connect(sid, environment):
  print("Client connected: ", sid)
  await asyncio.sleep(0)

@sio.on("disconnect")
async def discconnect(sid):
  print("Client disconnected: ", sid)
  await asyncio.sleep(0)

sio.register_namespace(CommandUplink("/commands"))
sio.register_namespace(ActionUplink("/actions"))
sio.register_namespace(UnitUplink("/units"))
sio.register_namespace(GameStateUplink("/game"))
app = web.Application()

sio.attach(app)

if __name__ == '__main__':
  asyncio.get_event_loop().create_task(web.run_app(app))
  asyncio.get_event_loop().run_forever()