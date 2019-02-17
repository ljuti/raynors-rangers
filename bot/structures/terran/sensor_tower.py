from bot.structures.terran.base_structure import BaseStructure
from bot.structures.models.terran.sensor_tower import SensorTowerModel

from sc2.unit import Unit

class SensorTower(BaseStructure):
  def __init__(self, unit: Unit, model: SensorTowerModel, service_hub):
    super(SensorTower, self).__init__(unit, service_hub)
    self.model = model