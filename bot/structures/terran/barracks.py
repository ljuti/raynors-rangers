from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable
from bot.structures.models.terran.barracks import BarracksModel

from sc2.unit import Unit
from sc2.constants import UpgradeId

class Barracks(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit: Unit, model: BarracksModel):
    super().__init__(unit, model)
    self.unit = unit
    self.model = model

    # Landable.__init__(self, unit)
    # Liftable.__init__(self, unit)
    # Reactorable.__init__(self, unit)
    # Techlabable.__init__(self, unit)

  def research_stim(self, game):
    if game.can_afford(UpgradeId.STIMPACK) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab.research(UpgradeId.STIMPACK), silent=False)

  def research_combat_shield(self, game):
    if game.can_afford(UpgradeId.SHIELDWALL) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab.research(UpgradeId.SHIELDWALL), silent=False)