from bot.units.terran.behaviors.composites.scouting.scout_for_proxies import ScoutingLocationsRemaining

from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.position import Point2

with description("ScoutingLocationsRemaining"):
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.condition = ScoutingLocationsRemaining()

    with it("can be instantiated"):
      expect(self.condition).to(be_a(ScoutingLocationsRemaining))

  with description("Evaluating the condition") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)
      self.condition = ScoutingLocationsRemaining()

    with it("will return FAILURE if there are no more scouting locations"):
      status = self.condition._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))

    with it("will return FAILURE if there are no more scouting locations"):
      self.tick.blackboard.set('scouting_locations', [], self.tick.tree.id)
      status = self.condition._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))

    with it("will return SUCCESS if there are scouting locations to visit"):
      self.tick.blackboard.set('scouting_locations', [Point2((50.0, 50.0))], self.tick.tree.id)
      status = self.condition._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))
