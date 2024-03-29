# -*- coding: utf-8 -*-
""" Structure Registry

Structure registry keeps track of all buildings that the AI has at any
given moment. When the construction of a new building begins, it is
registered to the registry. When the construction completes, its position
and possible designation are recorded to the structure object.
"""

from bot.registries.base_registry import BaseRegistry

from bot.structures.models.terran.armory import ArmoryModel
from bot.structures.models.terran.barracks import BarracksModel
from bot.structures.models.terran.bunker import BunkerModel
from bot.structures.models.terran.command_center import CommandCenterModel
from bot.structures.models.terran.engineering_bay import EngineeringBayModel
from bot.structures.models.terran.factory import FactoryModel
from bot.structures.models.terran.fusion_core import FusionCoreModel
from bot.structures.models.terran.ghost_academy import GhostAcademyModel
from bot.structures.models.terran.missile_turret import MissileTurretModel
from bot.structures.models.terran.reactor import ReactorModel
from bot.structures.models.terran.refinery import RefineryModel
from bot.structures.models.terran.sensor_tower import SensorTowerModel
from bot.structures.models.terran.starport import StarportModel
from bot.structures.models.terran.supply_depot import SupplyDepotModel
from bot.structures.models.terran.techlab import TechlabModel

from bot.structures.terran.armory import Armory
from bot.structures.terran.barracks import Barracks
from bot.structures.terran.bunker import Bunker
from bot.structures.terran.command_center import CommandCenter
from bot.structures.terran.engineering_bay import EngineeringBay
from bot.structures.terran.factory import Factory
from bot.structures.terran.fusion_core import FusionCore
from bot.structures.terran.ghost_academy import GhostAcademy
from bot.structures.terran.missile_turret import MissileTurret
from bot.structures.terran.reactor import Reactor
from bot.structures.terran.refinery import Refinery
from bot.structures.terran.sensor_tower import SensorTower
from bot.structures.terran.starport import Starport
from bot.structures.terran.supply_depot import SupplyDepot
from bot.structures.terran.techlab import Techlab

from collections import defaultdict

from sc2.unit import Unit
from sc2.constants import UnitTypeId
from sc2.position import Point2

class StructureRegistry(BaseRegistry):
  def __init__(self, service_hub=None):
    super().__init__()
    self.registrations = defaultdict(dict)
    self.load_models_and_klasses()
    self.service_hub = service_hub

  def add(self, unit, designation=None):
    # if self.get_with_tag(unit.tag):
    #   return

    structure = self.initialize_structure(unit)

    position = self.resolve_position_for(unit)

    self.objects.update(
      { unit.tag: { "unit": structure, "position": position, "type": unit.type_id }}
    )

    if designation:
      self.objects.update(
        { unit.tag: { "unit": structure, "designation": designation, "position": position, "type": unit.type_id }}
      )

    return True

  def complete(self, unit: Unit):
    """ Not yet properly implemented """
    pass

  def resolve_position_for(self, unit):
    """ Resolves proper position for the structure
    
    Supply depots report 'incorrect' or 'funny' positions and to be able
    to query them later, we need to fix the position offset.
    """
    if unit.type_id == UnitTypeId.SUPPLYDEPOT:
      return unit.position.offset(Point2((-0.5, -0.5)))
    else:
      return unit.position

  def initialize_structure(self, unit):
    model = self.model_for(unit.type_id)
    klass = self.klass_for(unit.type_id)
    return klass(unit, model, self.service_hub)

  def model_for(self, type_id):
    return self.models[type_id]

  def klass_for(self, type_id):
    return self.klasses[type_id]

  def load_models_and_klasses(self):
    self.models = {
      UnitTypeId.ARMORY: ArmoryModel(),
      UnitTypeId.BARRACKS: BarracksModel(),
      UnitTypeId.BUNKER: BunkerModel(),
      UnitTypeId.COMMANDCENTER: CommandCenterModel(),
      UnitTypeId.ENGINEERINGBAY: EngineeringBayModel(),
      UnitTypeId.FACTORY: FactoryModel(),
      UnitTypeId.FUSIONCORE: FusionCoreModel(),
      UnitTypeId.GHOSTACADEMY: GhostAcademyModel(),
      UnitTypeId.MISSILETURRET: MissileTurretModel,
      UnitTypeId.REACTOR: ReactorModel(),
      UnitTypeId.BARRACKSREACTOR: ReactorModel(),
      UnitTypeId.FACTORYREACTOR: ReactorModel(),
      UnitTypeId.STARPORTREACTOR: ReactorModel(),
      UnitTypeId.REFINERY: RefineryModel(),
      UnitTypeId.SENSORTOWER: SensorTowerModel(),
      UnitTypeId.STARPORT: StarportModel(),
      UnitTypeId.SUPPLYDEPOT: SupplyDepotModel(),
      UnitTypeId.TECHLAB: TechlabModel(),
      UnitTypeId.BARRACKSTECHLAB: TechlabModel(),
      UnitTypeId.FACTORYTECHLAB: TechlabModel(),
      UnitTypeId.STARPORTTECHLAB: TechlabModel()
    }

    self.klasses = {
      UnitTypeId.ARMORY: Armory,
      UnitTypeId.BARRACKS: Barracks,
      UnitTypeId.BUNKER: Bunker,
      UnitTypeId.COMMANDCENTER: CommandCenter,
      UnitTypeId.ENGINEERINGBAY: EngineeringBay,
      UnitTypeId.FACTORY: Factory,
      UnitTypeId.FUSIONCORE: FusionCore,
      UnitTypeId.GHOSTACADEMY: GhostAcademy,
      UnitTypeId.MISSILETURRET: MissileTurret,
      UnitTypeId.REACTOR: Reactor,
      UnitTypeId.BARRACKSREACTOR: Reactor,
      UnitTypeId.FACTORYREACTOR: Reactor,
      UnitTypeId.STARPORTREACTOR: Reactor,
      UnitTypeId.REFINERY: Refinery,
      UnitTypeId.SENSORTOWER: SensorTower,
      UnitTypeId.STARPORT: Starport,
      UnitTypeId.SUPPLYDEPOT: SupplyDepot,
      UnitTypeId.TECHLAB: Techlab,
      UnitTypeId.BARRACKSTECHLAB: Techlab,
      UnitTypeId.FACTORYTECHLAB: Techlab,
      UnitTypeId.STARPORTTECHLAB: Techlab
    }

  def get_objects_with_unit_type(self, unit_type):
    """ Returns structure objects for given unit type
    
    For example, calling with UnitTypeId.STARPORT returns all starports.
    """
    keys = [k for k in self.objects.keys() if self.objects[k].get("type", None) == unit_type]
    if keys:
      return [self.get_with_tag(k) for k in keys]
    return None

  def barracks(self) -> list([Barracks]):
    return self.get_objects_with_unit_type(UnitTypeId.BARRACKS)

  def production_barracks(self) -> list([Barracks]):
    structures = self.barracks()
    if structures:
      return list(filter(lambda x: x.production_ready == True, structures))
    return []

  def production_barracks_with_techlab(self) -> list([Barracks]):
    structures = self.production_barracks()
    if structures:
      return list(filter(lambda x: x.has_techlab(self) == True, structures))
    return []

  def production_barracks_with_reactor(self) -> list([Barracks]):
    structures = self.production_barracks()
    if structures:
      return list(filter(lambda x: x.has_reactor(self) == True, structures))
    return []