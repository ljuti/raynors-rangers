from sc2.constants import UnitTypeId, AbilityId

class Reactorable():
  def __init__(self, unit):
    self.unit = unit

  def build_reactor(self, game):
    if game.can_afford(self.reactor_type(self.unit.type_id)) and self.has_no_addon():
      self.production_ready = False
      game.command_bus.queue(self.unit.build(self.reactor_type(self.unit.type_id)), False)

  def reactor_type(self, type_id: UnitTypeId) -> UnitTypeId:
    if type_id == UnitTypeId.BARRACKS:
      return UnitTypeId.BARRACKSREACTOR
    elif type_id == UnitTypeId.FACTORY:
      return UnitTypeId.FACTORYREACTOR
    elif type_id == UnitTypeId.STARPORT:
      return UnitTypeId.STARPORTREACTOR

  def has_reactor(self, game) -> bool:
    return bool(
      self.unit.add_on_tag != 0
      and game.units.find_by_tag(self.unit.add_on_tag).type_id in [UnitTypeId.BARRACKSREACTOR, UnitTypeId.FACTORYREACTOR, UnitTypeId.STARPORTREACTOR]
    )