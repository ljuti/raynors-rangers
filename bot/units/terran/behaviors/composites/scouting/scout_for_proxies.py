from bot.btrees.core.condition import Condition
from bot.btrees.composites.mem_sequence import MemSequence
from bot.btrees.decorators.inverter import Inverter
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus
from bot.btrees.decorators.inverter import Inverter

from bot.units.terran.behaviors.actions.scouting.get_scouting_location import GetScoutingLocation
from bot.units.terran.behaviors.actions.scouting.move_to_location import MoveToLocation

from sc2.position import Point2

class ScoutingLocationsRemaining(Condition):
  def __init__(self):
    super(ScoutingLocationsRemaining, self).__init__()

  def tick(self, tick: Tick):
    locations = tick.blackboard.get('scouting_locations', tick.tree.id)
    if locations and len(locations) > 0:
      return BTreeStatus.SUCCESS
    return BTreeStatus.FAILURE

class ScoutForProxies(MemSequence):
  def __init__(self, location_data_store, children=None):
    super(ScoutForProxies, self).__init__(children)

    if children is None:
      self.children = [
        GetScoutingLocation(),
        MoveToLocation(),
        ScoutingLocationsRemaining()
      ]

    self.locations = location_data_store

  def enter(self, tick: Tick):
    tick.blackboard.set('scouting_locations', self.locations.potential_proxy_locations, tick.tree.id)