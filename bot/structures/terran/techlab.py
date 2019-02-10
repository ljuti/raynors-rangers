from bot.structures.terran.tech_structure import TechStructure
from bot.structures.models.terran.techlab import TechlabModel
from sc2.unit import Unit

class Techlab(TechStructure):
  def __init__(self, unit: Unit, model: TechlabModel):
    TechStructure.__init__(self, unit)
    self.model = model