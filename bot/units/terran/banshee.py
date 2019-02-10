from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.banshee import BansheeModel
from bot.units.terran.abilities.cloakable import Cloakable

from sc2.unit import Unit

class BansheeUnit(ArmyUnit, Cloakable):
  def __init__(self, unit: Unit, model: BansheeModel):
    super().__init__(unit)
    self.model = model