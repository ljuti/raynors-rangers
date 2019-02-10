from bot.units.terran.army_unit import ArmyUnit
from bot.units.terran.abilities.cloakable import Cloakable
from bot.units.models.terran.ghost import GhostModel

from sc2.unit import Unit

class GhostUnit(ArmyUnit, Cloakable):
  def __init__(self, unit: Unit, model: GhostModel):
    super().__init__(unit)
    self.model = model
