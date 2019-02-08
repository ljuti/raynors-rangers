from bot.stores.economic_data import EconomicData

from sc2.score import ScoreDetails

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true
import doubles

with description("EconomicData") as self:
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.store = EconomicData()

    with it("can be instantiated"):
      expect(self.store).to(be_a(EconomicData))

  with description("Income rates") as self:
    with before.each: # pylint: disable=no-member
      self.score = doubles.InstanceDouble('sc2.score.ScoreDetails')
      doubles.allow(self.score).collected_minerals.and_return(2000)
      doubles.allow(self.score).collected_vespene.and_return(800)
      doubles.allow(self.score).collection_rate_minerals.and_return(800)
      doubles.allow(self.score).collection_rate_vespene.and_return(300)
      self.store = EconomicData()
      self.store.update_economy_data(self.score)

    with description("Mineral income") as self:
      with it("reports mineral income rate"):
        expect(self.store.collection_rate_minerals).to(equal(800))

    with description("Gas income") as self:
      with it("reports gas income rate"):
        expect(self.store.collection_rate_gas).to(equal(300))

  with description("Evaluating if ahead") as self:
    with before.each: # pylint: disable=no-member
      self.score = doubles.InstanceDouble('sc2.score.ScoreDetails')

    with description("economically") as self:
      with before.each: # pylint: disable=no-member
        doubles.allow(self.score).killed_minerals_economy.and_return(2000)
        doubles.allow(self.score).killed_vespene_economy.and_return(800)
        doubles.allow(self.score).lost_minerals_economy.and_return(1000)
        doubles.allow(self.score).lost_vespene_economy.and_return(400)
        self.store = EconomicData()
        self.store.scores = self.score

      with it("reports we're ahead"):
        expect(self.store.ahead_economically).to(be_true)

    with description("with army") as self:
      with before.each: # pylint: disable=no-member
        doubles.allow(self.score).killed_minerals_army.and_return(2000)
        doubles.allow(self.score).killed_vespene_army.and_return(800)
        doubles.allow(self.score).lost_minerals_army.and_return(1000)
        doubles.allow(self.score).lost_vespene_army.and_return(400)
        self.store = EconomicData()
        self.store.scores = self.score

      with it("reports we're ahead"):
        expect(self.store.ahead_in_army).to(be_true)
