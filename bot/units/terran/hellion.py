from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.hellion import HellionModel

from sc2.unit import Unit

class HellionUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: HellionModel):
    super().__init__(unit)
    self.model = model