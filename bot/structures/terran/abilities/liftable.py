from sc2.constants import UnitTypeId, AbilityId
from sc2.unit_command import UnitCommand
from sc2.unit import Unit

from bot.command_bus import CommandBus

class Liftable:
  def __init__(self, unit: Unit, model):
    self.unit = unit
    self.model = model

  def lift(self, command_bus: CommandBus, immediately=True):
    if immediately:
      self.unit.orders.clear()
    return command_bus.queue(self.lift_action(self.unit.type_id))

  def lift_action(self, type_id) -> UnitCommand:
    action = None
    if type_id == UnitTypeId.BARRACKS:
      action = self.unit(AbilityId.LIFT_BARRACKS)
    elif type_id == UnitTypeId.FACTORY:
      action = self.unit(AbilityId.LIFT_FACTORY)
    elif type_id == UnitTypeId.STARPORT:
      action = self.unit(AbilityId.LIFT_STARPORT)
    elif type_id == UnitTypeId.COMMANDCENTER:
      action = self.unit(AbilityId.LIFT_COMMANDCENTER)
    elif type_id == UnitTypeId.ORBITALCOMMAND:
      action = self.unit(AbilityId.LIFT_ORBITALCOMMAND)

    return action