from bot.structures.terran.base_structure import BaseStructure
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.morphable import Morphable

class CommandCenter(BaseStructure, Landable, Liftable, Morphable):
  def __init__(self, unit, model):
    BaseStructure.__init__(self, unit)

    self.unit = unit
    self.model = model

    Landable.__init__(self, unit)
    Liftable.__init__(self, unit)
    Morphable.__init__(self, unit)