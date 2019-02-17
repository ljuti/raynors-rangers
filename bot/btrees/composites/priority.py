from bot.btrees.core.composite import Composite
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class Priority(Composite):
  def __init__(self, children=None):
    super(Priority, self).__init__(children)

  def tick(self, tick: Tick):
    for node in self.children:
      status = node._execute(tick)

      if status != BTreeStatus.FAILURE:
        return status

    return BTreeStatus.FAILURE