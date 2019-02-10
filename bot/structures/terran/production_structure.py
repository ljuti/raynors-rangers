from bot.structures.terran.base_structure import BaseStructure
from bot.locations.location import Location, Position

from sc2.unit import Unit
from sc2.constants import AbilityId

class ProductionStructure(BaseStructure):
  def __init__(self, unit: Unit):
    BaseStructure.__init__(self, unit)
    self.unit = unit
    self.production_ready = False

  def post_construction_complete(self, game):
    self.production_ready = True  

  def has_no_addon(self) -> bool:
    return bool(self.unit.add_on_tag == 0)

  def rally_units_to_position(self, game, position: Position):
    game.command_bus.queue(self.unit(AbilityId.RALLY_UNITS, position.coordinates))

  def rally_units_to_location(self, game, location: Location):
    self.rally_units_to_position(game, location.center)