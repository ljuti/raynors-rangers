from bot.units.terran.behaviors.actions.scouting.move_to_natural_expansion import MoveToNaturalExpansion

from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from bot.units.terran.scv import SCVUnit
from bot.units.models.terran.scv import SCVModel

from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("MoveToNaturalExpansion"):
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.condition = MoveToNaturalExpansion()

    with it("can be instantiated"):
      expect(self.condition).to(be_a(MoveToNaturalExpansion))

  with description("Running the action") as self:
    with before.each: # pylint: disable=no-member
      self.scv_unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.scv_unit).tag.and_return(111)
      doubles.allow(self.scv_unit).type_id.and_return(UnitTypeId.SCV)
      doubles.allow(self.scv_unit).position.and_return(Point2((0.0, 0.0)))
      self.scv = SCVUnit(self.scv_unit, SCVModel())

      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(target=self.scv, tree=self.tree, blackboard=self.blackboard)
      self.action = MoveToNaturalExpansion()

    with it("will return RUNNING if the scout is moving to the natural expansion"):
      self.tick.blackboard.set('natural_position', Point2((20.0, 20.0)), self.tick.tree.id)
      doubles.allow(self.scv_unit).orders.and_return([doubles.InstanceDouble('sc2.unit.UnitOrder', target=Point2((20.0, 20.0)))])
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.RUNNING))

    with it("will return SUCCESS if the scout has arrived to the natural expansion"):
      self.tick.blackboard.set('natural_position', Point2((20.0, 20.0)), self.tick.tree.id)
      doubles.allow(self.scv_unit).orders.and_return([doubles.InstanceDouble('sc2.unit.UnitOrder', target=Point2((20.0, 20.0)))])
      doubles.allow(self.scv_unit).position.and_return(Point2((19.0, 19.0)))
      status = self.action._execute(self.tick)
      expect(status).to(equal(BTreeStatus.SUCCESS))
