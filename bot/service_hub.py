from bot.command_bus import CommandBus

class ServiceHub():
  def __init__(self, game):
    self.game = game
    self.command_bus = None

  def register(self, service):
    if isinstance(service, CommandBus):
      self.command_bus = service
      return True

  def provide(self, service):
    pass

  def get(self, service):
    if service is CommandBus:
      return self.command_bus