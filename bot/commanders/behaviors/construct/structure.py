from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from bot.registries.unit_registry import UnitRegistry
from bot.registries.structure_registry import StructureRegistry
from bot.command_bus import CommandBus

import random

class BuildStructureAction(Action):
  title = "Build a structure"
  description = "Builds a given structure if requirements are met and can afford"

  def __init__(self, command):
    super(BuildStructureAction, self).__init__()

    self.command = command

  def enter(self, tick: Tick):
    pass

  def build_structure(self, actor, tick: Tick):
    if actor.can_afford(self.command.structure):
      scv = random.choice(actor.service_hub.get(UnitRegistry).scvs())
      tick.blackboard.set('scv', scv.unit.tag, tick.tree.id, self.id)

      action = scv.unit.build(self.command.structure, self.command.position.coordinates)
      success = actor.service_hub.get(CommandBus).queue(action)
      if success:
        return BTreeStatus.RUNNING

  def evaluate_build_state(self, scv_tag, actor, tick: Tick):
    scv = actor.service_hub.get(UnitRegistry).get_with_tag(scv_tag)
    if scv and scv.unit.is_constructing_scv:
      tick.blackboard.set('position', scv.unit.orders[0].target, tick.tree.id, self.id)
      return BTreeStatus.RUNNING
    elif scv and not scv.unit.is_constructing_scv:
      position = tick.blackboard.get('position', tick.tree.id, self.id)
      structure = actor.service_hub.get(StructureRegistry).get_with_position(position)
      if structure and structure.unit.is_ready:
        return BTreeStatus.SUCCESS

  def tick(self, tick: Tick):
    actor = tick.target

    scv_tag = tick.blackboard.get('scv', tick.tree.id, self.id)
    if scv_tag:
      status = self.evaluate_build_state(scv_tag, actor, tick)
      if status:
        return status
    else:
      status = self.build_structure(actor, tick)
      if status:
        return status
    return BTreeStatus.FAILURE

  def exit(self, tick: Tick):
    pass