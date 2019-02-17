from bot.btrees.actions.failure import Failure
from bot.btrees.core.enums import BTreeCategory, BTreeStatus
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

with description("Failure") as self:
  with description("Category") as self:
    with before.each: # pylint: disable=no-member
      pass

    with it("belongs to action category"):
      expect(Failure.category).to(equal(BTreeCategory.ACTION))

  with description("Tick") as self:
    with before.each: # pylint: disable=no-member
      self.action = Failure()
      self.action.id = "failure1"
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("ticks"):
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))