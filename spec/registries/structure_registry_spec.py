from bot.registries.structure_registry import StructureRegistry
from bot.structures.terran.barracks import Barracks

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("StructureRegistry") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.registry = StructureRegistry()

    with it("can be instantiated"):
      expect(self.registry).to(be_a(StructureRegistry))

  with description("Getting objects") as self:
    with before.each: # pylint: disable=no-member
      self.registry = StructureRegistry()

    with description("with tag") as self:
      with before.each: # pylint: disable=no-member
        self.unit = doubles.InstanceDouble('sc2.unit.Unit', cache=None)
        doubles.allow(self.unit).tag.and_return(123)
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
        self.registry.objects[123]["unit"] = self.unit

      with it("returns objects by tag"):
        expect(self.registry.get_with_tag).to(be_callable)
        expect(self.registry.get_with_tag(123)).to(equal(self.unit))

    with description("with designation") as self:
      with before.each: # pylint: disable=no-member
        self.unit = doubles.InstanceDouble('sc2.unit.Unit')
        doubles.allow(self.unit).tag.and_return(123)
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.unit).position.and_return(Point2((50.0, 40.0)))
        self.registry.add(self.unit, "barracks_1")

      with it("returns objects by designation"):
        expect(self.registry.get_designated).to(be_callable)
        expect(self.registry.get_designated("barracks_1")).to(be_a(Barracks))
        structure = self.registry.get_designated("barracks_1")
        expect(structure.unit).to(equal(self.unit))

    with description("with position") as self:
      with before.each: # pylint: disable=no-member
        self.unit = doubles.InstanceDouble('sc2.unit.Unit')
        doubles.allow(self.unit).tag.and_return(123)
        doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.unit).position.and_return(Point2((50.0, 40.0)))
        self.registry.add(self.unit, "barracks_1")

      with it("returns objects by designation"):
        position = Point2((50.0, 40.0))
        expect(self.registry.get_with_position).to(be_callable)
        expect(self.registry.get_with_position(position)).to(be_a(Barracks))
        structure = self.registry.get_with_position(position)
        expect(structure).to(be_a(Barracks))
        expect(structure.unit).to(equal(self.unit))

  with description("Adding objects") as self:
    with before.each:
      self.unit = doubles.InstanceDouble('sc2.unit.Unit')
      doubles.allow(self.unit).tag.and_return(24680)
      doubles.allow(self.unit).type_id.and_return(UnitTypeId.BARRACKS)
      doubles.allow(self.unit).position.and_return(Point2((10.0,20.0)))
      self.registry = StructureRegistry()

    with it("adds objects to the registry"):
      expect(self.registry.add).to(be_callable)
      expect(self.registry.add(self.unit)).to(be_true)
      expect(self.registry.amount).to(equal(1))
      expect(self.registry.get_with_tag(self.unit.tag)).to(be_a(Barracks))
      expect(self.registry.get_designated("barracks_1")).to(equal(None))

    with it("adds objects to the registry with designation"):
      expect(self.registry.add(self.unit, "barracks_1")).to(be_true)
      expect(self.registry.get_designated("barracks_1")).to(be_a(Barracks))

  with description("Removing objects") as self:
    with before.each:
      self.registry = StructureRegistry()

    with it("responds to remove"):
      expect(self.registry.remove).to(be_callable)

  with description("Updating objects") as self:
    with before.each:
      self.registry = StructureRegistry()

    with it("responds to update"):
      expect(self.registry.update).to(be_callable)

  with description("Getting sets of objects") as self:
    with before.each:
      self.registry = StructureRegistry()

    with description("Barracks") as self:
      with before.each: # pylint: disable=no-member
        self.barracks = doubles.InstanceDouble('sc2.unit.Unit')
        self.ready_barracks = doubles.InstanceDouble('sc2.unit.Unit')
        self.ready_barracks_techlab = doubles.InstanceDouble('sc2.unit.Unit')
        self.ready_barracks_reactor = doubles.InstanceDouble('sc2.unit.Unit')
        self.techlab = doubles.InstanceDouble('sc2.unit.Unit')
        self.reactor = doubles.InstanceDouble('sc2.unit.Unit')

        doubles.allow(self.barracks).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.ready_barracks).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.ready_barracks_techlab).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.ready_barracks_reactor).type_id.and_return(UnitTypeId.BARRACKS)
        doubles.allow(self.reactor).type_id.and_return(UnitTypeId.BARRACKSREACTOR)
        doubles.allow(self.techlab).type_id.and_return(UnitTypeId.BARRACKSTECHLAB)

        doubles.allow(self.barracks).tag.and_return(123)
        doubles.allow(self.ready_barracks).tag.and_return(234)
        doubles.allow(self.ready_barracks_techlab).tag.and_return(345)
        doubles.allow(self.ready_barracks_techlab).add_on_tag.and_return(999)
        doubles.allow(self.ready_barracks_reactor).tag.and_return(456)
        doubles.allow(self.ready_barracks_reactor).add_on_tag.and_return(888)
        doubles.allow(self.reactor).tag.and_return(888)
        doubles.allow(self.techlab).tag.and_return(999)

        doubles.allow(self.barracks).position.and_return(Point2((50.0, 50.0)))
        doubles.allow(self.ready_barracks).position.and_return(Point2((40.0, 40.0)))
        doubles.allow(self.ready_barracks_techlab).position.and_return(Point2((30.0, 30.0)))
        doubles.allow(self.ready_barracks_reactor).position.and_return(Point2((20.0, 20.0)))
        doubles.allow(self.reactor).position.and_return(Point2((15.0, 15.0)))
        doubles.allow(self.techlab).position.and_return(Point2((10.0, 10.0)))

        self.registry.add(self.barracks)
        self.registry.add(self.ready_barracks)
        self.registry.add(self.ready_barracks_techlab)
        self.registry.add(self.ready_barracks_reactor)
        self.registry.add(self.reactor)
        self.registry.add(self.techlab)

      with it("returns all barracks"):
        expect(self.registry.barracks).to(be_callable)
        expect(self.registry.barracks()).to(be_a(list))
        result = self.registry.barracks()
        expect(len(result)).to(be_above(0))
        for structure in result:
          expect(structure).to(be_a(Barracks))

      with it("returns all production barracks"):
        barracks = self.registry.get_with_tag(self.ready_barracks.tag)
        barracks.production_ready = True
        expect(self.registry.production_barracks).to(be_callable)
        expect(self.registry.production_barracks()).to(be_a(list))
        result = self.registry.production_barracks()
        expect(len(result)).to(equal(1))
        expect(result[0]).to(be_a(Barracks))
        expect(result[0].unit).to(equal(self.ready_barracks))

      with it("returns all techlabbed production barracks"):
        barracks = self.registry.get_with_tag(self.ready_barracks_techlab.tag)
        barracks.production_ready = True
        expect(self.registry.production_barracks_with_techlab).to(be_callable)
        expect(self.registry.production_barracks_with_techlab()).to(be_a(list))
        result = self.registry.production_barracks_with_techlab()
        expect(len(result)).to(equal(1))
        expect(result[0]).to(be_a(Barracks))
        expect(result[0].unit).to(equal(self.ready_barracks_techlab))

      with it("returns all reactored production barracks"):
        barracks = self.registry.get_with_tag(self.ready_barracks_reactor.tag)
        barracks.production_ready = True
        expect(self.registry.production_barracks_with_reactor).to(be_callable)
        expect(self.registry.production_barracks_with_reactor()).to(be_a(list))
        result = self.registry.production_barracks_with_reactor()
        expect(len(result)).to(equal(1))
        expect(result[0]).to(be_a(Barracks))
        expect(result[0].unit).to(equal(self.ready_barracks_reactor))