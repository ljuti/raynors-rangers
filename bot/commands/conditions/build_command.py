import enum

class GameConditionType(enum.Enum):
  AT_SUPPLY = 0
  AT_GAME_TIME = 1

class BuildCommandGameCondition():
  def __init__(self, data=(None, None)):
    self.resolve_condition_type(data[0])
    self.resolve_condition_value(data[1])

  def resolve_condition_type(self, c_type):
    if c_type == "at_supply":
      self.type_id = GameConditionType.AT_SUPPLY
    elif c_type == "at_game_time":
      self.type_id = GameConditionType.AT_GAME_TIME

  def resolve_condition_value(self, value):
    self.value = value