from bot.units.shared.properties import UnitProperties

class MarineUnit(UnitProperties):
  def __init__(self, model):
    self.model = model
    UnitProperties.__init__(model)