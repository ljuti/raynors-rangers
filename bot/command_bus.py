from sc2.unit_command import UnitCommand

class CommandBus():
  def __init__(self, game):
    self.game = game

  def prioritize(self, command: UnitCommand):
    return True

  def queue(self, command: UnitCommand, silent=True):
    return True
