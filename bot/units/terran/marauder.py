from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.marauder import MarauderModel

from sc2.unit import Unit

class MarauderUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: MarauderModel):
    super().__init__(unit)
    self.model = model