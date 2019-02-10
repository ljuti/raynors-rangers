from bot.factories.build_command import BuildCommandFactory
from bot.commands.build_command import BuildCommand
from bot.locations.location import StructurePosition

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId

with description("BuildCommandFactory") as self:
  with description("Initialization") as self:
    with it("can be instantiated"):
      factory = BuildCommandFactory()
      expect(factory).to(be_a(BuildCommandFactory))

  with description("Creating commands") as self:
    with before.each: # pylint: disable=no-member
      self.factory = BuildCommandFactory()

    with it("can create a build command"):
      expect(self.factory.create).to(be_callable)
      command = self.factory.create()
      expect(command).to(be_a(BuildCommand))

    with it("commands must have structure they are supposed to build"):
      command = self.factory.create()
      expect(command).to(be_a(BuildCommand))
      expect(command).to(have_property('structure'))
      expect(command.structure).to(be_a(UnitTypeId))

    with it("commands must have a position where the structure will be built"):
      command = self.factory.create()
      expect(command).to(be_a(BuildCommand))
      expect(command).to(have_property('position'))
      expect(command.position).to(be_a(StructurePosition))

    with it("commands can have a set of requirements that must be met"):
      command = self.factory.create()
      expect(command).to(be_a(BuildCommand))
      expect(command).to(have_property('requirements'))
      expect(command.requirements).to(be_a(list))
