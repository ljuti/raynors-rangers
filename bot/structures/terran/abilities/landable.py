from sc2.constants import UnitTypeId, AbilityId
from sc2.unit import Unit

from bot.command_bus import CommandBus

class Landable:
  def __init__(self, unit: Unit, model):
    self.unit = unit
    self.model = model
    self.landing_position = None

  def land(self, command_bus: CommandBus):
    position = self.landing_position
    if position is None:
      """ TODO/FIXME: Should get the landing position from location service """
      position = self.get_landing_position(game)

    command_bus.queue(self.land_action(self.landing_position))

  def land_action(self, position):
    ability = None

    if self.unit.type_id == UnitTypeId.BARRACKS:
      ability = AbilityId.LAND_BARRACKS, position
    elif self.unit.type_id == UnitTypeId.FACTORY:
      ability = AbilityId.LAND_FACTORY
    elif self.unit.type_id == UnitTypeId.STARPORT:
      ability = AbilityId.LAND_STARPORT
    elif self.unit.type_id == UnitTypeId.COMMANDCENTER:
      ability = AbilityId.LAND_COMMANDCENTER
    elif self.unit.type_id == UnitTypeId.ORBITALCOMMAND:
      ability = AbilityId.LAND_ORBITALCOMMAND

    return self.unit(ability, position)

  def get_landing_position(self, game):
    """ TODO: Implement, get a position from location mapper """
    return True