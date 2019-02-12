from bot.units.terran.army_unit import ArmyUnit
from bot.units.terran.abilities.flight import Flight
from bot.units.models.terran.liberator import LiberatorModel
from bot.units.shared.properties import UnitProperties

from sc2.unit import Unit

class LiberatorUnit(ArmyUnit, Flight, UnitProperties):
  def __init__(self, unit: Unit, model: LiberatorModel):
    super().__init__(unit, model)
    self.model = model