from bot.units.terran.behaviors.composites.scouting.scout_natural_expansion import NaturalExpansionScouted

from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

with description("NaturalExpansionScouted"):
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.condition = NaturalExpansionScouted()

    with it("can be instantiated"):
      expect(self.condition).to(be_a(NaturalExpansionScouted))

  with description("Evaluating the condition") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)
      self.condition = NaturalExpansionScouted()

    with it("will return FAILURE if natural hasn't been scouted"):
      status = self.condition._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))

    with it("will return SUCCESS if natural has been scouted"):
      self.tick.blackboard.set('natural_scouted', True, self.tick.tree.id)
      status = self.condition._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))
