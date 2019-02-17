from bot.btrees.core.decorator import Decorator
from bot.btrees.core.enums import BTreeCategory

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, contain, be_empty
import doubles

with description("Decorator") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.condition = Decorator(child="child1")

    with it("can be instantiated"):
      expect(self.condition).to(be_a(Decorator))
      expect(self.condition.child).not_to(equal(None))
      expect(self.condition.child).to(equal('child1'))

    with it("has a correct category"):
      expect(Decorator.category).to(equal(BTreeCategory.DECORATOR))