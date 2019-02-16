from bot.structures.terran.abilities.landable import Landable
from bot.structures.models.terran.barracks import BarracksModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_empty
import doubles

from sc2.position import Point2
from sc2.constants import UnitTypeId

with description("Landable") as self:
  with before.each: # pylint: disable=no-member
    self.command_bus = CommandBus(doubles.InstanceDouble('bot.MyBot'))

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.model = BarracksModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.landable = Landable(self.unit, self.model)

    with it("can be initialized"):
      expect(self.landable).to(be_a(Landable))

  with description("Ability") as self:
    with before.each: # pylint: disable=no-member
      self.model = BarracksModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.landable = Landable(self.unit, self.model)

    with description("Barracks") as self:
      with before.each: # pylint: disable=no-member
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
        doubles.allow(self.unit).orders.and_return([])

      with it("can be landed with specified landing position"):
        expect(self.landable.land).to(be_callable)
        self.landable.landing_position = Point2((50.0, 50.0))
        expect(self.landable.land(self.command_bus)).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
