from bot.structures.terran.barracks import Barracks
from bot.structures.models.terran.barracks import BarracksModel

from sc2.unit import Unit

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable
import doubles

with description("Barracks") as self:
  with before.each: # pylint: disable=no-member
    self.model = BarracksModel()
    self.unit = doubles.InstanceDouble('sc2.unit.Unit')
    doubles.allow(self.unit).tag.and_return(112233)
    self.structure = Barracks(self.unit, self.model)
