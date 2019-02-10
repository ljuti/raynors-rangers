from sc2.data import CloakState
from sc2.constants import UnitTypeId, AbilityId

from bot.units.models.terran.banshee import BansheeModel
from bot.units.models.terran.ghost import GhostModel

from bot.command_bus import CommandBus

class Cloakable:
  def __init__(self, unit):
    self.unit = unit
    self.type_id = unit.type_id

  def cloak(self, command_bus: CommandBus):
    if self.unit.energy > 0:
      if isinstance(self.model, BansheeModel): # pylint: disable=no-member
        return command_bus.prioritize(self.unit(AbilityId.BEHAVIOR_CLOAKON_BANSHEE))
      elif isinstance(self.model, GhostModel): # pylint: disable=no-member
        return command_bus.prioritize(self.unit(AbilityId.BEHAVIOR_CLOAKON_GHOST))
    return False

  def de_cloak(self, command_bus: CommandBus):
    if isinstance(self.model, BansheeModel): # pylint: disable=no-member
      return command_bus.queue(self.unit(AbilityId.BEHAVIOR_CLOAKOFF_BANSHEE))
    elif isinstance(self.model, GhostModel): # pylint: disable=no-member
      return command_bus.queue(self.unit(AbilityId.BEHAVIOR_CLOAKOFF_GHOST))
    return False

  @property
  def is_fully_cloaked(self) -> bool:
    return bool(self.unit._proto.cloak in {CloakState.Cloaked.value})

  @property
  def is_cloaked_but_detected(self) -> bool:
    return bool(self.unit._proto.cloak in {CloakState.CloakedDetected.value})

  @property
  def is_cloaked(self) -> bool:
    return bool(self.unit.is_cloaked())

  @property
  def cloak_left_in_seconds(self):
    if isinstance(self.model, BansheeModel): # pylint: disable=no-member
      return int(self.unit.energy / 1.26)
    elif isinstance(self.model, GhostModel): # pylint: disable=no-member
      return int(self.unit.energy / 1.3)
    else:
      return 0