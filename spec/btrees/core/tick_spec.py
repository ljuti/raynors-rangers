from bot.btrees.core.tick import Tick
from bot.btrees.core.base_node import BaseNode

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, be_empty, contain
import doubles

with description("Tick") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.tick = Tick()

    with it("can be instantiated"):
      expect(self.tick).to(be_a(Tick))
      expect(self.tick.tree).to(equal(None))
      expect(self.tick.debug).to(equal(None))
      expect(self.tick.target).to(equal(None))
      expect(self.tick.blackboard).to(equal(None))
      expect(self.tick._node_count).to(equal(0))
      expect(self.tick._open_nodes).to(equal([]))

  with description("Node methods") as self:
    with before.each: # pylint: disable=no-member
      self.tick = Tick()

    with it("has a method for entering a node"):
      expect(self.tick._enter_node).to(be_callable)

    with it("has a method for exiting a node"):
      expect(self.tick._exit_node).to(be_callable)

    with it("has a method for opening a node"):
      expect(self.tick._open_node).to(be_callable)

    with it("has a method for closing a node"):
      expect(self.tick._close_node).to(be_callable)

    with it("has a method for ticking a node"):
      expect(self.tick._tick_node).to(be_callable)

  with description("Entering a node") as self:
    with before.each: # pylint: disable=no-member
      self.tick = Tick()
      self.node = BaseNode()

    with it("increases node count"):
      expect(self.tick._node_count).to(equal(0))
      expect(self.tick._open_nodes).to(be_empty)
      self.tick._enter_node(self.node)
      expect(self.tick._node_count).to(equal(1))
      expect(self.tick._open_nodes).not_to(be_empty)
      expect(self.tick._open_nodes).to(contain(self.node))

  with description("Closing a node") as self:
    with before.each: # pylint: disable=no-member
      self.tick = Tick()
      self.node = BaseNode()
      self.tick._enter_node(self.node)

    with it("updates Tick when closing the node"):
      expect(self.tick._node_count).to(equal(1))
      expect(self.tick._open_nodes).to(contain(self.node))
      self.tick._close_node(self.node)
      expect(self.tick._node_count).to(equal(1))
      expect(self.tick._open_nodes).not_to(contain(self.node))