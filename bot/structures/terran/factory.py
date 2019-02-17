from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable
from bot.structures.models.terran.factory import FactoryModel

from sc2.unit import Unit
from sc2.constants import AbilityId, UpgradeId, UnitTypeId

class Factory(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit: Unit, model: FactoryModel):
    super().__init__(unit, model)
    self.model = model
    self.command_bus = None

  def train_hellion(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.HELLION))

  def train_cyclone(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.CYCLONE))

  def train_siege_tank(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.SIEGETANK))

  def train_thor(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.THOR))

  def train_widow_mine(self):
    return self.command_bus.queue(self.unit.train(UnitTypeId.WIDOWMINE))

  def research_blue_flame(self, game):
    if game.can_afford(UpgradeId.HELLIONCAMPAIGNINFERNALPREIGNITER) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab(AbilityId.RESEARCH_INFERNALPREIGNITER), silent=False)

  def research_drilling_claws(self, game):
    if game.can_afford(UpgradeId.DRILLCLAWS) and self.has_techlab(game) and game.units(UnitTypeId.ARMORY).exists:
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab.research(UpgradeId.DRILLCLAWS), silent=False)

  def research_magfield_accelerator(self, game):
    if game.can_afford(UpgradeId.CYCLONELOCKONDAMAGEUPGRADE) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab.research(UpgradeId.CYCLONELOCKONDAMAGEUPGRADE), silent=False)