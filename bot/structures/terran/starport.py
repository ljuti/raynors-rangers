from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.models.terran.starport import StarportModel
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable

from sc2.unit import Unit
from sc2.constants import UnitTypeId, UpgradeId

class Starport(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit: Unit, model: StarportModel):
    super().__init__(unit, model)
    self.model = model
    self.command_bus = None

  def train_medivac(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.MEDIVAC))

  def train_banshee(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.BANSHEE))

  def train_raven(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.RAVEN))

  def train_viking(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.VIKING))

  def train_battlecruiser(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.BATTLECRUISER))

  def research_banshee_cloak(self, game):
    if game.can_afford(UpgradeId.BANSHEECLOAK) and self.has_techlab(game.structures):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      return game.command_bus.queue(techlab.research(UpgradeId.BANSHEECLOAK), silent=False)
    return False

  def research_banshee_speed(self, game):
    if game.can_afford(UpgradeId.BANSHEESPEED) and self.has_techlab(game.structures):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      return game.command_bus.queue(techlab.research(UpgradeId.BANSHEESPEED), silent=False)
    return False

  def research_advanced_ballistics(self, game):
    if game.can_afford(UpgradeId.LIBERATORAGRANGEUPGRADE) and self.has_techlab(game.structures):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      return game.command_bus.queue(techlab.research(UpgradeId.LIBERATORAGRANGEUPGRADE), silent=False)
    return False