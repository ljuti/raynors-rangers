from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.viking import VikingModel

from sc2.unit import Unit

class VikingUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: VikingModel):
    super().__init__(unit)
    self.model = model