from bot.structures.terran.tech_structure import TechStructure
from bot.structures.models.terran.ghost_academy import GhostAcademyModel

from sc2.unit import Unit
from sc2.constants import AbilityId, UpgradeId

class GhostAcademy(TechStructure):
  def __init__(self, unit: Unit, model: GhostAcademyModel):
    TechStructure.__init__(self, unit)
    self.model = model

  def research_cloak(self, game):
    if game.can_afford(UpgradeId.PERSONALCLOAKING):
      self.research(game, UpgradeId.PERSONALCLOAKING)

  def build_nuke(self, game):
    if game.can_afford(AbilityId.BUILD_NUKE):
      game.command_bus.queue(self.unit(AbilityId.BUILD_NUKE, queue=True))