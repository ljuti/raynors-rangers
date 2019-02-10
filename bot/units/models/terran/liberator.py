from sc2.constants import UnitTypeId, AbilityId

class LiberatorModel():
  def __init__(self):
    self.supply = 3
    self.cargo_size = 0
    self.loadable = False
    self.health = 180
    self.range_unsieged = 5
    self._range_sieged = 10
    self._range_sieged_upgraded = 14
    self.advanced_ballistics = False

    self.sight_unsieged = 10
    self._sight_sieged = 13
    self._sight_sieged_upgraded = 17
    self.speed = 4.72

    self.ground_attack = False
    self.aerial_attack = True

    self.sieged_type_id = UnitTypeId.LIBERATORAG
    self.siege_ability = AbilityId.LIBERATORMORPHTOAG_LIBERATORAGMODE
    self.unsiege_ability = AbilityId.LIBERATORMORPHTOAA_LIBERATORAAMODE

  @property
  def range_sieged(self) -> int:
    if self.advanced_ballistics:
      return self._range_sieged_upgraded
    return self._range_sieged

  @property
  def sight_sieged(self) -> int:
    if self.advanced_ballistics:
      return self._sight_sieged_upgraded
    return self._sight_sieged