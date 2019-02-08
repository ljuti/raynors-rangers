class SCVUnit():
  def __init__(self, model):
    self.model = model

  def update(self, game, unit):
    if unit.is_constructing_scv():
      return