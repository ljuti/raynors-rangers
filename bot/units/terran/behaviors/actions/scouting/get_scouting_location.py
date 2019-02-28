from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from sc2.position import Point2

class GetScoutingLocation(Action):
  def __init__(self):
    super(GetScoutingLocation, self).__init__()

  def tick(self, tick: Tick):
    currently_scouting = tick.blackboard.get('currently_scouting', tick.tree.id)

    if currently_scouting and isinstance(currently_scouting, Point2):
      return BTreeStatus.SUCCESS

    locations = tick.blackboard.get('scouting_locations', tick.tree.id)

    if locations:
      location = locations.popleft()
      tick.blackboard.set('currently_scouting', location, tick.tree.id)
      return BTreeStatus.SUCCESS

    return BTreeStatus.FAILURE