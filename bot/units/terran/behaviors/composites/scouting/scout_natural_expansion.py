from bot.btrees.core.condition import Condition
from bot.btrees.composites.sequence import Sequence
from bot.btrees.decorators.inverter import Inverter
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from bot.units.terran.behaviors.actions.scouting.move_to_natural_expansion import MoveToNaturalExpansion

from sc2.position import Point2

class NaturalExpansionScouted(Condition):
  def __init__(self):
    super(NaturalExpansionScouted, self).__init__()

  def tick(self, tick: Tick):
    scouted = tick.blackboard.get('natural_scouted', tick.tree.id)
    if scouted:
      return BTreeStatus.SUCCESS
    return BTreeStatus.FAILURE

class ScoutNaturalExpansion(Sequence):
  def __init__(self, location_data_store, children=None):
    super(ScoutNaturalExpansion, self).__init__(children)

    if children is None:
      self.children = [
        Inverter(child=NaturalExpansionScouted()),
        MoveToNaturalExpansion()
      ]

    self.locations = location_data_store

  def enter(self, tick: Tick):
    tick.blackboard.set('natural_position', self.locations.natural, tick.tree.id)