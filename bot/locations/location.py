from sc2.position import Point2, Point3

class Position():
  def __init__(self, coordinates):
    self.coordinates = coordinates

  @property
  def coordinates_resolved(self) -> bool:
    return bool(
      isinstance(self.coordinates, ( Point2, Point3 ))
    )

  @property
  def position_x(self):
    if self.coordinates and isinstance(self.coordinates, ( Point2, Point3 )):
      return self.coordinates.x
    return None

  @property
  def position_y(self):
    if self.coordinates and isinstance(self.coordinates, ( Point2, Point3 )):
      return self.coordinates.y
    return None

class NextToStructurePosition(Position):
  def __init__(self, designation=None):
    super().__init__(None)
    self.designation = designation
    self.position_type = "next_to"

class BaseLocationPosition(Position):
  def __init__(self, designation=None):
    super().__init__(None)
    self.designation = designation
    self.position_type = "base"

class NamedPosition(Position):
  def __init__(self, designation=None):
    super().__init__(None)
    self.designation = designation
    self.position_type = "name"

class OnStructurePosition(Position):
  def __init__(self, designation=None):
    super().__init__(None)
    self.designation = designation
    self.position_type = "structure"

class StructurePosition(Position):
  def __init__(self, coordinates, structure=None):
    super().__init__(coordinates)
    self.structure = structure

  def __repr__(self):
    return f"StructurePosition(x: {self.position_x}, y: {self.position_y})"

class Location():
  def __init__(self):
    self.center_position = None

  @property
  def center(self) -> Point2:
    return self.center_position