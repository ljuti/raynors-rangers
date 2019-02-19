from bot.btrees.composites.sequence import Sequence

class LoadNextPhase(Sequence):
  def __init__(self, children=None):
    super(LoadNextPhase, self).__init__(children)

    if children is None:
      self.children = [
        
      ]