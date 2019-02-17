from bot.btrees.core.action import Action
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

import time

class Wait(Action):
  def __init__(self, milliseconds=0):
    super(Wait, self).__init__()
    self.end_time = milliseconds/1000.

  def open(self, tick: Tick):
    start_time = time.time()
    tick.blackboard.set('start_time', start_time, tick.tree.id, self.id)

  def tick(self, tick: Tick):
    current_time = time.time()
    start_time = tick.blackboard.get('start_time', tick.tree.id, self.id)

    if (current_time - start_time > self.end_time):
      return BTreeStatus.SUCCESS

    return BTreeStatus.RUNNING