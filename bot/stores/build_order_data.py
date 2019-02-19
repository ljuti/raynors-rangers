class BuildOrderData():
  def __init__(self):
    self.build_order_loaded = False
    self.loaded_phases_count = 0
    self.completed_phases_count = 0

  @property
  def build_order_complete(self):
    return bool(
      self.build_order_loaded
      and (self.completed_phases_count == self.loaded_phases_count)
    )