from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from bot.registries.unit_registry import UnitRegistry
from bot.command_bus import CommandBus

class BuildStructureAction(Action):
  title = "Build a structure"
  description = "Builds a given structure if requirements are met and can afford"

  def __init__(self, command):
    super(BuildStructureAction, self).__init__()

    self.command = command

  def enter(self, tick: Tick):
    pass

  def tick(self, tick: Tick):
    actor = tick.target

    if actor.can_afford(self.command.structure):
      scv = actor.service_hub.get(UnitRegistry).select_scv()
      action = scv.unit.build(self.command.structure, self.command.position.coordinates)
      success = actor.service_hub.get(CommandBus).queue(action)
      if success:
        return BTreeStatus.SUCCESS

    return BTreeStatus.FAILURE

  def exit(self, tick: Tick):
    pass