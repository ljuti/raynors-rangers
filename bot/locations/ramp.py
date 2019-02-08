from bot.locations.location import Location, StructurePosition

from sc2.game_info import Ramp

class RampLocation(Location):
  def __init__(self, ramp=None):
    super().__init__()

    self.ramp_corner_depot_positions = None
    self.ramp_middle_depot_position = None

    if ramp:
      self.ramp_object = ramp
      self.initialize_from_ramp()

  def initialize_from_ramp(self):
    """ With ramps, the center is assumed to be the top center of ramp """
    self.center_position = self.ramp_object.top_center

  @classmethod
  def from_ramp(klass, ramp: Ramp):
    return klass(ramp)

  def ramp_corner_depots_as_positions(self):
    if self.ramp_corner_depot_positions is None:
      ramp_corner_depots = self.ramp_object.corner_depots
      if len(ramp_corner_depots) == 2:
        self.ramp_corner_depot_positions = [StructurePosition(pos, None) for pos in ramp_corner_depots]
    return self.ramp_corner_depot_positions

  def ramp_middle_depot_as_position(self):
    if self.ramp_middle_depot_position is None:
      self.ramp_middle_depot_position = StructurePosition(self.ramp_object.depot_in_middle, None)
    return self.ramp_middle_depot_position

  @property
  def corner_depot_positions(self) -> list:
    return self.ramp_corner_depots_as_positions()

  @property
  def middle_depot_position(self) -> StructurePosition:
    return self.ramp_middle_depot_as_position()