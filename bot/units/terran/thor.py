from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.thor import ThorModel

from sc2.unit import Unit

class ThorUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: ThorModel):
    super().__init__(unit)
    self.model = model