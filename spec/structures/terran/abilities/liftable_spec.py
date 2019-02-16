from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.models.terran.barracks import BarracksModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_empty
import doubles

from sc2.constants import UnitTypeId

with description("Liftable") as self:
  with before.each: # pylint: disable=no-member
    self.command_bus = CommandBus(doubles.InstanceDouble('bot.MyBot'))

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.model = BarracksModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.liftable = Liftable(self.unit, self.model)

    with it("can be initialized"):
      expect(self.liftable).to(be_a(Liftable))

  with description("Ability") as self:
    with before.each: # pylint: disable=no-member
      self.model = BarracksModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.liftable = Liftable(self.unit, self.model)

    with description("Barracks") as self:
      with before.each: # pylint: disable=no-member
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
        doubles.allow(self.unit).orders.and_return([])

      with it("can be lifted"):
        expect(self.liftable.lift).to(be_callable)
        expect(self.liftable.lift(self.command_bus)).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
  
    with description("Factory") as self:
      with before.each: # pylint: disable=no-member
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.FACTORY)
        doubles.allow(self.unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
        doubles.allow(self.unit).orders.and_return([])

      with it("can be lifted"):
        expect(self.liftable.lift).to(be_callable)
        expect(self.liftable.lift(self.command_bus)).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
  
    with description("Starport") as self:
      with before.each: # pylint: disable=no-member
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.STARPORT)
        doubles.allow(self.unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
        doubles.allow(self.unit).orders.and_return([])

      with it("can be lifted"):
        expect(self.liftable.lift).to(be_callable)
        expect(self.liftable.lift(self.command_bus)).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
  