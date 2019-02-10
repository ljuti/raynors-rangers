from bot.structures.terran.tech_structure import TechStructure
from bot.structures.models.terran.armory import ArmoryModel

from sc2.unit import Unit
from sc2.constants import UpgradeId

class Armory(TechStructure):
  def __init__(self, unit: Unit, model: ArmoryModel):
    TechStructure.__init__(self, unit)
    self.model = model

  def research_mech_weapons(self, game):
    if UpgradeId.TERRANVEHICLEWEAPONSLEVEL2 in game.state.upgrades:
      self.research(game, UpgradeId.TERRANVEHICLEWEAPONSLEVEL3)
    elif UpgradeId.TERRANVEHICLEWEAPONSLEVEL1 in game.state.upgrades:
      self.research(game, UpgradeId.TERRANVEHICLEWEAPONSLEVEL2)
    else:
      self.research(game, UpgradeId.TERRANVEHICLEWEAPONSLEVEL1)

  def research_mech_armor(self, game):
    if UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL2 in game.state.upgrades:
      self.research(game, UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL3)
    elif UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL1 in game.state.upgrades:
      self.research(game, UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL2)
    else:
      self.research(game, UpgradeId.TERRANVEHICLEANDSHIPARMORSLEVEL1)

  def research_air_weapons(self, game):
    if UpgradeId.TERRANSHIPWEAPONSLEVEL2 in game.state.upgrades:
      self.research(game, UpgradeId.TERRANSHIPWEAPONSLEVEL3)
    elif UpgradeId.TERRANSHIPWEAPONSLEVEL1 in game.state.upgrades:
      self.research(game, UpgradeId.TERRANSHIPWEAPONSLEVEL2)
    else:
      self.research(game, UpgradeId.TERRANSHIPWEAPONSLEVEL1)