from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.enums import BTreeCategory

class Action(BaseNode):
  category = BTreeCategory.ACTION

  def __init__(self):
    super(Action, self).__init__()