from socketio import AsyncClientNamespace

class CommandUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

class ActionUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

  async def relay(self, action):
    self.emit("action", { "ability": action.ability, "actor": action.unit.tag, "actor_type": action.unit.type_id, "target": action.target, "queued": action.queue })

class GameStateUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass
