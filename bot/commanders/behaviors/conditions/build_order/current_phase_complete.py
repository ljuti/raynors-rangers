from bot.btrees.core.condition import Condition
from bot.btrees.core.tick import Tick

class CurrentPhaseComplete(Condition):
  def __init__(self):
    super(CurrentPhaseComplete, self).__init__()

  def tick(self, tick: Tick):
    current_phase = tick.blackboard.get('current_phase', tick.tree.id)
    