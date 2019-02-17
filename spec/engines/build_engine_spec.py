from bot.engines.build_engine import BuildEngine

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2
from sc2 import Race

with description("BuildEngine") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.engine = BuildEngine()

    with it("can be instantiated"):
      expect(self.engine).to(be_a(BuildEngine))

  with description("Selecting and loading build orders") as self:
    with before.each: # pylint: disable=no-member
      self.engine = BuildEngine()
      self.engine.enemy_race = Race.Zerg

    with description("Selecting a build") as self:
      with it("will choose a build based on the race of the opponent"):
        expect(self.engine.select_build).to(be_callable)