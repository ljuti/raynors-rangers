from socketio import Namespace

class CommandUplink(Namespace):
  def on_connect(self, sid, environment):
    print("[commands] Client connection: ", sid)

  def on_disconnect(self, sid):
    print("[commands] Client disconnected: ", sid)

class ActionUplink(Namespace):
  def on_connect(self, sid, environment):
    print("[actions] Client connection: ", sid)

  def on_disconnect(self, sid):
    print("[actions] Client disconnected: ", sid)

  async def relay(self, action):
    self.emit("action", { "ability": action.ability, "actor": action.unit.tag, "actor_type": action.unit.type_id, "target": action.target, "queued": action.queue })

class GameStateUplink(Namespace):
  def on_connect(self, sid, environment):
    print("[game] Client connection: ", sid)

  def on_disconnect(self, sid):
    print("[game] Client disconnected: ", sid)
