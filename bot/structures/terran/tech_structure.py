from bot.structures.terran.base_structure import BaseStructure

from sc2.unit import Unit

class TechStructure(BaseStructure):
  def __init__(self, unit: Unit, service_hub):
    super(TechStructure, self).__init__(unit, service_hub)

  def research(self, game, upgrade):
    if game.can_afford(upgrade):
      game.command_bus.queue(self.unit.research(upgrade))