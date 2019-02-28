from bot.units.terran.behaviors.composites.scouting.scout_for_proxies import ScoutForProxies

from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus
from bot.btrees.core.blackboard import Blackboard

from bot.stores.location_data import LocationData
from bot.units.models.terran.scv import SCVModel
from bot.units.terran.scv import SCVUnit

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from bot.service_hub import ServiceHub
from bot.command_bus import CommandBus

from collections import deque

from sc2.position import Point2
from sc2.constants import UnitTypeId

with description("ScoutForProxies") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot', service_hub=ServiceHub(self))
    self.game.service_hub.register(CommandBus(self.game))

  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.locations = LocationData()
      self.locations.natural = Point2((50.0, 50.0))
      self.locations.map_center = Point2((100.0, 100.0))
      self.locations.ordered_expansions = [None, None, Point2((25.0, 25.0)), Point2((35.0, 35.0))]
      self.locations.prepare_proxy_locations()
      self.sequence = ScoutForProxies(self.locations)

    with it("can be instantiated"):
      expect(self.sequence).to(be_a(ScoutForProxies))

  with description("Executing the sequence") as self:
    with before.each: # pylint: disable=no-member
      self.locations = LocationData()
      self.locations.natural = Point2((50.0, 50.0))
      self.locations.map_center = Point2((100.0, 100.0))
      self.locations.ordered_expansions = [None, None, Point2((25.0, 25.0)), Point2((35.0, 35.0))]
      self.locations.prepare_proxy_locations()
      self.sequence = ScoutForProxies(self.locations)

      self.scv_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.scv_unit).tag.and_return(111)
      doubles.allow(self.scv_unit).type_id.and_return(UnitTypeId.SCV)
      doubles.allow(self.scv_unit).position.and_return(Point2((0.0, 0.0)))
      self.scv = SCVUnit(self.scv_unit, SCVModel(), service_hub=self.game.service_hub)

      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(target=self.scv, tree=self.tree, blackboard=self.blackboard)
      
    with description("Entering the sequence") as self:
      with it("has scouting locations in the blackboard"):
        self.sequence.enter(self.tick)
        expect(self.blackboard.get('scouting_locations', self.tick.tree.id)).to(be_a(deque))

    with description("Scouting for proxies") as self:
      with it("scouts"):
        doubles.allow(self.scv_unit).orders.and_return([])
        doubles.allow(self.scv_unit).move.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))

        self.sequence.enter(self.tick)
        self.sequence.open(self.tick)
        status = self.sequence.tick(self.tick)
        expect(status).to(equal(BTreeStatus.RUNNING))

        print(self.blackboard._tree_memory)
        doubles.allow(self.scv_unit).position.and_return(Point2((25.0, 25.0)))

        status = self.sequence.tick(self.tick)
        expect(status).to(equal(BTreeStatus.SUCCESS))
        print(self.blackboard._tree_memory)

        doubles.allow(self.scv_unit).position.and_return(Point2((35.0, 35.0)))
        status = self.sequence.tick(self.tick)
        expect(status).to(equal(BTreeStatus.SUCCESS))
