from bot.units.terran.base_unit import BaseUnit

from bot.command_bus import CommandBus

class SCVUnit(BaseUnit):
  def __init__(self, unit, model, service_hub=None):
    super(SCVUnit, self).__init__(unit)
    self.unit = unit
    self.model = model
    self.services = service_hub

  def update(self, game, unit):
    if unit.is_constructing_scv():
      return

  def move_to(self, position):
    return self.services.get(CommandBus).queue(self.unit.move(position))