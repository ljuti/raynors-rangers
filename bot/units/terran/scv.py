class SCVUnit():
  def __init__(self, unit, model):
    self.unit = unit
    self.model = model

  def update(self, game, unit):
    if unit.is_constructing_scv():
      return