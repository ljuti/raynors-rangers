from bot.commanders.build_commander import BuildCommander
from bot.commanders.behaviors.construct.structure import BuildStructureAction
from bot.commands.build_command import BuildCommand
from bot.locations.location import StructurePosition
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.enums import BTreeStatus

from bot.units.terran.scv import SCVUnit
from bot.units.models.terran.scv import SCVModel

from bot.command_bus import CommandBus
from bot.service_hub import ServiceHub
from bot.registries.unit_registry import UnitRegistry
from bot.registries.structure_registry import StructureRegistry

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, be_empty
import doubles

from sc2.constants import UnitTypeId, AbilityId
from sc2.position import Point2
from sc2.unit_command import UnitCommand
from sc2.unit import UnitOrder

with description("BuildStructureAction") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot', service_hub=ServiceHub(self))
    self.command_bus = CommandBus(self.game)
    self.unit_registry = UnitRegistry(self.game)
    self.structures = StructureRegistry()
    self.game.service_hub.register(self.command_bus)
    self.game.service_hub.register(self.unit_registry)
    self.game.service_hub.register(self.structures)

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.command = BuildCommand()
      self.data = {
        "structure": UnitTypeId.BARRACKS,
        "position": StructurePosition(Point2((50.0, 50.0)))
      }
      self.command.init(self.data)

      self.action = BuildStructureAction(self.command)

    with it("can be instantiated"):
      expect(self.action).to(be_a(BuildStructureAction))
      expect(self.action.command).not_to(equal(None))
      expect(self.action.command).to(be_a(BuildCommand))
      expect(self.action.command.is_valid).to(be_true)

  with description("Executing") as self:
    with before.each: # pylint: disable=no-member
      self.scv_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.scv_unit).type_id.and_return(UnitTypeId.SCV)
      doubles.allow(self.scv_unit).tag.and_return(111)
      doubles.allow(self.scv_unit).position.and_return(Point2((50.0, 40.0)))
      doubles.allow(self.scv_unit).build.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
      self.unit_registry.add(self.scv_unit)

      self.command = BuildCommand()
      self.data = {
        "structure": UnitTypeId.BARRACKS,
        "position": StructurePosition(Point2((50.0, 50.0)))
      }
      self.command.init(self.data)
      self.action = BuildStructureAction(self.command)
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.commander = BuildCommander(self.game.service_hub)
      self.tick = self.tree.get_tick_object(self.commander, self.blackboard)

    with it("orders an SCV to build the structure"):
      expect(self.action).to(be_a(BuildStructureAction))

      doubles.allow(self.commander).can_afford.and_return(True)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.RUNNING))
      expect(self.command_bus.actions).not_to(be_empty)

    with it("keeps running when an SCV is building the structure"):
      expect(self.action).to(be_a(BuildStructureAction))

      doubles.allow(self.commander).can_afford.and_return(True)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.RUNNING))
      expect(self.command_bus.actions).not_to(be_empty)

      doubles.allow(self.scv_unit).is_constructing_scv.and_return(True)
      doubles.allow(self.scv_unit).orders.and_return([UnitOrder(AbilityId.TERRANBUILD_BARRACKS, Point2((50.0, 40.0)), 0.0)])

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.RUNNING))

    with it("returns success when the SCV has finished building the structure"):
      expect(self.action).to(be_a(BuildStructureAction))

      doubles.allow(self.commander).can_afford.and_return(True)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.RUNNING))
      expect(self.command_bus.actions).not_to(be_empty)

      doubles.allow(self.scv_unit).is_constructing_scv.and_return(True)
      doubles.allow(self.scv_unit).orders.and_return([UnitOrder(AbilityId.TERRANBUILD_BARRACKS, Point2((50.0, 40.0)), 0.0)])

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.RUNNING))

      doubles.allow(self.scv_unit).is_constructing_scv.and_return(False)

      structure_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(structure_unit).type_id.and_return(UnitTypeId.BARRACKS)
      doubles.allow(structure_unit).tag.and_return(222)
      doubles.allow(structure_unit).is_ready.and_return(True)
      doubles.allow(structure_unit).position.and_return(Point2((50.0, 40.0)))
      self.structures.add(structure_unit)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))

    with it("fails if the structure cannot be afforded"):
      expect(self.action).to(be_a(BuildStructureAction))

      doubles.allow(self.commander).can_afford.and_return(False)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.FAILURE))
      expect(self.command_bus.actions).to(be_empty)
