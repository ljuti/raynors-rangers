import uuid

from bot.btrees.core.enums import BTreeStatus
from bot.btrees.core.tick import Tick

class BaseNode(object):
  category = None
  title = None
  description = None

  def __init__(self):
    self.id = str(uuid.uuid4())
    self.title = self.title or self.__class__.__name__

  def _execute(self, tick: Tick):
    self._enter(tick)

    if (not tick.blackboard.get('is_open', tick.tree.id, self.id)):
      self._open(tick)

    status = self._tick(tick)

    if (status != BTreeStatus.RUNNING):
      self._close(tick)

    self._exit(tick)

    return status

  def _enter(self, tick: Tick):
    tick._enter_node(self)
    self.enter(tick)

  def _open(self, tick: Tick):
    tick._open_node(self)
    tick.blackboard.set('is_open', True, tick.tree.id, self.id)
    self.open(tick)

  def _tick(self, tick: Tick):
    tick._tick_node(self)
    return self.tick(tick)

  def _close(self, tick: Tick):
    tick._close_node(self)
    tick.blackboard.set('is_open', False, tick.tree.id, self.id)
    self.close(tick)

  def _exit(self, tick: Tick):
    tick._exit_node(self)
    self.exit(tick)

  def enter(self, tick: Tick):
    pass

  def exit(self, tick: Tick):
    pass

  def open(self, tick: Tick):
    pass

  def close(self, tick: Tick):
    pass

  def tick(self, tick: Tick):
    pass
