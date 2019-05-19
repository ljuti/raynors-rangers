from bot.structures.terran.starport import Starport
from bot.structures.models.terran.starport import StarportModel

from bot.command_bus import CommandBus
from bot.registries.structure_registry import StructureRegistry

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

  with description("Abilities") as self:
    with before.each: # pylint: disable=no-member
      self.model = StarportModel()
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.unit).tag.and_return(112233)
      doubles.allow(self.unit).type_id.and_return(UnitTypeId.STARPORT)
      doubles.allow(self.unit).position.and_return(Point2((50.0, 50.0)))
      self.structure = Starport(self.unit, self.model)

    with description("Landing") as self:
      with it("has a method for landing"):
        expect(self.structure.land).to(be_callable)

    with description("Lifting") as self:
      with it("has a method for lifting"):
        expect(self.structure.lift).to(be_callable)

    with description("Building a reactor") as self:
      with it("has a method for building a reactor"):
        expect(self.structure.build_reactor).to(be_callable)

    with description("Building a techlab") as self:
      with it("has a method for building a techlab"):
        expect(self.structure.build_techlab).to(be_callable)

  with description("Upgrades") as self:
    with before.each: # pylint: disable=no-member
      self.registry = StructureRegistry()
      doubles.allow(self.unit).add_on_tag.and_return(999)
      self.techlab_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.techlab_unit).type_id.and_return(UnitTypeId.STARPORTTECHLAB)
      doubles.allow(self.techlab_unit).tag.and_return(999)
      doubles.allow(self.techlab_unit).position.and_return(Point2((10.0, 10.0)))
      unit_list = doubles.InstanceDouble('sc2.units.Units')
      doubles.allow(unit_list).find_by_tag(999).and_return(self.techlab_unit)

      self.registry.add(self.unit)
      self.registry.add(self.techlab_unit)

      self.game = doubles.InstanceDouble('sc2.bot_ai.BotAI', units=unit_list, command_bus=CommandBus(self), structures=self.registry)

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

  with description("Training units") as self:
    with description("Medivacs") as self:
      with it("can train medivacs"):
        expect(self.structure.train_medivac).to(be_callable)

    with description("Liberators") as self:
      with it("can train liberators"):
        expect(self.structure.train_medivac).to(be_callable)

    with description("Banshees") as self:
      with it("can train banshees"):
        expect(self.structure.train_banshee).to(be_callable)

    with description("Ravens") as self:
      with it("can train ravens"):
        expect(self.structure.train_raven).to(be_callable)

    with description("Vikings") as self:
      with it("can train vikings"):
        expect(self.structure.train_viking).to(be_callable)

    with description("Battlecruisers") as self:
      with it("can train battlecruisers"):
        expect(self.structure.train_battlecruiser).to(be_callable)