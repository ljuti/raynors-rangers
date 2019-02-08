class LiberatorModel():
  def __init__(self):
    self.supply = 3
    self.cargo_size = 0
    self.loadable = False
    self.health = 180
    self.sieged = False
    self.range_unsieged = 5
    self.range_sieged = 10
    self.range_sieged_upgraded = 14
    self.advanced_ballistics = False
    self.sight_unsieged = 10
    self.sight_sieged = 13
    self.sight_sieged_upgraded = 17
    self.speed = 4.72

    self.ground_attack = False
    self.aerial_attack = True