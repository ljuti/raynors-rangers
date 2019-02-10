from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.battlecruiser import BattlecruiserModel

from sc2.unit import Unit

class BattlecruiserUnit(ArmyUnit):
  def __init__(self, unit, model):
    super().__init__(unit)
    self.model = model