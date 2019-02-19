from bot.commanders.behaviors.conditions.build_order.current_phase_complete import CurrentPhaseComplete
from bot.commanders.behaviors.composites.build_order.load_next_phase import LoadNextPhase

from bot.btrees.composites.sequence import Sequence
from bot.btrees.decorators.inverter import Inverter

from bot.data_store import DataStore
from bot.stores.build_order_data import BuildOrderData

class GetActivePhase(Sequence):
  def __init__(self, children=None):
    super(GetActivePhase, self).__init__(children)

    if children is None:
      self.children = [
        CurrentPhaseComplete(),
        LoadNextPhase()
      ]