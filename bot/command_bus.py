from sc2.unit_command import UnitCommand

class CommandBus():
  def __init__(self, game):
    self.game = game
    self.actions = []

  def prioritize(self, command: UnitCommand):
    return True

  def queue(self, command: UnitCommand, silent=True):
    self.actions.append(command)
    return True
