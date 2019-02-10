from bot.structures.terran.base_structure import BaseStructure
from bot.structures.models.terran.reactor import ReactorModel

from sc2.unit import Unit

class Reactor(BaseStructure):
  def __init__(self, unit: Unit, model: ReactorModel):
    BaseStructure.__init__(self, unit)
    self.model = model