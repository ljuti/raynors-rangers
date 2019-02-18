from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.models.terran.starport import StarportModel
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable

from sc2.unit import Unit
from sc2.constants import UnitTypeId, UpgradeId

class Starport(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit: Unit, model: StarportModel, service_hub=None):
    super().__init__(unit, model, service_hub)
    self.model = model
    self.command_bus = None
    self.structures = None

  def train_medivac(self, amount=1, queue=True):
    if amount == 2 and self.has_reactor(self.structures):
      self.command_bus.queue(self.unit.train(UnitTypeId.MEDIVAC, queue=queue))
    return self.command_bus.queue(self.unit.train(UnitTypeId.MEDIVAC, queue=queue))

  def train_banshee(self, queue=True):
    return self.command_bus.queue(self.unit.train(UnitTypeId.BANSHEE, queue=True))

  def train_raven(self, queue=True):
    return self.command_bus.queue(self.unit.train(UnitTypeId.RAVEN, queue=True))

  def train_viking(self, amount=1, queue=True):
    if amount == 2 and self.has_reactor(self.structures):
      self.command_bus.queue(self.unit.train(UnitTypeId.VIKING, queue=queue))
    return self.command_bus.queue(self.unit.train(UnitTypeId.VIKING, queue=queue))

  def train_battlecruiser(self, queue=True):
    return self.command_bus.queue(self.unit.train(UnitTypeId.BATTLECRUISER, queue=queue))

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