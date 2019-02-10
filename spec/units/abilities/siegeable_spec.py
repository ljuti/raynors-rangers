from bot.units.terran.abilities.siegeable import Siegeable
from bot.units.models.terran.liberator import LiberatorModel
from bot.units.models.terran.siege_tank import SiegeTankModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId

with description("Siegeable") as self:
  with before.each: # pylint: disable=no-member
    self.game = doubles.InstanceDouble('bot.MyBot')
    self.command_bus = CommandBus(self.game)

  with description("Properties") as self:
    with before.each: # pylint: disable=no-member
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.model = SiegeTankModel()
      doubles.allow(self.unit).unit_alias.and_return([UnitTypeId.SIEGETANKSIEGED])
      self.siegeable = Siegeable(self.unit, self.model)

    with it("has a range property"):
      expect(self.siegeable).to(have_property('range'))

    with it("has a sieged range property"):
      expect(self.siegeable).to(have_property('range_sieged'))
      expect(self.siegeable.range_sieged).to(equal(self.model.range_sieged))

    with it("has a unsieged range property"):
      expect(self.siegeable).to(have_property('range_unsieged'))
      expect(self.siegeable.range_unsieged).to(equal(self.model.range_unsieged))

  with description("Sieging") as self:
    with before.each: # pylint: disable=no-member
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.model = SiegeTankModel()
      self.siegeable = Siegeable(self.unit, self.model)

    with it("has a method for sieging"):
      expect(self.siegeable.siege).to(be_callable)

    with it("will siege when it can"):
      doubles.allow(self.unit).unit_alias.and_return(None)
      doubles.allow(self.unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
      expect(self.siegeable.siege(self.command_bus)).to(be_true)
      doubles.allow(self.unit).unit_alias.and_return([UnitTypeId.SIEGETANKSIEGED])
      expect(self.siegeable.is_sieged).to(be_true)

    with it("will not siege when already sieged"):
      doubles.allow(self.unit).unit_alias.and_return([UnitTypeId.SIEGETANKSIEGED])
      expect(self.siegeable.is_sieged).to(be_true)
      expect(self.siegeable.siege(self.command_bus)).not_to(be_true)

  with description("Unsieging") as self:
    with before.each: # pylint: disable=no-member
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      self.model = SiegeTankModel()
      self.siegeable = Siegeable(self.unit, self.model)

    with it("has a method for unsieging"):
      expect(self.siegeable.unsiege).to(be_callable)

    with it("will unsiege when it can"):
      doubles.allow(self.unit).unit_alias.and_return([UnitTypeId.SIEGETANKSIEGED])
      doubles.allow(self.unit).__call__.and_return(doubles.InstanceDouble('sc2.unit_command.UnitCommand'))
      expect(self.siegeable.unsiege(self.command_bus)).to(be_true)
      doubles.allow(self.unit).unit_alias.and_return(None)
      expect(self.siegeable.is_not_sieged).to(be_true)

    with it("will not siege when already sieged"):
      doubles.allow(self.unit).unit_alias.and_return(None)
      expect(self.siegeable.is_not_sieged).to(be_true)
      expect(self.siegeable.unsiege(self.command_bus)).not_to(be_true)
