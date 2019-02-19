from bot.commanders.behaviors.composites.build_order.evaluate_active_phase import EvaluateActivePhase

from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.composites.priority import Priority
from bot.btrees.composites.mem_priority import MemPriority
from bot.btrees.decorators.inverter import Inverter
from bot.commanders.behaviors.actions.build_order.complete import BuildOrderCompleteAction

from bot.data_store import DataStore
from bot.stores.build_order_data import BuildOrderData

class BuildOrderExecutionTree(BehaviorTree):
  def __init__(self, data_store: DataStore):
    super(BuildOrderExecutionTree, self).__init__()
    self.data_store = data_store
    self.root = self.build_tree()

  def build_tree(self):
    return Priority(children=[
      EvaluateActivePhase(self.data_store, children=[

      ]),
    ])