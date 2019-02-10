import abc

class Command():
  __metaclass__ = abc.ABCMeta

  def __init__(self):
    pass

  @abc.abstractmethod
  async def execute(self, game, actor=None):
    raise NotImplementedError