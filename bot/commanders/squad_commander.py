# -*- coding: utf-8 -*-
""" Squad Commander

This is the high-level commander class for executing squad level actions
for army.

Preferably this commander could be given missions to execute, and would
operate independently.
"""

from bot.commanders.commander import Commander

class SquadCommander(Commander):
  def __init__(self):
    super().__init__()