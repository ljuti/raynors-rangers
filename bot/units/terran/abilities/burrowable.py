from sc2.constants import AbilityId

class Burrowable:
  def __init__(self, unit):
    self.unit = unit

  def burrow(self, command_bus):
    if not self.unit.is_burrowed:
      return command_bus.queue(self.unit(AbilityId.BURROWDOWN_WIDOWMINE, queue=True))
    return False

  def unburrow(self, command_bus):
    if self.unit.is_burrowed:
      return command_bus.queue(self.unit(AbilityId.BURROWUP_WIDOWMINE, queue=True))
    return False