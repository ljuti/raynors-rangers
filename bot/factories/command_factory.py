import abc

class CommandFactory():
  __metaclass__ = abc.ABCMeta

  def __init__(self):
    pass

  @abc.abstractclassmethod
  def create_command(self, input):
    raise NotImplementedError