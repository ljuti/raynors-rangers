from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class MoveToLocation(Action):
  def __init__(self):
    super(MoveToLocation, self).__init__()

  def tick(self, tick: Tick):
    actor = tick.target
    location = tick.blackboard.get('currently_scouting', tick.tree.id)
    distance = actor.unit.position.distance_to(location)

    if self.ordered_to_move_to(actor, location):
      if distance > 5:
        return BTreeStatus.RUNNING
      elif distance <= 3:
        tick.blackboard.set('currently_scouting', None, tick.tree.id)
        return BTreeStatus.SUCCESS
    elif distance > 5:
      status = actor.move_to(location)
      if status:
        return BTreeStatus.RUNNING
    elif distance <= 3:
      tick.blackboard.set('currently_scouting', None, tick.tree.id)
      return BTreeStatus.SUCCESS

    return BTreeStatus.FAILURE

  def ordered_to_move_to(self, actor, position) -> bool:
    return (
      actor.unit.orders
      and actor.unit.order_target == position
    )