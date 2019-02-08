from bot.locations.location import StructurePosition
from bot.locations.ramp import RampLocation

from sc2.game_info import GameInfo
from sc2.game_info import Ramp
from sc2.position import Point2

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, have_property, be_callable
import doubles

main_ramp_points = {
  Point2((128, 40)),
  Point2((129, 39)),
  Point2((126, 38)),
  Point2((127, 37)),
  Point2((124, 36)),
  Point2((125, 35)),
  Point2((128, 39)),
  Point2((125, 36)),
  Point2((127, 39)),
  Point2((126, 36)),
  Point2((124, 37)),
  Point2((127, 38)),
  Point2((126, 37)),
  Point2((128, 38)),
  Point2((125, 37)),
  Point2((126, 35))
}

with description("RampLocation") as self:
  with description("Initialization") as self:
    with description("without arguments") as self:
      with before.each: # pylint: disable=no-member
        self.location = RampLocation()

      with it("can be instantiated"):
        expect(self.location).to(be_a(RampLocation))

    with description("from a Ramp object") as self:
      with before.each: # pylint: disable=no-member
        self.ramp = Ramp(main_ramp_points, None)
        doubles.allow(self.ramp).top_center.and_return(Point2((124.5, 35.5)))
        self.location = RampLocation.from_ramp(self.ramp)

      with it("can be instantiated"):
        expect(self.location).to(be_a(RampLocation))
        expect(self.location.center).to(equal(Point2((124.5, 35.5))))

  with description("From a Ramp object") as self:
    with description("'small' ramps") as self:
      with before.each: # pylint: disable=no-member
        self.ramp = Ramp(main_ramp_points, None)
        doubles.allow(self.ramp).top_center.and_return(Point2((124.5, 35.5)))
        doubles.allow(self.ramp).corner_depots.and_return({ Point2((124, 36)), Point2((125, 35)) })
        doubles.allow(self.ramp).depot_in_middle.and_return(Point2((124, 36)))
        self.location = RampLocation.from_ramp(self.ramp)

      with it("has proper positions for corner depots"):
        expect(self.location).to(have_property('corner_depot_positions'))
        expect(self.location.corner_depot_positions).to(be_a(list))
        for position in self.location.corner_depot_positions:
          expect(position).to(be_a(StructurePosition))
          expect(position.coordinates).to(be_a(Point2))
          expect(position.structure).to(equal(None))

      with it("has proper position for middle depot"):
        expect(self.location).to(have_property('middle_depot_position'))
        expect(self.location.middle_depot_position).to(be_a(StructurePosition))