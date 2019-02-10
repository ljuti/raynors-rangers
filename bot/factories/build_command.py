from bot.factories.command_factory import CommandFactory
from bot.commands.build_command import BuildCommand
from bot.locations.location import StructurePosition

from sc2.constants import UnitTypeId
from sc2.position import Point2

class BuildCommandFactory(CommandFactory):
  def __init__(self):
    super().__init__()

  def create(self):
    command = BuildCommand()
    command.init(
      {
        "structure": UnitTypeId.SUPPLYDEPOT,
        "position": StructurePosition(Point2((50.0, 50.0)))
      }
    )
    return command