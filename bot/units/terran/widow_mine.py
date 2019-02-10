from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.widow_mine import WidowMineModel
from bot.units.terran.abilities.burrowable import Burrowable

from sc2.unit import Unit

class WidowMineUnit(ArmyUnit, Burrowable):
  def __init__(self, unit: Unit, model: WidowMineModel):
    super().__init__(unit)
    self.model = model