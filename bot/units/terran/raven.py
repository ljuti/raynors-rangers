from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.raven import RavenModel

from sc2.unit import Unit

class RavenUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: RavenModel):
    super().__init__(unit)
    self.model = model