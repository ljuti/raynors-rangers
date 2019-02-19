from bot.commanders.behaviors.actions.build_order.complete import BuildOrderComplete
from bot.commanders.behaviors.composites.build_order.get_active_phase import GetActivePhase

from bot.btrees.composites.priority import Priority
from bot.btrees.decorators.inverter import Inverter

from bot.data_store import DataStore
from bot.stores.build_order_data import BuildOrderData

class EvaluateActivePhase(Priority):
  def __init__(self, data_store: DataStore, children=None):
    super(EvaluateActivePhase, self).__init__(children)

    if children is None:
      self.children = [
        Inverter(child=BuildOrderComplete(data_store.get(BuildOrderData))),
        GetActivePhase()
      ]
