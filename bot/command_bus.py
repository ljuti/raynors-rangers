from sc2.unit_command import UnitCommand

class CommandBus():
  def __init__(self, game):
    self.game = game
    self.actions = []
    self.silent_actions = []

  def prioritize(self, command: UnitCommand):
    return True

  def queue(self, command: UnitCommand, silent=True):
    self.actions.append(command)
    return True

  async def execute(self):
    for action in self.actions:
      await self.game.do(action)

    self.actions.clear()
    await self.execute_silently()

  async def execute_silently(self):
    await self.game.do_actions(self.silent_actions)
    self.silent_actions.clear()