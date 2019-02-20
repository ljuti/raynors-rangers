from bot.command_bus import CommandBus
from bot.registries.unit_registry import UnitRegistry
from bot.registries.structure_registry import StructureRegistry

from bot.stores.location_data import LocationData

class ServiceHub():
  def __init__(self, game):
    self.game = game
    self.command_bus = None
    self.unit_registry = None
    self.structure_registry = None
    self.location_data = None

  def register(self, service):
    if isinstance(service, CommandBus):
      self.command_bus = service
      return True
    if isinstance(service, UnitRegistry):
      self.unit_registry = service
      return True
    if isinstance(service, StructureRegistry):
      self.structure_registry = service
      return True
    if isinstance(service, LocationData):
      self.location_data = service
      return True

  def provide(self, service):
    pass

  def get(self, service):
    if service is CommandBus:
      return self.command_bus
    elif service is UnitRegistry:
      return self.unit_registry
    elif service is StructureRegistry:
      return self.structure_registry
    elif service is LocationData:
      return self.location_data