from bot.btrees.core.decorator import Decorator
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

import time

class MaxTime(Decorator):
  def __init__(self, child, max_time=0):
    super(MaxTime, self).__init__(child)

    self.max_time = max_time

  def open(self, tick: Tick):
    tick.blackboard.set('start_time', time.time(), tick.tree.id, self.id)

  def tick(self, tick: Tick):
    if not self.child:
      return BTreeStatus.ERROR

    current_time = time.time()
    start_time = tick.blackboard.get('start_time', tick.tree.id, self.id)

    status = self.child._execute(tick)

    if (current_time - start_time > self.max_time):
      return BTreeStatus.FAILURE

    return status