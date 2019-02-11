from bot.units.terran.siege_tank import SiegeTankUnit
from bot.units.models.terran.siege_tank import SiegeTankModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("SiegeTank") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot')
    self.command_bus = CommandBus(self.game)

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      model = SiegeTankModel()
      tank_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(tank_unit).tag.and_return(1234)
      doubles.allow(tank_unit).type_id.and_return(UnitTypeId.SIEGETANK)
      doubles.allow(tank_unit).position.and_return(Point2((10.0, 20.0)))
      self.unit = SiegeTankUnit(tank_unit, model)

    with it("can be instantiated"):
      expect(self.unit).to(be_a(SiegeTankUnit))
      expect(self.unit.tag).to(equal(1234))
      expect(self.unit.type_id).to(equal(UnitTypeId.SIEGETANK))

  with description("Abilities") as self:
    with description("Sieging") as self:
      with before.each: # pylint: disable=no-member
        model = SiegeTankModel()
        self.tank_unit = doubles.InstanceDouble('sc2.unit.Unit')
        doubles.allow(self.tank_unit).tag.and_return(1234)
        doubles.allow(self.tank_unit).type_id.and_return(UnitTypeId.SIEGETANK)
        doubles.allow(self.tank_unit).position.and_return(Point2((10.0, 20.0)))
        doubles.allow(self.tank_unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
        self.unit = SiegeTankUnit(self.tank_unit, model)

      with it("has a method for sieging"):
        expect(self.unit.siege).to(be_callable)

      with it("has a method for unsieging"):
        expect(self.unit.unsiege).to(be_callable)

  with description("Properties") as self:
    with before.each: # pylint: disable=no-member
      self.model = SiegeTankModel()
      self.tank_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.tank_unit).tag.and_return(1234)
      doubles.allow(self.tank_unit).type_id.and_return(UnitTypeId.SIEGETANK)
      doubles.allow(self.tank_unit).position.and_return(Point2((10.0, 20.0)))
      doubles.allow(self.tank_unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
      self.unit = SiegeTankUnit(self.tank_unit, self.model)

    with it("has a property for range"):
      doubles.allow(self.tank_unit).unit_alias.and_return(None)
      expect(self.unit).to(have_property('range'))
      expect(self.unit.range).to(equal(self.model.range_unsieged))

    with it("the range changes when sieged"):
      doubles.allow(self.tank_unit).unit_alias.and_return(None)
      expect(self.unit.siege(self.command_bus)).to(be_true)
      doubles.allow(self.tank_unit).unit_alias.and_return([self.model.sieged_type_id])
      expect(self.unit.range).to(equal(self.model.range_sieged))
