from bot.units.terran.abilities.loadable import Loadable
from bot.units.models.terran.medivac import MedivacModel
from bot.units.models.terran.siege_tank import SiegeTankModel

from bot.service_hub import ServiceHub
from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId

service_hub = None

with description("Loadable") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot')
    self.command_bus = CommandBus(self.game)
    global service_hub
    service_hub = ServiceHub(self.game)
    service_hub.register(self.command_bus)

  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.model = SiegeTankModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.loadable = Loadable(self.unit, self.model)

    with it("can be instantiated"):
      expect(self.loadable).to(be_a(Loadable))

  with description("Abilities") as self:
    with description("Loading") as self:
      with before.each: # pylint: disable=no-member
        self.medivac_model = MedivacModel()
        self.medivac_unit = doubles.InstanceDouble('sc2.unit.Unit')
        doubles.allow(self.medivac_unit).tag.and_return(2233)
        doubles.allow(self.medivac_unit).type_id.and_return(UnitTypeId.MEDIVAC)
        doubles.allow(self.medivac_unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
        doubles.allow(self.medivac_unit).cargo_used.and_return(0)
        doubles.allow(self.medivac_unit).cargo_max.and_return(8)
        self.model = SiegeTankModel()
        self.unit = doubles.InstanceDouble('sc2.unit.Unit')
        self.loadable = Loadable(self.unit, self.model)

      with it("has a method for loading"):
        expect(self.loadable.load).to(be_callable)

      with it("loads onto the target unit"):
        doubles.expect(self.command_bus.queue)
        expect(self.loadable.load(self.medivac_unit, self.command_bus)).to(be_true)

      with it("loads onto the target unit only if there's cargo space"):
        doubles.allow(self.medivac_unit).has_cargo.and_return(True)
        doubles.allow(self.medivac_unit).cargo_used.and_return(6)
        expect(self.loadable.load(self.medivac_unit, self.command_bus)).not_to(be_true)
