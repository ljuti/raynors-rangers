from bot.btrees.core.decorator import Decorator
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

class Inverter(Decorator):
  def tick(self, tick: Tick):
    if not self.child:
      return BTreeStatus.ERROR

    status = self.child._execute(tick)

    if status == BTreeStatus.SUCCESS:
      return BTreeStatus.FAILURE
    elif status == BTreeStatus.FAILURE:
      return BTreeStatus.SUCCESS

    return status