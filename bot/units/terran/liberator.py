from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.liberator import LiberatorModel

from sc2.unit import Unit

class LiberatorUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: LiberatorModel):
    super().__init__(unit)
    self.model = model