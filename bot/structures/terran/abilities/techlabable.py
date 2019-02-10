from sc2.constants import UnitTypeId

class Techlabable:
  def __init__(self, unit):
    self.unit = unit

  def build_techlab(self, game):
    if game.can_afford(self.techlab_type(self.unit.type_id)) and self.has_no_addon():
      self.production_ready = False
      game.command_bus.queue(self.unit.build(self.techlab_type(self.unit.type_id)))

  def techlab_type(self, type_id: UnitTypeId) -> UnitTypeId:
    if type_id == UnitTypeId.BARRACKS:
      return UnitTypeId.BARRACKSTECHLAB
    elif type_id == UnitTypeId.FACTORY:
      return UnitTypeId.FACTORYTECHLAB
    elif type_id == UnitTypeId.STARPORT:
      return UnitTypeId.STARPORTTECHLAB

  def has_techlab(self, game) -> bool:
    return bool(
      self.unit.add_on_tag != 0
      and game.units.find_by_tag(self.unit.add_on_tag).type_id in [UnitTypeId.BARRACKSTECHLAB, UnitTypeId.FACTORYTECHLAB, UnitTypeId.STARPORTTECHLAB]
    )