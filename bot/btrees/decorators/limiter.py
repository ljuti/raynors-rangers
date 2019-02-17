from bot.btrees.core.decorator import Decorator
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class Limiter(Decorator):
  def __init__(self, child, max_loop):
    super(Limiter, self).__init__(child)

    self.max_loop = max_loop

  def open(self, tick: Tick):
    tick.blackboard.set('attempt', 0, tick.tree.id, self.id)

  def tick(self, tick: Tick):
    if not self.child:
      return BTreeStatus.ERROR

    attempt = tick.blackboard.get('attempt', tick.tree.id, self.id)
    if attempt < self.max_loop:
      status = self.child._execute(tick)

      if status in [BTreeStatus.SUCCESS, BTreeStatus.FAILURE]:
        tick.blackboard.set('attempt', attempt+1, tick.tree.id, self.id)

      return status

    return BTreeStatus.FAILURE