import abc
import binascii
import os

class Command():
  __metaclass__ = abc.ABCMeta

  def __init__(self):
    self.command_id = self.generate_id()

  def generate_id(self):
    return binascii.hexlify(os.urandom(8)).decode('utf-8')

  @abc.abstractmethod
  async def execute(self, game, actor=None):
    raise NotImplementedError