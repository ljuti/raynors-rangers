from bot.structures.terran.base_structure import BaseStructure

class Bunker(BaseStructure):
  def __init__(self, unit, model, service_hub):
    BaseStructure.__init__(self, unit, service_hub)
    self.model = model

  async def update(self, game, unit):
    self.unit = unit
    self.close_enemies = game.nearby_enemies_for(unit)

    if self.under_fire:
      self.call_for_repair_force(game)

    if self.damaged:
      self.request_repairs(game)

  def call_for_repair_force(self, game):
    """ TODO: Finish implementation """
    scvs_close_by = game.workers.closer_than(3, self.unit.position).amount
    if scvs_close_by < 4:
      if scvs_close_by == 0:
        """ Likely initial attack, get initial repair force """
        pass
      else:
        """ A strong attack and SCVs are dying, get more """
        # game.structures.bases.nearby(self.unit.position)
        pass
