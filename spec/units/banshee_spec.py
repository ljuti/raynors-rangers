from bot.units.terran.banshee import BansheeUnit
from bot.units.models.terran.banshee import BansheeModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId

with description("BansheeUnit") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot')
    self.command_bus = CommandBus(self.game)

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      banshee_model = BansheeModel()
      banshee_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(banshee_unit).tag.and_return(999)
      doubles.allow(banshee_unit).type_id.and_return(UnitTypeId.BANSHEE)
      self.unit = BansheeUnit(banshee_unit, banshee_model)

    with it("can be instatiated"):
      expect(self.unit).to(be_a(BansheeUnit))
      expect(self.unit.tag).to(equal(999))
      expect(self.unit.type_id).to(equal(UnitTypeId.BANSHEE))

  with description("Abilities") as self:
    with description("Cloaking") as self:
      with before.each: # pylint: disable=no-member
        banshee_model = BansheeModel()
        game_data = doubles.InstanceDouble('sc2.game_data.GameData', cloak=1)
        self.banshee_unit = doubles.InstanceDouble('sc2.unit.Unit', _proto=game_data)
        doubles.allow(self.banshee_unit).tag.and_return(999)
        doubles.allow(self.banshee_unit).type_id.and_return(UnitTypeId.BANSHEE)
        doubles.allow(self.banshee_unit).energy.and_return(100)
        doubles.allow(self.banshee_unit).__call__.and_return(None)
        self.unit = BansheeUnit(self.banshee_unit, banshee_model)

      with it("has a method for cloaking the unit"):
        expect(self.unit.cloak).to(be_callable)

      with it("will cloak unit if it has sufficient energy"):
        expect(self.unit.cloak(self.command_bus)).to(be_true)

      with it("will not cloak the unit if it doesn't have sufficient energy"):
        doubles.allow(self.banshee_unit).energy.and_return(0)
        expect(self.unit.cloak(self.command_bus)).not_to(be_true)

      with it("has a method for decloaking the unit"):
        expect(self.unit.de_cloak).to(be_callable)
        expect(self.unit.de_cloak(self.command_bus)).to(be_true)

      with it("can tell how long it's going to be cloaked"):
        expect(self.unit).to(have_property('cloak_left_in_seconds'))
        expect(self.unit.cloak_left_in_seconds).to(equal(79))

      with it("has a property to tell if it's fully cloaked"):
        expect(self.unit).to(have_property('is_fully_cloaked'))

      with it("has a property to tell if it's cloaked but detected"):
        expect(self.unit).to(have_property('is_cloaked_but_detected'))
