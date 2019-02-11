from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.siege_tank import SiegeTankModel
from bot.units.terran.abilities.siegeable import Siegeable

from sc2.unit import Unit

class SiegeTankUnit(ArmyUnit, Siegeable):
  def __init__(self, unit: Unit, model: SiegeTankModel):
    super().__init__(unit)
    self.model = model