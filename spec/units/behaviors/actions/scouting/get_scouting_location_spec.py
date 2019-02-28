from bot.units.terran.behaviors.actions.scouting.get_scouting_location import GetScoutingLocation

from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from collections import deque

from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("GetScoutingLocation"):
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.condition = GetScoutingLocation()

    with it("can be instantiated"):
      expect(self.condition).to(be_a(GetScoutingLocation))

  with description("Running the action") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)
      self.action = GetScoutingLocation()

    with it("will return FAILURE if it cannot find any scouting locations"):
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))

    with it("will return SUCCESS if we're already scouting a location"):
      self.tick.blackboard.set('currently_scouting', Point2((20.0, 20.0)), self.tick.tree.id)
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))

    with it("will return SUCCESS if a new scouting location can be assigned"):
      self.tick.blackboard.set('scouting_locations', deque([Point2((20.0, 20.0))]), self.tick.tree.id)
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))
      expect(self.tick.blackboard.get('currently_scouting', self.tick.tree.id)).to(equal(Point2((20.0, 20.0))))
