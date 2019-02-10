from bot.structures.terran.starport import Starport
from bot.structures.models.terran.starport import StarportModel

from bot.command_bus import CommandBus

from sc2.units import Units
from sc2.unit import Unit
from sc2.position import Point2
from sc2.constants import UnitTypeId, AbilityId, UpgradeId

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, be_false
import doubles

with description("Starport") as self:
  with before.each: # pylint: disable=no-member
    self.model = StarportModel()
    self.unit = doubles.InstanceDouble('sc2.unit.Unit')
    doubles.allow(self.unit).tag.and_return(112233)
    doubles.allow(self.unit).type_id.and_return(UnitTypeId.STARPORT)
    doubles.allow(self.unit).position.and_return(Point2((50.0, 50.0)))
    self.structure = Starport(self.unit, self.model)

  with description("Initialization") as self:
    with it("can be instantiated"):
      expect(self.structure).to(be_a(Starport))

  with description("Upgrades") as self:
    with before.each: # pylint: disable=no-member
      doubles.allow(self.unit).add_on_tag.and_return(999)
      self.techlab_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.techlab_unit).type_id.and_return(UnitTypeId.STARPORTTECHLAB)
      unit_list = doubles.InstanceDouble('sc2.units.Units')
      doubles.allow(unit_list).find_by_tag(999).and_return(self.techlab_unit)

      self.game = doubles.InstanceDouble('sc2.bot_ai.BotAI', units=unit_list, command_bus=CommandBus(self))

    with description("Banshee cloak"):
      with it("can queue Banshee cloak research"):
        doubles.allow(self.techlab_unit).research(UpgradeId.BANSHEECLOAK)
        doubles.allow(self.game).can_afford(UpgradeId.BANSHEECLOAK).and_return(True)
        expect(self.structure.research_banshee_cloak).to(be_callable)
        expect(self.structure.research_banshee_cloak(self.game)).to(be_true)

      with it("will not queue Banshee cloak research if it cannot afford it"):
        doubles.allow(self.game).can_afford(UpgradeId.BANSHEECLOAK).and_return(False)
        expect(self.structure.research_banshee_cloak).to(be_callable)
        expect(self.structure.research_banshee_cloak(self.game)).to(be_false)

    with description("Banshee speed"):
      with it("can queue Banshee speed research"):
        doubles.allow(self.techlab_unit).research(UpgradeId.BANSHEESPEED)
        doubles.allow(self.game).can_afford(UpgradeId.BANSHEESPEED).and_return(True)
        expect(self.structure.research_banshee_speed).to(be_callable)
        expect(self.structure.research_banshee_speed(self.game)).to(be_true)

      with it("will not queue Banshee speed research if it cannot afford it"):
        doubles.allow(self.game).can_afford(UpgradeId.BANSHEESPEED).and_return(False)
        expect(self.structure.research_banshee_speed).to(be_callable)
        expect(self.structure.research_banshee_speed(self.game)).to(be_false)

    with description("Advanced ballistics"):
      with it("can queue Liberator Advanced Ballistics research"):
        doubles.allow(self.techlab_unit).research(UpgradeId.LIBERATORAGRANGEUPGRADE)
        doubles.allow(self.game).can_afford(UpgradeId.LIBERATORAGRANGEUPGRADE).and_return(True)
        expect(self.structure.research_advanced_ballistics).to(be_callable)
        expect(self.structure.research_advanced_ballistics(self.game)).to(be_true)

      with it("will not queue Liberator Advanced Ballistics research if it cannot afford it"):
        doubles.allow(self.game).can_afford(UpgradeId.LIBERATORAGRANGEUPGRADE).and_return(False)
        expect(self.structure.research_advanced_ballistics).to(be_callable)
        expect(self.structure.research_advanced_ballistics(self.game)).to(be_false)