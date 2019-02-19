from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class BuildOrderComplete(Action):
  def __init__(self, data_store=None):
    super(BuildOrderComplete, self).__init__()

    self.data_store = data_store

  def tick(self, tick: Tick):
    if self.data_store.build_order_complete:
      return BTreeStatus.SUCCESS
    return BTreeStatus.FAILURE