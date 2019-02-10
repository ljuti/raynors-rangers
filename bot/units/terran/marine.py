from bot.units.shared.properties import UnitProperties

from bot.units.models.terran.marine import MarineModel

from sc2.unit import Unit

class MarineUnit(UnitProperties):
  def __init__(self, unit: Unit, model: MarineModel):
    self.unit = unit
    self.model = model

    UnitProperties.__init__(self, model)