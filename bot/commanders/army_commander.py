# -*- coding: utf-8 -*-
""" Army Commander

This is the high-level commander class for the whole army and/or larger
army groups. It should command squads that are part of the army and decide
on a high level what the army should do at any given time.
"""

from bot.commanders.commander import Commander

class ArmyCommander(Commander):
  def __init__(self):
    super().__init__()