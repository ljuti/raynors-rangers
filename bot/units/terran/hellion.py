from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.hellion import HellionModel
from bot.units.shared.properties import UnitProperties

from sc2.unit import Unit

class HellionUnit(ArmyUnit, UnitProperties):
  def __init__(self, unit: Unit, model: HellionModel):
    super().__init__(unit, model)
    self.model = model