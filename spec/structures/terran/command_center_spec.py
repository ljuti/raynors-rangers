from bot.structures.terran.command_center import CommandCenter
from bot.structures.models.terran.command_center import CommandCenterModel

from sc2.unit import Unit

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable
import doubles

with description("CommandCenter") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.model = CommandCenterModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.unit).tag.and_return(112233)
      self.structure = CommandCenter(self.unit, self.model)

    with it("can be instantiated"):
      expect(self.structure).to(be_a(CommandCenter))

  with description("Abilities") as self:
    with before.each: # pylint: disable=no-member
      self.model = CommandCenterModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.unit).tag.and_return(112233)
      self.structure = CommandCenter(self.unit, self.model)

    with it("has a landing ability"):
      expect(self.structure.land).to(be_callable)

    with it("has a lifting ability"):
      expect(self.structure.lift).to(be_callable)

    with it("has a morphing ability"):
      expect(self.structure.morph_to).to(be_callable)
