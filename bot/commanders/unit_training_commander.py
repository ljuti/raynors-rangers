# -*- coding: utf-8 -*-
""" Unit Training Commander

This is the high-level commander class for building army units and
compositions requested by the army commander or the main general.
"""

from bot.commanders.commander import Commander

from sc2.constants import UnitTypeId

class UnitTrainingCommander(Commander):
  def __init__(self):
    super().__init__()
    self.structures = None

  def train(self, type_id, amount=None):
    structures = self.production_structures_for(type_id)
    if structures:
      # Train units
      return True
    return False

  def production_structures_for(self, type_id):
    return self.structures.production_structures_for(type_id)