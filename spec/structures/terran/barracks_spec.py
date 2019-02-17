from bot.structures.terran.barracks import Barracks
from bot.structures.models.terran.barracks import BarracksModel

from bot.command_bus import CommandBus

from sc2.unit import Unit
from sc2.constants import AbilityId, UnitTypeId
from sc2.position import Point2

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, be_empty
import doubles

with description("Barracks") as self:
  with before.each: # pylint: disable=no-member
    self.model = BarracksModel()
    self.unit = doubles.InstanceDouble('sc2.unit.Unit')
    doubles.allow(self.unit).tag.and_return(112233)
    doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
    doubles.allow(self.unit).position.and_return(Point2((50.0, 50.0)))
    self.structure = Barracks(self.unit, self.model)

    self.game = doubles.InstanceDouble('bot.MyBot')
    self.command_bus = CommandBus(self.game)

  with description("Initialization") as self:
    with it("can be instantiated"):
      expect(self.structure).to(be_a(Barracks))

  with description("Upgrades") as self:
    pass

  with description("Training units") as self:
    with before.each: # pylint: disable=no-member
      self.structure.command_bus = self.command_bus

    with description("Marines") as self:
      with before.each: # pylint: disable=no-member
        action = doubles.InstanceDouble('sc2.unit_command.UnitCommand', ability=AbilityId.BARRACKSTRAIN_MARINE, unit=self.structure.unit)
        doubles.allow(self.unit).train.and_return(action)

      with it("can train marines") as self:
        expect(self.structure.train_marine).to(be_callable)
        expect(self.structure.train_marine()).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
        for action in self.command_bus.actions:
          expect(action.ability).to(equal(AbilityId.BARRACKSTRAIN_MARINE))
          expect(action.unit).to(equal(self.structure.unit))

    with description("Marauders") as self:
      with before.each: # pylint: disable=no-member
        action = doubles.InstanceDouble('sc2.unit_command.UnitCommand', ability=AbilityId.BARRACKSTRAIN_MARAUDER, unit=self.structure.unit)
        doubles.allow(self.unit).train.and_return(action)

      with it("can train marines") as self:
        expect(self.structure.train_marauder).to(be_callable)
        expect(self.structure.train_marauder()).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
        for action in self.command_bus.actions:
          expect(action.ability).to(equal(AbilityId.BARRACKSTRAIN_MARAUDER))
          expect(action.unit).to(equal(self.structure.unit))

    with description("Reapers") as self:
      with before.each: # pylint: disable=no-member
        action = doubles.InstanceDouble('sc2.unit_command.UnitCommand', ability=AbilityId.BARRACKSTRAIN_REAPER, unit=self.structure.unit)
        doubles.allow(self.unit).train.and_return(action)

      with it("can train marines") as self:
        expect(self.structure.train_reaper).to(be_callable)
        expect(self.structure.train_reaper()).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
        for action in self.command_bus.actions:
          expect(action.ability).to(equal(AbilityId.BARRACKSTRAIN_REAPER))
          expect(action.unit).to(equal(self.structure.unit))

    with description("Ghosts") as self:
      with before.each: # pylint: disable=no-member
        action = doubles.InstanceDouble('sc2.unit_command.UnitCommand', ability=AbilityId.BARRACKSTRAIN_GHOST, unit=self.structure.unit)
        doubles.allow(self.unit).train.and_return(action)

      with it("can train marines") as self:
        expect(self.structure.train_ghost).to(be_callable)
        expect(self.structure.train_ghost()).to(be_true)
        expect(self.command_bus.actions).not_to(be_empty)
        for action in self.command_bus.actions:
          expect(action.ability).to(equal(AbilityId.BARRACKSTRAIN_GHOST))
          expect(action.unit).to(equal(self.structure.unit))
