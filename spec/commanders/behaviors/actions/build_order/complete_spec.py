from bot.data_store import DataStore
from bot.stores.build_order_data import BuildOrderData
from bot.commanders.build_commander import BuildCommander
from bot.commanders.behaviors.actions.build_order.complete import BuildOrderComplete
from bot.btrees.core.enums import BTreeStatus
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, be_empty
import doubles

with description("BuildOrderComplete") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot', data_store=DataStore(self))

  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.game.data_store.register(BuildOrderData())
      self.data_store = self.game.data_store.get(BuildOrderData)
      self.action = BuildOrderComplete(self.data_store)

    with it("can be instantiated"):
      expect(self.action).to(be_a(BuildOrderComplete))
      expect(self.action.data_store).not_to(equal(None))
      expect(self.action.data_store).to(be_a(BuildOrderData))

  with description("Evaluating completion") as self:
    with before.each: # pylint: disable=no-member
      self.game.data_store.register(BuildOrderData())
      self.data_store = self.game.data_store.get(BuildOrderData)
      self.action = BuildOrderComplete(self.data_store)

      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.commander = BuildCommander(None)
      self.tick = self.tree.get_tick_object(self.commander, self.blackboard)

    with it("will return False when build order is not yet loaded"):
      expect(self.data_store.build_order_loaded).to(be_false)
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))

    with it("will return False when build order is not yet complete"):
      self.data_store.build_order_loaded = True
      self.data_store.loaded_phases_count = 5
      self.data_store.completed_phases_count = 4
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))

    with it("will return True when build order is completed"):
      self.data_store.build_order_loaded = True
      self.data_store.loaded_phases_count = 5
      self.data_store.completed_phases_count = 5
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))