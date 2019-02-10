from bot.registries.base_registry import BaseRegistry

from collections import defaultdict

from mamba import description, context, it
from expects import *

from sc2.units import Units
from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("BaseRegistry") as self:
  with description("Initialization") as self:
    with before.each:
      self.registry = BaseRegistry()

  with description("Properties") as self:
    with before.each:
      self.registry = BaseRegistry()

    with it("has a dictionary for objects"):
      expect(self.registry).to(have_property('objects'))
      expect(self.registry.objects).to(be_a(defaultdict))

  with description("Getting objects") as self:
    with before.each:
      self.registry = BaseRegistry()

    with description("with tag") as self:
      with before.each:
        self.registry.objects[123]["unit"] = "Unit"

      with it("returns objects by tag"):
        expect(self.registry.get_with_tag).to(be_callable)
        expect(self.registry.get_with_tag(123)).to(equal("Unit"))

    with description("with designation") as self:
      with before.each:
        self.registry.objects[123]["unit"] = "BARRACKSOBJECT"
        self.registry.objects[123]["designation"] = "barracks_1"

      with it("returns objects by designation"):
        expect(self.registry.get_with_designation).to(be_callable)
        expect(self.registry.get_with_designation("barracks_1")).to(equal("BARRACKSOBJECT"))

    with description("with position") as self:
      with before.each:
        self.registry.objects[123]["unit"] = "BARRACKSOBJECT"
        self.registry.objects[123]["position"] = Point2((50.0, 40.0))

      with it("returns objects by designation"):
        expect(self.registry.get_with_position).to(be_callable)
        expect(self.registry.get_with_position(Point2((50.0, 40.0)))).to(equal("BARRACKSOBJECT"))

  with description("Adding objects") as self:
    with before.each:
      self.registry = BaseRegistry()

    with it("responds to add"):
      expect(self.registry.add).to(be_callable)

  with description("Removing objects") as self:
    with before.each:
      self.registry = BaseRegistry()

    with it("responds to add"):
      expect(self.registry.remove).to(be_callable)

  with description("Updating objects") as self:
    with before.each:
      self.registry = BaseRegistry()

    with it("responds to add"):
      expect(self.registry.update).to(be_callable)