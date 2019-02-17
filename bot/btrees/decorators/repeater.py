from bot.btrees.core.decorator import Decorator
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class Repeater(Decorator):
  def __init__(self, child, max_loop=-1):
    super(Repeater, self).__init__(child)

    self.max_loop = max_loop

  def open(self, tick: Tick):
    tick.blackboard.set('loop', 0, tick.tree.id, self.id)

  def tick(self, tick: Tick):
    if not self.child:
      return BTreeStatus.ERROR
    
    loop_number = tick.blackboard.get('loop', tick.tree.id, self.id)
    status = BTreeStatus.SUCCESS

    while self.max_loop < 0 or loop_number < self.max_loop:
      status = self.child._execute(tick)

      if status in [BTreeStatus.SUCCESS, BTreeStatus.FAILURE]:
        loop_number += 1
      else:
        break

    tick.blackboard.set('loop', loop_number, tick.tree.id, self.id)
    return status