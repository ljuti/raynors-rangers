from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.marauder import MarauderModel
from bot.units.terran.abilities.stimmable import Stimmable
from bot.units.shared.properties import UnitProperties

from sc2.unit import Unit

class MarauderUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: MarauderModel):
    super().__init__(unit, model)
    self.model = model