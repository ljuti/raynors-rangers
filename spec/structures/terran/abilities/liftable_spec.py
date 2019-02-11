from bot.structures.terran.abilities.liftable import Liftable
from bot.structures.models.terran.barracks import BarracksModel

from bot.command_bus import CommandBus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property
import doubles

from sc2.constants import UnitTypeId

with description("Liftable") as self:
  pass