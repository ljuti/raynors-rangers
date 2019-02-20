from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class MoveToNaturalExpansion(Action):
  def __init__(self):
    super(MoveToNaturalExpansion, self).__init__()

  def tick(self, tick: Tick):
    actor = tick.target
    natural_expansion = tick.blackboard.get('natural_position', tick.tree.id)
    distance = actor.unit.position.distance_to(natural_expansion)

    if self.ordered_to_move_to_natural(actor, natural_expansion):
      if distance > 5:
        return BTreeStatus.RUNNING
      elif distance <= 5:
        print("Natural scouted")
        return BTreeStatus.SUCCESS
    elif distance > 5:
      status = actor.move_to(natural_expansion)
      if status:
        return BTreeStatus.RUNNING
    elif distance < 5:
      print("Natural scouted")
      return BTreeStatus.SUCCESS

    return BTreeStatus.FAILURE

  def ordered_to_move_to_natural(self, actor, position) -> bool:
    return (
      actor.unit.orders
      and actor.unit.order_target == position
    )