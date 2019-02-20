from sc2.position import Point2

class LocationData():
  def __init__(self, main=None):
    self.main = main
    self.natural = None

  def prepare_expansions(self, expansion_locations):
    start = self.main
    waypoints = [point for point in list(expansion_locations)]
    print(waypoints)
    waypoints.sort(key=lambda p: (p[0] - start[0]) ** 2 + (p[1] - start[1]) ** 2)
    self.ordered_expansions = [Point2((p[0], p[1])) for p in waypoints]
    self.natural = self.ordered_expansions[1]