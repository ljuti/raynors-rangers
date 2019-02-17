import uuid

from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick

class BehaviorTree(object):
  def __init__(self):
    self.id = str(uuid.uuid4())
    self.title = "BehaviorTree"
    self.description = ""
    self.properties = {}
    self.root = None
    self.debug = None

  def get_tick_object(self, target, blackboard: Blackboard):
    tick_object = Tick()
    tick_object.target = target
    tick_object.blackboard = blackboard
    tick_object.tree = self
    tick_object.debug = self.debug
    return tick_object

  def tick(self, target, blackboard: Blackboard):
    tick = self.get_tick_object(target, blackboard)
    self.root._execute(tick)
    self.finish_tick(tick, blackboard)

  def finish_tick(self, tick: Tick, blackboard: Blackboard):
    last_open_nodes = blackboard.get('open_nodes', self.id)
    current_open_nodes = tick._open_nodes

    start = 0
    for node1, node2 in zip(last_open_nodes, current_open_nodes):
      start += 1
      if node1 != node2:
        break

    for val in range(len(last_open_nodes) - 1, start - 1, -1):
      last_open_nodes[val]._close(tick)

    blackboard.set('open_nodes', current_open_nodes, self.id)
    blackboard.set('node_count', tick._node_count, self.id)