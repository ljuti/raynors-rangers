from sc2.position import Point2

class Position():
  def __init__(self, coordinates):
    self.coordinates = coordinates

class StructurePosition(Position):
  def __init__(self, coordinates, structure=None):
    super().__init__(coordinates)
    self.structure = structure

class Location():
  def __init__(self):
    self.center_position = None

  @property
  def center(self) -> Point2:
    return self.center_position