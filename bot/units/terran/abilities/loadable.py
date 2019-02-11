from bot.command_bus import CommandBus

from sc2.unit import Unit
from sc2.constants import AbilityId

class Loadable:
  def __init__(self, unit: Unit, model):
    self.unit = unit
    self.model = model

    self.loaded = False
    self.loaded_in = None

  """ TODO: You must check the loading status in the Update Method to prevent unit state warp. """

  def load(self, target: Unit, command_bus: CommandBus):
    if not self.is_passenger and self.target_has_space(target):
      self.loaded = True
      self.loaded_in = target.tag
      return command_bus.queue(target(AbilityId.LOAD, self.unit))
    return False

  def unload(self, target: Unit, command_bus: CommandBus):
    if is_passenger:
      self.loaded = False
      self.loaded_in = None
      return command_bus.queue(target(AbilityId.UNLOADUNIT, self.unit))
    return False

  def unload_at(self, target: Unit, position: Point2, command_bus: CommandBus):
    if is_passenger:
      return command_bus.queue(target(AbilityId.UNLOADALLAT, position, queue=True))
    return False

  def target_has_space(self, target) -> bool:
    return bool(
      (target.cargo_max - target.cargo_used) >= self.model.cargo_size
    )

  @property
  def is_passenger(self) -> bool:
    return bool(
      self.loaded
    )