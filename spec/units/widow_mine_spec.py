from bot.units.terran.widow_mine import WidowMineUnit
from bot.units.models.terran.widow_mine import WidowMineModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId

with description("WidowMineUnit") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot')
    self.command_bus = CommandBus(self.game)

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      model = WidowMineModel()
      unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(unit).tag.and_return(999)
      doubles.allow(unit).type_id.and_return(UnitTypeId.WIDOWMINE)
      self.unit = WidowMineUnit(unit, model)

    with it("can be instatiated"):
      expect(self.unit).to(be_a(WidowMineUnit))
      expect(self.unit.tag).to(equal(999))
      expect(self.unit.type_id).to(equal(UnitTypeId.WIDOWMINE))

  with description("Abilities") as self:
    with description("Burrow") as self:
      with before.each: # pylint: disable=no-member
        model = WidowMineModel()
        self.wm_unit = doubles.InstanceDouble('sc2.unit.Unit')
        doubles.allow(self.wm_unit).tag.and_return(999)
        doubles.allow(self.wm_unit).type_id.and_return(UnitTypeId.BANSHEE)
        doubles.allow(self.wm_unit).energy.and_return(100)
        doubles.allow(self.wm_unit).__call__.and_return(None)
        self.unit = WidowMineUnit(self.wm_unit, model)

      with it("has a method for burrowing"):
        expect(self.unit.burrow).to(be_callable)

      with it("has a method for unburrowing"):
        expect(self.unit.unburrow).to(be_callable)

      with it("will burrow"):
        doubles.allow(self.wm_unit).is_burrowed.and_return(False)
        expect(self.unit.burrow(self.command_bus)).to(be_true)

      with it("will unburrow"):
        doubles.allow(self.wm_unit).is_burrowed.and_return(True)
        expect(self.unit.unburrow(self.command_bus)).to(be_true)

      with it("will not burrow if already burrowed"):
        doubles.allow(self.wm_unit).is_burrowed.and_return(True)
        expect(self.unit.burrow(self.command_bus)).not_to(be_true)

      with it("will not unburrow if already above ground"):
        doubles.allow(self.wm_unit).is_burrowed.and_return(False)
        expect(self.unit.unburrow(self.command_bus)).not_to(be_true)
