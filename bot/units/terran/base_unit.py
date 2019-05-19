# -*- coding: utf-8 -*-
""" Base Unit

Terran base unit class.
"""

from bot.btrees.core.blackboard import Blackboard

class BaseUnit():
  def __init__(self, unit):
    self.unit = unit
    self.tag = unit.tag
    self.behavior = None
    self.blackboard = None
    self.type_id = unit.type_id

  def update(self, game, unit):
    """ Game loop update method
    
    Called during every game loop. If a behavior is assigned to the unit,
    it will attempt to execute the next tick in the behavior tree.
    """
    self.unit = unit
    if self.behavior:
      if self.blackboard is None:
        self.blackboard = Blackboard()
      self.behavior.tick(self, self.blackboard)
