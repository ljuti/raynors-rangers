from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class Failure(Action):
  def tick(self, tick: Tick):
    return BTreeStatus.FAILURE