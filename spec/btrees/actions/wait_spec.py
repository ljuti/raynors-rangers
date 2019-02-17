from bot.btrees.actions.wait import Wait
from bot.btrees.core.enums import BTreeCategory, BTreeStatus
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

import time

with description("Wait") as self:
  with description("Category") as self:
    with before.each: # pylint: disable=no-member
      pass

    with it("belongs to action category"):
      expect(Wait.category).to(equal(BTreeCategory.ACTION))

  with description("Tick") as self:
    with before.each: # pylint: disable=no-member
      self.action = Wait(milliseconds=15)
      self.action.id = "wait1"
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("waits"):
      start_time = time.time()
      status = self.action._execute(self.tick)

      expect(status).to(equal(BTreeStatus.RUNNING))

      while (time.time() - start_time) * 1000 < 25: time.sleep(0.01)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))