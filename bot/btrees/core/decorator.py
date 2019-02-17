from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.enums import BTreeCategory

class Decorator(BaseNode):
  category = BTreeCategory.DECORATOR

  def __init__(self, child=None):
    super(Decorator, self).__init__()

    self.child = child or []