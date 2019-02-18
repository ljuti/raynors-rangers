from bot.commanders.commander import Commander

class BuildCommander(Commander):
  def __init__(self, service_hub=None):
    super().__init__()
    self.service_hub = service_hub

  def can_afford(self, structure):
    return True