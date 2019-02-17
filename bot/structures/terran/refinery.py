from bot.structures.terran.base_structure import BaseStructure
from bot.structures.models.terran.refinery import RefineryModel

from sc2.unit import Unit
from sc2.constants import UnitTypeId

class Refinery(BaseStructure):
  def __init__(self, unit: Unit, model: RefineryModel, service_hub):
    super(Refinery, self).__init__(unit, service_hub)
    self.model = model
    self.command_center = None
    self.geyser = None

  @property
  def requires_gatherers(self) -> bool:
    return bool(self.unit.surplus_harvesters < 0)

  @property
  def is_fully_saturated(self) -> bool:
    return bool(self.unit.assigned_harvesters == self.unit.ideal_harvesters)

  @property
  def is_over_saturated(self) -> bool:
    return bool(self.unit.surplus_harvesters > 0)

  def post_construction_complete(self, game):
    self.register_command_center(game)
    if self.command_center:
      self.command_center.register_refinery(self)
    scvs = game.workers.gathering.take(3)
    for scv in scvs:
      game.command_bus.queue(scv.gather(self.unit))

  def register_command_center(self, game):
    cc_unit = game.units.of_type([UnitTypeId.COMMANDCENTER, UnitTypeId.ORBITALCOMMAND, UnitTypeId.PLANETARYFORTRESS]).closest_to(self.unit.position)
    if cc_unit and self.unit.position.distance_to(cc_unit.position) < 10:
      self.command_center = game.structures.get_with_tag(cc_unit.tag)