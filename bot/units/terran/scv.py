from bot.units.terran.base_unit import BaseUnit

class SCVUnit(BaseUnit):
  def __init__(self, unit, model):
    super(SCVUnit, self).__init__(unit)
    self.unit = unit
    self.model = model

  def update(self, game, unit):
    if unit.is_constructing_scv():
      return