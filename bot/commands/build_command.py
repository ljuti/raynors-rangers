from bot.commands.command import Command
from bot.locations.location import StructurePosition, NamedPosition, OnStructurePosition, BaseLocationPosition, NextToStructurePosition
from bot.commands.requirements.build_command import BuildCommandRequirement
from bot.commands.conditions.build_command import BuildCommandGameCondition

from sc2.constants import UnitTypeId
from sc2.position import Point2, Point3

class BuildCommand(Command):
  def __init__(self):
    super().__init__()

    self.structure = self.position = self.game_conditions = self.meta = self.assigned_to = None
    self.under_execution = self.completed = False
    self.requirements = []
    self.game_conditions = []

  def __repr__(self):
    return f"BuildCommand([{self.command_id}] for {self.structure} @ {self.position}, completed: {self.completed})"

  def init(self, data: dict):
    self.structure = data.get('structure', None)
    self.resolve_position(data.get('position', None))
    self.resolve_requirements(data.get('requirements', []))
    self.resolve_game_conditions(data.get('conditions', []))

  def resolve_position(self, position):
    if isinstance(position, StructurePosition):
      self.position = position
    elif isinstance(position, ( Point2, Point3 )):
      self.position = StructurePosition(position)
    elif isinstance(position, dict):
      self.resolve_position_data(position)

  def resolve_position_data(self, data):
    if "name" in data.keys():
      self.position = NamedPosition(data.get("name", None))
    elif "structure" in data.keys():
      self.position = OnStructurePosition(data.get("structure", None))
    elif "base" in data.keys():
      self.position = BaseLocationPosition(data.get("base", None))
    elif "next_to" in data.keys():
      self.position = NextToStructurePosition(data.get("next_to", None))

  def resolve_requirements(self, r_data):
    for data in r_data:
      requirement = BuildCommandRequirement(data)
      if isinstance(requirement, BuildCommandRequirement):
        self.requirements.append(requirement)

  def resolve_game_conditions(self, c_data):
    for key in c_data:
      condition = BuildCommandGameCondition(( key, c_data[key] ))
      if isinstance(condition, BuildCommandGameCondition):
        self.game_conditions.append(condition)

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