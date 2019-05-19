# -*- coding: utf-8 -*-
""" Location Data Store

Location Data Store keeps track of interesting Location objects and points
in the game map.
"""

from collections import deque
from sc2.position import Point2

class LocationData():
  def __init__(self, main=None):
    self.main = main
    self.natural = None
    self.map_center = None
    self.ordered_expansions = None
    
  def prepare_expansions(self, expansion_locations):
    start = self.main
    waypoints = [point for point in list(expansion_locations)]
    print(waypoints)
    waypoints.sort(key=lambda p: (p[0] - start[0]) ** 2 + (p[1] - start[1]) ** 2)
    self.ordered_expansions = [Point2((p[0], p[1])) for p in waypoints]
    self.natural = self.ordered_expansions[1]

  def prepare_proxy_locations(self):
    self.potential_proxy_locations = deque([])
    self.potential_proxy_locations.append(self.ordered_expansions[2])
    self.potential_proxy_locations.append(self.ordered_expansions[3])
    self.potential_proxy_locations.append(self.map_center)