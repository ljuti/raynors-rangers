from spec.support.uplink_server import CommandUplink, ActionUplink, GameStateUplink
from socketio import AsyncServer
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import request

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true
import doubles

sio = AsyncServer()

@sio.on("message")
async def print_message(sid, message):
  print("Socket ID: ", sid)
  print(message)

@sio.on("connect")
async def connect(sid, environment):
  print("Client connected: ", sid)

@sio.on("disconnect")
async def discconnect(sid):
  print("Client disconnected: ", sid)

sio.register_namespace(CommandUplink("/commands"))
sio.register_namespace(ActionUplink("/actions"))
sio.register_namespace(GameStateUplink("/game"))
app = web.Application()

sio.attach(app)
# web.run_app(app)

with description("Uplink") as self:
  with before.all: # pylint: disable=no-member
    pass

  with it("can do stuff"):
    expect(1).to(be_a(int))

  with after.all: # pylint: disable=no-member
    pass
    # app.shutdown()