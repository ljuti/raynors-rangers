from bot.service_hub import ServiceHub
from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable
import doubles

with description("ServiceHub") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot')

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.hub = ServiceHub(self.game)

    with it("can be instantiated"):
      expect(self.hub).to(be_a(ServiceHub))

  with description("Registering services") as self:
    with before.each: # pylint: disable=no-member
      self.hub = ServiceHub(self.game)

    with it("has a method for registering a service"):
      expect(self.hub.register).to(be_callable)

    with it("can register a service"):
      command_bus = CommandBus(self.game)
      expect(self.hub.command_bus).to(equal(None))
      expect(self.hub.register(command_bus)).to(be_true)
      expect(self.hub.command_bus).to(equal(command_bus))

  with description("Getting access to a service") as self:
    with before.each: # pylint: disable=no-member
      self.command_bus = CommandBus(self.game)
      self.hub = ServiceHub(self.game)
      self.hub.register(self.command_bus)

    with it("returns a requested service"):
      expect(self.hub.get).to(be_callable)
      expect(self.hub.get(CommandBus)).to(equal(self.command_bus))