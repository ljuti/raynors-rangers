# -*- coding: utf-8 -*-
""" Unit Registry

Unit registry keeps track of all units that the AI has at any given moment.

Units can be queried by a tag or by type of units.
"""

from bot.registries.base_registry import BaseRegistry

from bot.units.terran.base_unit import BaseUnit
from bot.units.terran.banshee import BansheeUnit
from bot.units.terran.battlecruiser import BattlecruiserUnit
from bot.units.terran.cyclone import CycloneUnit
from bot.units.terran.ghost import GhostUnit
from bot.units.terran.hellion import HellionUnit
from bot.units.terran.liberator import LiberatorUnit
from bot.units.terran.marauder import MarauderUnit
from bot.units.terran.marine import MarineUnit
from bot.units.terran.medivac import MedivacUnit
from bot.units.terran.raven import RavenUnit
from bot.units.terran.reaper import ReaperUnit
from bot.units.terran.scv import SCVUnit
from bot.units.terran.siege_tank import SiegeTankUnit
from bot.units.terran.thor import ThorUnit
from bot.units.terran.viking import VikingUnit
from bot.units.terran.widow_mine import WidowMineUnit

from bot.units.models.terran.banshee import BansheeModel
from bot.units.models.terran.battlecruiser import BattlecruiserModel
from bot.units.models.terran.cyclone import CycloneModel
from bot.units.models.terran.ghost import GhostModel
from bot.units.models.terran.hellion import HellionModel
from bot.units.models.terran.liberator import LiberatorModel
from bot.units.models.terran.marauder import MarauderModel
from bot.units.models.terran.marine import MarineModel
from bot.units.models.terran.medivac import MedivacModel
from bot.units.models.terran.raven import RavenModel
from bot.units.models.terran.reaper import ReaperModel
from bot.units.models.terran.scv import SCVModel
from bot.units.models.terran.siege_tank import SiegeTankModel
from bot.units.models.terran.thor import ThorModel
from bot.units.models.terran.viking import VikingModel
from bot.units.models.terran.widow_mine import WidowMineModel

from sc2.unit import Unit
from sc2.constants import UnitTypeId

class UnitRegistry(BaseRegistry):
  def __init__(self, game, service_hub=None):
    super().__init__()
    self.game = game
    self.services = service_hub
    self.load_models_and_klasses()

  def get_with_tags(self, tags: list) -> list:
    return list(
      self.get_with_tag(tag) for tag in tags if tag in self.objects.keys()
    )

  def make_decisions(self, game):
    self.game = game

    for unit in self.game.units():
      unit_obj = self.get_with_tag(unit.tag)
      if unit_obj:
        unit_obj.update(self.game, unit)

  def get_with_unit_type(self, unit_type) -> list:
    keys = [k for k in self.objects.keys() if self.objects[k].get("type", None) == unit_type]
    if keys:
      return list(self.get_with_tag(k) for k in keys)
    return []

  def add(self, unit: Unit, designation=None):
    if self.get_with_tag(unit.tag):
      return

    unit = self.initialize_unit(unit)

    self.objects.update(
      { unit.tag: { "unit": unit, "type": unit.type_id }}
    )

    if designation:
      self.objects.update(
        { unit.tag: { "unit": unit, "type": unit.type_id, "designation": designation }}
      )

    return True

  def complete(self, unit: Unit):
    pass

  def model_for(self, type_id: UnitTypeId):
    return self.models.get(type_id)

  def klass_for(self, type_id: UnitTypeId):
    return self.klasses.get(type_id)

  def initialize_unit(self, unit) -> BaseUnit:
    model = self.model_for(unit.type_id)
    klass = self.klass_for(unit.type_id)
    return klass(unit, model, self.services)

  def marines(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.MARINE))

  def banshees(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.BANSHEE))

  def battlecruisers(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.BATTLECRUISER))

  def cyclones(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.CYCLONE))

  def ghosts(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.GHOST))

  def hellions(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.HELLION))

  def liberators(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.LIBERATOR))

  def marauders(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.MARAUDER))

  def medivacs(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.MEDIVAC))

  def ravens(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.RAVEN))

  def reapers(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.REAPER))

  def scvs(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.SCV))

  def siege_tanks(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.SIEGETANK))

  def thors(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.THOR))

  def vikings(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.VIKING))

  def widow_mines(self) -> list:
    return list(self.get_with_unit_type(UnitTypeId.WIDOWMINE))

  def load_models_and_klasses(self):
    self.models = {
      UnitTypeId.BANSHEE: BansheeModel(),
      UnitTypeId.BATTLECRUISER: BattlecruiserModel(),
      UnitTypeId.CYCLONE: CycloneModel(),
      UnitTypeId.GHOST: GhostModel(),
      UnitTypeId.HELLION: HellionModel(),
      UnitTypeId.LIBERATOR: LiberatorModel(),
      UnitTypeId.MARAUDER: MarauderModel(),
      UnitTypeId.MARINE: MarineModel(),
      UnitTypeId.MEDIVAC: MedivacModel,
      UnitTypeId.RAVEN: RavenModel(),
      UnitTypeId.REAPER: ReaperModel(),
      UnitTypeId.SCV: SCVModel(),
      UnitTypeId.SIEGETANK: SiegeTankModel(),
      UnitTypeId.THOR: ThorModel(),
      UnitTypeId.VIKING: VikingModel(),
      UnitTypeId.WIDOWMINE: WidowMineModel()
    }

    self.klasses = {
      UnitTypeId.BANSHEE: BansheeUnit,
      UnitTypeId.BATTLECRUISER: BattlecruiserUnit,
      UnitTypeId.CYCLONE: CycloneUnit,
      UnitTypeId.GHOST: GhostUnit,
      UnitTypeId.HELLION: HellionUnit,
      UnitTypeId.LIBERATOR: LiberatorUnit,
      UnitTypeId.MARAUDER: MarauderUnit,
      UnitTypeId.MARINE: MarineUnit,
      UnitTypeId.MEDIVAC: MedivacUnit,
      UnitTypeId.RAVEN: RavenUnit,
      UnitTypeId.REAPER: ReaperUnit,
      UnitTypeId.SCV: SCVUnit,
      UnitTypeId.SIEGETANK: SiegeTankUnit,
      UnitTypeId.THOR: ThorUnit,
      UnitTypeId.VIKING: VikingUnit,
      UnitTypeId.WIDOWMINE: WidowMineUnit
    }
