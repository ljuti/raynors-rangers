import abc

from sc2.unit import Unit
from sc2.position import Point2
from sc2.constants import AbilityId

class BaseStructure():
  __metaclass__ = abc.ABCMeta

  def __init__(self, unit: Unit):
    self.unit = unit
    self.tag = unit.tag
    self.type_id = unit.type_id
    self.designation = None
    self.saved_position = unit.position

  @abc.abstractmethod
  def post_construction_complete(self, game):
    """ Implement this in structure classes """
    return

  def request_repairs(self, game):
    """ Call for one SCV to repair the structure """
    scv = game.workers.prefer_idle.closest_to(self.unit.position)
    if scv:
      game.command_bus.queue(scv(AbilityId.EFFECT_REPAIR_SCV, self.unit))

  @property
  def position(self) -> Point2:
    return self.saved_position

  @property
  def under_fire(self) -> bool:
    return bool(
      self.unit.health_percentage < 1
      and self.close_enemies
    )

  @property
  def damaged(self) -> bool:
    return bool(
      self.unit.health_percentage < 1
    )
