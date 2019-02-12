from bot.units.shared.properties import UnitProperties

from bot.units.terran.army_unit import ArmyUnit
from bot.units.terran.abilities.loadable import Loadable
from bot.units.terran.abilities.stimmable import Stimmable
from bot.units.models.terran.marine import MarineModel

from sc2.unit import Unit

class MarineUnit(ArmyUnit, Stimmable, UnitProperties):
  def __init__(self, unit: Unit, model: MarineModel):
    super().__init__(unit, model)
    self.unit = unit
    self.model = model
