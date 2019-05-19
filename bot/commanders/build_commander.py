# -*- coding: utf-8 -*-
""" Build Commander

This is the high-level commander class for building structures in game.
A good candidate for implementing build order execution.
"""

from bot.commanders.commander import Commander

class BuildCommander(Commander):
  def __init__(self, service_hub=None):
    super().__init__()
    self.service_hub = service_hub

  def can_afford(self, structure):
    return True