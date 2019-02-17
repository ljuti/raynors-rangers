from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.enums import BTreeCategory

class Condition(BaseNode):
  category = BTreeCategory.CONDITION

  def __init__(self):
    super(Condition, self).__init__()