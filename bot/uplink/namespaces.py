from socketio import AsyncClientNamespace

class CommandUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

  async def command(self, command):
    pass

class ActionUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

class UnitUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

class GameStateUplink(AsyncClientNamespace):
  def on_connect(self):
    pass

  def on_disconnect(self):
    pass

  async def relay(self, state):
    self.emit("game", state, namespace="/game")