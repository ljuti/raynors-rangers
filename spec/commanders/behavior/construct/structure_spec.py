from bot.commanders.build_commander import BuildCommander
from bot.commanders.behaviors.construct.structure import BuildStructureAction
from bot.commands.build_command import BuildCommand
from bot.locations.location import StructurePosition
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.enums import BTreeStatus

from bot.command_bus import CommandBus
from bot.service_hub import ServiceHub
from bot.registries.unit_registry import UnitRegistry

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, be_empty
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2
from sc2.unit_command import UnitCommand

with description("BuildStructureAction") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot', service_hub=ServiceHub(self))
    self.command_bus = CommandBus(self.game)
    self.unit_registry = UnitRegistry(self.game)
    self.game.service_hub.register(self.command_bus)
    self.game.service_hub.register(self.unit_registry)

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

    with it("builds the structure"):
      expect(self.action).to(be_a(BuildStructureAction))

      doubles.allow(self.commander).can_afford.and_return(True)

      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))
      expect(self.command_bus.actions).not_to(be_empty)
      for action in self.command_bus.actions:
        expect(action).to(be_a(UnitCommand))