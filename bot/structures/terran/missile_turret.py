from bot.structures.terran.base_structure import BaseStructure
from bot.structures.models.terran.missile_turret import MissileTurretModel

from sc2.unit import Unit

class MissileTurret(BaseStructure):
  def __init__(self, unit: Unit, model: MissileTurretModel, service_hub):
    BaseStructure.__init__(self, unit, service_hub)
    self.model = model

  async def update(self, game, unit):
    self.unit = unit
    self.close_enemies = game.nearby_enemies_for(unit)

    if self.close_enemies:
      if unit.not_attacking:
        self.select_best_target()

    if self.under_fire:
      self.call_for_repair_force(game)

  def select_best_target(self):
    raise NotImplementedError

  def call_for_repair_force(self, game):
    raise NotImplementedError