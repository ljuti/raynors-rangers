import enum

from sc2.constants import UnitTypeId

class RequirementType(enum.Enum):
  STRUCTURE = 0
  DESIGNATED = 1
  UNKNOWN = 99

class BuildCommandRequirement():
  def __init__(self, data={}):
    self.data = data
    self.type_id = self.designations = self.unit_type_id = self.unit_amount = None
    self.parse_data()

  def parse_data(self):
    self.type_id = self.resolve_requirement_type(self.data.get('type', None))

    if self.type_id == RequirementType.STRUCTURE:
      self.unit_type_id = self.resolve_unit_type_id(self.data.get('structure', None))
      self.unit_amount = self.data.get('amount', 1)
    if self.type_id == RequirementType.DESIGNATED:
      self.designations = self.data.get('designation', None)

  def resolve_unit_type_id(self, u_type):
    if isinstance(u_type, str):
      return UnitTypeId[u_type]
    elif isinstance(u_type, UnitTypeId):
      return u_type
    return None

  def resolve_requirement_type(self, r_type):
    if r_type == "structure":
      return RequirementType.STRUCTURE
    elif r_type == "designation":
      return RequirementType.DESIGNATED
    else:
      return RequirementType.UNKNOWN
