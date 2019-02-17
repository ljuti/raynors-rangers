from bot.structures.terran.tech_structure import TechStructure
from bot.structures.models.terran.engineering_bay import EngineeringBayModel

from bot.service_hub import ServiceHub

from sc2.unit import Unit
from sc2.constants import UnitTypeId, UpgradeId

class EngineeringBay(TechStructure):
  def __init__(self, unit: Unit, model: EngineeringBayModel, service_hub=None):
    TechStructure.__init__(self, unit, service_hub)
    self.model = model
    self.structures = None

  def research_infantry_weapons(self, game):
    if game.units(UnitTypeId.ARMORY):
      if UpgradeId.TERRANINFANTRYWEAPONSLEVEL2 in game.state.upgrades:
        self.research(game, UpgradeId.TERRANINFANTRYWEAPONSLEVEL3)
      else:
        self.research(game, UpgradeId.TERRANINFANTRYWEAPONSLEVEL2)
    else:
      self.research(game, UpgradeId.TERRANINFANTRYWEAPONSLEVEL1)

  def research_infantry_armor(self, game):
    if game.units(UnitTypeId.ARMORY):
      if UpgradeId.TERRANINFANTRYARMORSLEVEL2 in game.state.upgrades:
        self.research(game, UpgradeId.TERRANINFANTRYARMORSLEVEL3)
      else:
        self.research(game, UpgradeId.TERRANINFANTRYARMORSLEVEL2)
    else:
      self.research(game, UpgradeId.TERRANINFANTRYARMORSLEVEL1)

  def research_hisec_auto(self, game):
    self.research(game, UpgradeId.HISECAUTOTRACKING)

  def research_building_armor(self, game):
    self.research(game, UpgradeId.TERRANBUILDINGARMOR)