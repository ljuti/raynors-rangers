from bot.commanders.behaviors.composites.build_order.evaluate_active_phase import EvaluateActivePhase

from bot.btrees.core.enums import BTreeStatus
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick

from bot.data_store import DataStore
from bot.stores.build_order_data import BuildOrderData

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, be_empty
import doubles

from sc2.position import Point2

with description("EvaluateActivePhase") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot', start_location=None, data_store=DataStore(self))

  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.game.data_store.register(BuildOrderData())
      self.data_store = self.game.data_store
      self.composite = EvaluateActivePhase(self.data_store)

    with it("can be instantiated"):
      expect(self.composite).to(be_a(EvaluateActivePhase))
      expect(self.composite.children).not_to(be_empty)

  with description("Scenarios"):
    with before.each: # pylint: disable=no-member
      self.game.data_store.register(BuildOrderData())
      self.data_store = self.game.data_store
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with description("Build Order Not Complete - Active Phase Detected") as self:
      with it("will return True as there's an active phase going on"):
        doubles.allow(self.blackboard).get.and_return(0)
        composite = EvaluateActivePhase(self.data_store)
        status = composite.tick(self.tick)

        expect(status).to(equal(BTreeStatus.SUCCESS))

    with description("Build Order Not Complete - Active Phase Not Detected") as self:
      with it("will return True because we just loaded an active phase"):
        doubles.allow(self.blackboard).get.and_return(0)
        composite = EvaluateActivePhase(self.data_store)
        status = composite.tick(self.tick)

        expect(status).to(equal(BTreeStatus.SUCCESS))

    with description("Build Order Complete") as self:
      pass