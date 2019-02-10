from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.medivac import MedivacModel

from sc2.unit import Unit

class MedivacUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: MedivacModel):
    super().__init__(unit)
    self.model = model