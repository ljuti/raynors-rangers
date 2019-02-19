from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.composites.priority import Priority

from bot.units.terran.behaviors.composites.scouting.scout_natural_expansion import ScoutNaturalExpansion

from bot.service_hub import ServiceHub
from bot.stores.location_data import LocationData

class SCVScoutingTree(BehaviorTree):
  def __init__(self, service_hub: ServiceHub):
    super(SCVScoutingTree, self).__init__()
    self.services = service_hub
    self.root = self.build_tree()

  def build_tree(self):
    return Priority(children=[
      ScoutNaturalExpansion(self.services.get(LocationData)),
      ScoutForProxies(),
      ScoutEnemyMainBase(),
      ScoutEnemyExpansions()
    ])