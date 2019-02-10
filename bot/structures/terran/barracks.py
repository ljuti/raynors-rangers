from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable

class Barracks(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit, model):
    ProductionStructure.__init__(self, unit)
    self.unit = unit
    self.model = model

    Landable.__init__(self, unit)
    Liftable.__init__(self, unit)
    Reactorable.__init__(self, unit)
    Techlabable.__init__(self, unit)