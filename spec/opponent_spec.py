from bot.opponent import Opponent

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

with description("Opponent") as self:
  with before.each: # pylint: disable=no-member
    self.opponent = Opponent()

  with description("Properties") as self:
    with it("has a race property"):
      expect(self.opponent).to(have_property('race'))

    with it("has a known main base property"):
      expect(self.opponent).to(have_property('known_main_location'))

    with it("has a known natural base property"):
      expect(self.opponent).to(have_property('known_natural_location'))

    with it("has a known army strength property"):
      expect(self.opponent).to(have_property('known_army_strength'))

