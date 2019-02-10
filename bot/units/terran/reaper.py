from bot.units.terran.army_unit import ArmyUnit
from bot.units.models.terran.reaper import ReaperModel

from sc2.unit import Unit

class ReaperUnit(ArmyUnit):
  def __init__(self, unit: Unit, model: ReaperModel):
    super().__init__(unit)
    self.model = model