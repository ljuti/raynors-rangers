from sc2.constants import AbilityId
from sc2.unit import Unit

from bot.command_bus import CommandBus

class Morphable:
  def __init__(self, unit: Unit, model):
    self.unit = unit
    self.model = model

  def morph_to(self, command_bus: CommandBus, ability: AbilityId):
    self.unit.orders.clear()

    """ TODO/FIXME: Service locator, get economy service, ask if can afford. """
    if game.can_afford(ability):
      command_bus.queue(self.unit(ability))

  def morph_to_orbital(self, command_bus: CommandBus):
    self.morph_to(command_bus, AbilityId.UPGRADETOORBITAL_ORBITALCOMMAND)

  def morph_to_planetary(self, command_bus: CommandBus):
    self.morph_to(command_bus, AbilityId.UPGRADETOPLANETARYFORTRESS_PLANETARYFORTRESS)