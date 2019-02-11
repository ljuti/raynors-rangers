from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.models.terran.starport import StarportModel
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable

from sc2.unit import Unit
from sc2.constants import UpgradeId

class Starport(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit: Unit, model: StarportModel):
    super().__init__(unit, model)
    self.model = model

  def research_banshee_cloak(self, game):
    if game.can_afford(UpgradeId.BANSHEECLOAK) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      return game.command_bus.queue(techlab.research(UpgradeId.BANSHEECLOAK), silent=False)
    return False

  def research_banshee_speed(self, game):
    if game.can_afford(UpgradeId.BANSHEESPEED) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      return game.command_bus.queue(techlab.research(UpgradeId.BANSHEESPEED), silent=False)
    return False

  def research_advanced_ballistics(self, game):
    if game.can_afford(UpgradeId.LIBERATORAGRANGEUPGRADE) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      return game.command_bus.queue(techlab.research(UpgradeId.LIBERATORAGRANGEUPGRADE), silent=False)
    return False