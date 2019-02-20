from bot.structures.terran.base_structure import BaseStructure
from bot.structures.models.terran.supply_depot import SupplyDepotModel

from sc2.unit import Unit

class SupplyDepot(BaseStructure):
  def __init__(self, unit: Unit, model: SupplyDepotModel, service_hub=None):
    super(SupplyDepot, self).__init__(unit, service_hub)
    self.model = model
