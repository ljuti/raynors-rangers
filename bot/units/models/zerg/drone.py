class DroneModel():
  def __init__(self):
    self.supply = 1
    self.cargo_size = 1
    self.health = 40
    self.range = 0.1
    self.sight = 8
    self.speed = 3.94

    self.ground_attack = True
    self.aerial_attack = False