class UnitProperties:
  def __init__(self, model):
    self.model = model

  @property
  def supply(self) -> int:
    return self.model.supply

  @property
  def loadable(self) -> bool:
    return self.model.loadable

  @property
  def speed(self) -> float:
    return float(self.model.speed)

  @property
  def sight(self) -> int:
    return self.model.sight

  @property
  def range(self) -> float:
    return float(self.model.range)

  @property
  def can_attack_ground(self) -> bool:
    return bool(self.model.ground_attack)

  @property
  def can_attack_air(self) -> bool:
    return bool(self.model.aerial_attack)