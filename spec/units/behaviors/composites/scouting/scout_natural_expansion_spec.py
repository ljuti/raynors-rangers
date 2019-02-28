from bot.units.terran.behaviors.composites.scouting.scout_natural_expansion import ScoutNaturalExpansion

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

from sc2.position import Point2
from sc2.constants import UnitTypeId

with description("ScoutNaturalExpansion") as self:
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
      self.sequence = ScoutNaturalExpansion(self.locations)

    with it("can be instantiated"):
      expect(self.sequence).to(be_a(ScoutNaturalExpansion))

  with description("Executing the sequence") as self:
    with before.each: # pylint: disable=no-member
      self.locations = LocationData()
      self.locations.natural = Point2((50.0, 50.0))
      self.sequence = ScoutNaturalExpansion(self.locations)

      self.scv_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.scv_unit).tag.and_return(111)
      doubles.allow(self.scv_unit).type_id.and_return(UnitTypeId.SCV)
      doubles.allow(self.scv_unit).position.and_return(Point2((0.0, 0.0)))
      self.scv = SCVUnit(self.scv_unit, SCVModel(), service_hub=self.game.service_hub)

      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(target=self.scv, tree=self.tree, blackboard=self.blackboard)
      
    with description("Entering the sequence") as self:
      with it("has natural position in the blackboard"):
        self.sequence.enter(self.tick)
        expect(self.blackboard.get('natural_position', self.tick.tree.id)).to(be_a(Point2))
        expect(self.blackboard.get('natural_position', self.tick.tree.id)).to(equal(self.locations.natural))

    with description("Scouting natural expansion") as self:
      with it("scouts the natural expansion"):
        doubles.allow(self.scv_unit).orders.and_return([])
        doubles.allow(self.scv_unit).move.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))

        self.sequence.enter(self.tick)
        status = self.sequence.tick(self.tick)
        expect(status).to(equal(BTreeStatus.RUNNING))

        doubles.allow(self.scv_unit).orders.and_return([doubles.InstanceDouble('sc2.unit.UnitOrder', target=self.locations.natural)])
        doubles.allow(self.scv_unit).order_target.and_return(self.locations.natural)
        status = self.sequence.tick(self.tick)
        expect(status).to(equal(BTreeStatus.RUNNING))

        doubles.allow(self.scv_unit).position.and_return(Point2((48.0, 48.0)))
        status = self.sequence.tick(self.tick)
        expect(status).to(equal(BTreeStatus.SUCCESS))
