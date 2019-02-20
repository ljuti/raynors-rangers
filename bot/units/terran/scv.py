from bot.units.terran.base_unit import BaseUnit

from bot.btrees.core.blackboard import Blackboard
from bot.units.terran.behaviors.trees.scv_scouting import SCVScoutingTree

from bot.command_bus import CommandBus

class SCVUnit(BaseUnit):
  def __init__(self, unit, model, service_hub=None):
    super(SCVUnit, self).__init__(unit)
    self.unit = unit
    self.model = model
    self.services = service_hub
    self.behavior = None
    self.blackboard = None

  def update(self, game, unit):
    self.unit = unit
    if self.behavior:
      if self.blackboard is None:
        self.blackboard = Blackboard()
      self.behavior.tick(self, self.blackboard)

  def begin_scouting(self):
    print(f"Assigning scouting behavior to {self.unit.tag}")
    self.behavior = SCVScoutingTree(self.services)

  def move_to(self, position):
    print(f"Got a command to move to {position}")
    return self.services.get(CommandBus).queue(self.unit.move(position))