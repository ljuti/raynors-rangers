from sc2.constants import UnitTypeId, AbilityId
from sc2.unit import Unit

class Stimmable:
  def __init__(self, unit):
    self.unit = unit

  async def stim(self, game):
    if await game.can_cast(AbilityId.EFFECT_STIM, self.unit):
      if self.should_stim():
        game.command_bus.queue(self.unit(AbilityId.EFFECT_STIM))

  def should_stim(self) -> bool:
    """ TODO: Needs code to check if the unit should stim or not """
    return bool(True)