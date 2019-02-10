from sc2.constants import AbilityId

class Morphable:
  def __init__(self, unit):
    self.unit = unit

  def morph_to(self, game, ability):
    self.unit.orders.clear()

    if game.can_afford(ability):
      game.command_bus.queue(self.unit(ability))

  def morph_to_orbital(self, game):
    self.morph_to(game, AbilityId.UPGRADETOORBITAL_ORBITALCOMMAND)

  def morph_to_planetary(self, game):
    self.morph_to(game, AbilityId.UPGRADETOPLANETARYFORTRESS_PLANETARYFORTRESS)