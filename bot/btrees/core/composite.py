from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.enums import BTreeCategory

class Composite(BaseNode):
  category = BTreeCategory.COMPOSITE

  def __init__(self, children=None):
    super(Composite, self).__init__()

    self.children = children or []