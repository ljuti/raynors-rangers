from bot.commands.command import Command
from bot.locations.location import StructurePosition

from sc2.constants import UnitTypeId
from sc2.position import Point2

class BuildCommand(Command):
  def __init__(self):
    super().__init__()

    self.structure = self.position = self.game_conditions = None
    self.requirements = []

  def init(self, data: dict):
    self.structure = data.get('structure', None)
    self.position = data.get('position', None)
    self.requirements = data.get('requirements', [])

  @property
  def is_valid(self) -> bool:
    return bool(
      self.structure_is_valid
      and self.position_is_valid
    )

  @property
  def is_executable(self) -> bool:
    return bool(
      self.is_valid
      and self.requirements_met
      and self.game_conditions_met
    )

  @property
  def requirements_met(self) -> bool:
    return bool(True)

  @property
  def game_conditions_met(self) -> bool:
    return bool(True)

  @property
  def structure_is_valid(self) -> bool:
    return bool(
      isinstance(self.structure, UnitTypeId)
      and self.valid_structure_type(self.structure)
    )

  @property
  def position_is_valid(self) -> bool:
    return bool(
      isinstance(self.position, ( StructurePosition, Point2 ))
    )

  def valid_structure_type(self, type_id) -> bool:
    return bool(
      type_id in [
        UnitTypeId.ARMORY,
        UnitTypeId.BARRACKS,
        UnitTypeId.BUNKER,
        UnitTypeId.COMMANDCENTER,
        UnitTypeId.ENGINEERINGBAY,
        UnitTypeId.FACTORY,
        UnitTypeId.FUSIONCORE,
        UnitTypeId.GHOSTACADEMY,
        UnitTypeId.MISSILETURRET,
        UnitTypeId.REFINERY,
        UnitTypeId.SENSORTOWER,
        UnitTypeId.STARPORT,
        UnitTypeId.SUPPLYDEPOT,
        UnitTypeId.BARRACKSREACTOR,
        UnitTypeId.BARRACKSTECHLAB,
        UnitTypeId.FACTORYREACTOR,
        UnitTypeId.FACTORYTECHLAB,
        UnitTypeId.STARPORTREACTOR,
        UnitTypeId.STARPORTTECHLAB,
      ]
    )