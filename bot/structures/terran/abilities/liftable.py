from sc2.constants import UnitTypeId, AbilityId
from sc2.unit_command import UnitCommand

class Liftable:
  def __init__(self, unit):
    self.unit = unit

  def lift(self, game, immediately=True):
    if immediately:
      self.unit.orders.clear()
    game.command_bus.queue(self.lift_action(self.unit.type_id))

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