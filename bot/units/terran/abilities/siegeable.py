from bot.units.models.terran.liberator import LiberatorModel
from bot.units.models.terran.siege_tank import SiegeTankModel

from bot.command_bus import CommandBus
from sc2.unit import Unit

from sc2.constants import AbilityId

class Siegeable:
  def __init__(self, unit: Unit, model: ( LiberatorModel, SiegeTankModel )):
    self.unit = unit
    self.model = model

  @property
  def range(self) -> int:
    return int(self.current_range())

  @property
  def range_sieged(self) -> int:
    return int(self.model.range_sieged)

  @property
  def range_unsieged(self) -> int:
    return int(self.model.range_unsieged)

  @property
  def is_sieged(self) -> bool:
    return bool(
      self.unit.unit_alias is not None
      and self.model.sieged_type_id in self.unit.unit_alias
    )

  @property
  def is_not_sieged(self) -> bool:
    return bool(
      self.unit.unit_alias is None
    )

  @property
  def siege_ability(self) -> AbilityId:
    return self.model.siege_ability

  @property
  def unsiege_ability(self) -> AbilityId:
    return self.model.unsiege_ability

  def current_range(self) -> int:
    if self.is_sieged:
      return self.range_sieged
    else:
      return self.range_unsieged

  def siege(self, command_bus: CommandBus):
    if self.is_not_sieged:
      return command_bus.queue(self.unit(self.siege_ability))
    return False

  def unsiege(self, command_bus: CommandBus):
    if self.is_sieged:
      return command_bus.queue(self.unit(self.unsiege_ability))
    return False