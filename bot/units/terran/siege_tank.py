from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.siege_tank import SiegeTankModel

from sc2.unit import Unit

class SiegeTankUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: SiegeTankModel):
    super().__init__(unit)
    self.model = model