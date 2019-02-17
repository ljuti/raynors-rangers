from bot.btrees.core.condition import Condition
from bot.btrees.core.enums import BTreeCategory

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, contain, be_empty
import doubles

with description("Condition") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.condition = Condition()

    with it("can be instantiated"):
      expect(self.condition).to(be_a(Condition))

    with it("has a correct category"):
      expect(Condition.category).to(equal(BTreeCategory.CONDITION))