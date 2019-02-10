from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.cyclone import CycloneModel

from sc2.unit import Unit

class CycloneUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: CycloneModel):
    super().__init__(unit)
    self.model = model