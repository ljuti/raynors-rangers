# -*- coding: utf-8 -*-
""" Command Center

Terran command center structure class.

Implements the following abilities
- Landable
- Liftable
- Morphable (to orbital command or planetary fortress)

Because command center is the base unit object for all three command center
types in the game, all unit objects should be CommandCenter and then
underlying unit model class can change to reflect the properties of the unit.
"""

from bot.structures.terran.base_structure import BaseStructure
from bot.structures.terran.abilities.landable import Landable
from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.terran.abilities.morphable import Morphable
from bot.structures.models.terran.command_center import CommandCenterModel
from bot.structures.models.terran.orbital_command import OrbitalCommandModel
from bot.structures.models.terran.planetary_fortress import PlanetaryFortressModel

from sc2.unit import Unit

class CommandCenter(BaseStructure, Landable, Liftable, Morphable):
  def __init__(self, unit: Unit, model: CommandCenterModel, service_hub):
    BaseStructure.__init__(self, unit, service_hub)

    self.unit = unit
    self.model = model

    Landable.__init__(self, unit, model)
    Liftable.__init__(self, unit, model)
    Morphable.__init__(self, unit, model)