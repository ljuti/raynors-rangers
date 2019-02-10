from bot.commands.requirements.build_command import BuildCommandRequirement, RequirementType
from bot.commands.build_command import BuildCommand
from bot.locations.location import StructurePosition

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, contain
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2

from copy import deepcopy

with description("BuildCommandRequirement") as self:
  with description("Initialization"):
    with it("can be instantiated"):
      requirement = BuildCommandRequirement()
      expect(requirement).to(be_a(BuildCommandRequirement))

  with description("Resolving requirement type") as self:
    with before.each: # pylint: disable=no-member
      self.requirement = BuildCommandRequirement({})

    with it("resolves requirement type as structure"):
      expect(self.requirement.resolve_requirement_type).to(be_callable)
      expect(self.requirement.resolve_requirement_type("structure")).to(equal(RequirementType.STRUCTURE))

    with it("resolves requirement type as designated"):
      expect(self.requirement.resolve_requirement_type).to(be_callable)
      expect(self.requirement.resolve_requirement_type("designation")).to(equal(RequirementType.DESIGNATED))

  with description("Structure requirement") as self:
    with before.each: # pylint: disable=no-member
      self.data = {
        "type": "structure",
        "structure": "BARRACKS"
      }

    with it("resolves to 'a single barracks required'"):
      requirement = BuildCommandRequirement(self.data)
      expect(requirement).to(be_a(BuildCommandRequirement))
      expect(requirement.type_id).to(equal(RequirementType.STRUCTURE))
      expect(requirement.unit_type_id).to(equal(UnitTypeId.BARRACKS))
      expect(requirement.unit_amount).to(equal(1))

    with it("can resolve to 'multiple factories required'"):
      data = deepcopy(self.data)
      data["amount"] = 3
      data["structure"] = UnitTypeId.FACTORY

      requirement = BuildCommandRequirement(data)
      expect(requirement).to(be_a(BuildCommandRequirement))
      expect(requirement.type_id).to(equal(RequirementType.STRUCTURE))
      expect(requirement.unit_type_id).to(equal(UnitTypeId.FACTORY))
      expect(requirement.unit_amount).to(equal(3))

  with description("Designated requirement") as self:
    with before.each: # pylint: disable=no-member
      self.data = {
        "type": "designation",
        "designation": ["barracks_1", "factory_1"]
      }

    with it("is a correct type of requirement"):
      requirement = BuildCommandRequirement(self.data)
      expect(requirement).to(be_a(BuildCommandRequirement))
      expect(requirement.type_id).to(equal(RequirementType.DESIGNATED))
      expect(requirement.designations).to(contain("barracks_1"))
      expect(requirement.designations).to(contain("factory_1"))