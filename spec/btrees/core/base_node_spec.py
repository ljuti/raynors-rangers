from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.tick import Tick

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

with description("BaseNode") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.node = BaseNode()

    with it("can be instantiated"):
      expect(self.node).to(be_a(BaseNode))
      expect(self.node.id).not_to(equal(None))
      expect(self.node.title).not_to(equal(None))

  with description("Opening a node") as self:
    with before.each: # pylint: disable=no-member
      self.node = BaseNode()
      self.tick = Tick()

  with description("Closing a node") as self:
    pass