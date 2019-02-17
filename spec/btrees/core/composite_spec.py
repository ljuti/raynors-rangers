from bot.btrees.core.composite import Composite
from bot.btrees.core.enums import BTreeCategory

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, contain, be_empty
import doubles

with description("Composite") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.composite = Composite(children=['child1', 'child2'])

    with it("can be instantiated"):
      expect(self.composite).to(be_a(Composite))
      expect(self.composite.children).not_to(be_empty)
      expect(self.composite.children).to(contain('child1'))
      expect(self.composite.children).to(contain('child2'))

    with it("has a correct category"):
      expect(Composite.category).to(equal(BTreeCategory.COMPOSITE))