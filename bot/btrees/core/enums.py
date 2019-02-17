import enum

class BTreeStatus(enum.Enum):
  SUCCESS = 0
  FAILURE = 1
  RUNNING = 2
  ERROR = 3

class BTreeCategory(enum.Enum):
  ACTION = 0
  COMPOSITE = 1
  CONDITION = 2
  DECORATOR = 3