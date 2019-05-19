# -*- coding: utf-8 -*-
""" Army Unit

Army Unit class should implement all behavior that is shared by army units.
Only SCV is not counted as Army Unit.
"""

from bot.units.terran.base_unit import BaseUnit

class ArmyUnit(BaseUnit):
  def __init__(self, unit):
    super().__init__(unit)