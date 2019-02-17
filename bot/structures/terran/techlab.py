from bot.structures.terran.tech_structure import TechStructure
from bot.structures.models.terran.techlab import TechlabModel
from sc2.unit import Unit

class Techlab(TechStructure):
  def __init__(self, unit: Unit, model: TechlabModel, service_hub):
    TechStructure.__init__(self, unit, service_hub)
    self.model = model