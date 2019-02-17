from bot.btrees.core.composite import Composite
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class MemPriority(Composite):
  def __init__(self, children=None):
    super(MemPriority, self).__init__(children)

  def open(self, tick: Tick):
    tick.blackboard.set('running_child', 0, tick.tree.id, self.id)

  def tick(self, tick: Tick):
    idx = tick.blackboard.get('running_child', tick.tree.id, self.id)

    for val in range(idx, len(self.children)):
      node = self.children[val]
      status = node._execute(tick)

      if status != BTreeStatus.FAILURE:
        if status == BTreeStatus.RUNNING:
          tick.blackboard.set('running_child', val, tick.tree.id, self.id)
        return status

    return BTreeStatus.FAILURE