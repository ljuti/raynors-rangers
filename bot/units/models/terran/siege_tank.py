from sc2.constants import UnitTypeId, AbilityId

class SiegeTankModel():
  def __init__(self):
    self.supply = 3
    self.cargo_size = 4
    self.health = 175
    self.range_sieged = 13
    self.range_unsieged = 7
    self.sight = 11
    self.speed = 3.15
    self.aoe_radius = 2.5

    self.ground_attack = True
    self.aerial_attack = False

    self.sieged_type_id = UnitTypeId.SIEGETANKSIEGED
    self.siege_ability = AbilityId.SIEGEMODE_SIEGEMODE
    self.unsiege_ability = AbilityId.UNSIEGE_UNSIEGE