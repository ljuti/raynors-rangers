from bot.structures.terran.tech_structure import TechStructure
from bot.structures.models.terran.fusion_core import FusionCoreModel

from sc2.unit import Unit
from sc2.constants import UpgradeId

class FusionCore(TechStructure):
  def __init__(self, unit: Unit, model: FusionCoreModel):
    TechStructure.__init__(self, unit)
    self.model = model

  def research_yamato(self, game):
    if game.can_afford(UpgradeId.YAMATOCANNON):
      self.research(game, UpgradeId.YAMATOCANNON)