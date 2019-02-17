from bot.structures.terran.production_structure import ProductionStructure
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.reactorable import Reactorable
from bot.structures.terran.abilities.techlabable import Techlabable
from bot.structures.models.terran.barracks import BarracksModel

from sc2.unit import Unit
from sc2.constants import UnitTypeId, UpgradeId

class Barracks(ProductionStructure, Landable, Liftable, Reactorable, Techlabable):
  def __init__(self, unit: Unit, model: BarracksModel):
    super().__init__(unit, model)
    self.unit = unit
    self.model = model
    self.command_bus = None
    self.structures = None

  def train_marine(self, amount=1, queue=True):
    if amount == 2 and self.has_reactor(self.structures):
      self.command_bus.queue(self.unit.train(UnitTypeId.MARINE, queue=queue))
    return self.command_bus.queue(self.unit.train(UnitTypeId.MARINE, queue=queue))

  def train_marauder(self, queue=True):
    return self.command_bus.queue(self.unit.train(UnitTypeId.MARAUDER, queue=queue))

  def train_reaper(self, amount=1, queue=True):
    if amount == 2 and self.has_reactor(self.structures):
      self.command_bus.queue(self.unit.train(UnitTypeId.REAPER, queue=queue))
    return self.command_bus.queue(self.unit.train(UnitTypeId.REAPER, queue=queue))

  def train_ghost(self, queue=True):
    return self.command_bus.queue(self.unit.train(UnitTypeId.GHOST, queue=queue))

  def research_stim(self, game):
    if game.can_afford(UpgradeId.STIMPACK) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab.research(UpgradeId.STIMPACK), silent=False)

  def research_combat_shield(self, game):
    if game.can_afford(UpgradeId.SHIELDWALL) and self.has_techlab(game):
      techlab = game.units.find_by_tag(self.unit.add_on_tag)
      game.command_bus.queue(techlab.research(UpgradeId.SHIELDWALL), silent=False)