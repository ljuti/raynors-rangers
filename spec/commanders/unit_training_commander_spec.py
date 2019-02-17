from bot.commanders.unit_training_commander import UnitTrainingCommander

from bot.structures.models.terran.barracks import BarracksModel
from bot.structures.terran.barracks import Barracks

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("UnitTrainingCommander") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.commander = UnitTrainingCommander()

    with it("can be instantiated"):
      expect(self.commander).to(be_a(UnitTrainingCommander))

  with description("Training units") as self:
    with before.each: # pylint: disable=no-member
      self.commander = UnitTrainingCommander()

    with description("Infantry") as self:
      with before.each: # pylint: disable=no-member
        self.model = BarracksModel()
        self.barracks_unit = doubles.InstanceDouble('sc2.unit.Unit')
        doubles.allow(self.barracks_unit).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.barracks_unit).tag.and_return(111)
        doubles.allow(self.barracks_unit).position.and_return(Point2((50.0, 50.0)))
        self.barracks = Barracks(self.barracks_unit, self.model)

      with _it("can train marines"):
        expect(self.commander.train).to(be_callable)
        expect(self.commander.train(UnitTypeId.MARINE)).to(be_true)