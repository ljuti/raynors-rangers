from bot.btrees.composites.mem_priority import MemPriority
from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.enums import BTreeStatus
from bot.btrees.core.tick import Tick

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, contain, be_empty
import doubles

def get_node(status):
  node = doubles.InstanceDouble('bot.btrees.core.base_node.BaseNode')
  doubles.allow(node)._execute.and_return(status)
  return node

with description("MemPriority") as self:
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.priority = MemPriority()

    with it("can be instantiated"):
      expect(self.priority).to(be_a(MemPriority))
      expect(self.priority.id).not_to(equal(None))
      expect(self.priority.title).to(equal("MemPriority"))
      expect(self.priority.name).to(equal("MemPriority"))

  with description("Scenarios") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with description("Success") as self:
      with it("executes success scenario"):
        node1 = get_node(BTreeStatus.FAILURE)
        node2 = get_node(BTreeStatus.SUCCESS)
        node3 = get_node(BTreeStatus.SUCCESS)

        doubles.expect(node1)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node2)._execute.and_return(BTreeStatus.SUCCESS).once()
        doubles.expect(node3)._execute.and_return(BTreeStatus.SUCCESS).never()

        doubles.allow(self.blackboard).get.and_return(0)
        priority = MemPriority(children=[node1, node2, node3])
        status = priority.tick(self.tick)

        expect(status).to(equal(BTreeStatus.SUCCESS))

    with description("Failure") as self:
      with it("executes failure scenario"):
        node1 = get_node(BTreeStatus.FAILURE)
        node2 = get_node(BTreeStatus.FAILURE)
        node3 = get_node(BTreeStatus.FAILURE)

        doubles.expect(node1)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node2)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node3)._execute.and_return(BTreeStatus.FAILURE).once()

        doubles.allow(self.blackboard).get.and_return(0)
        priority = MemPriority(children=[node1, node2, node3])
        status = priority.tick(self.tick)

        expect(status).to(equal(BTreeStatus.FAILURE))

    with description("Running") as self:
      with it("executes a running scenario"):
        node1 = get_node(BTreeStatus.FAILURE)
        node2 = get_node(BTreeStatus.FAILURE)
        node3 = get_node(BTreeStatus.RUNNING)
        node4 = get_node(BTreeStatus.SUCCESS)

        doubles.expect(node1)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node2)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node3)._execute.and_return(BTreeStatus.RUNNING).once()
        doubles.expect(node4)._execute.and_return(BTreeStatus.SUCCESS).never()

        doubles.allow(self.blackboard).get.and_return(0)
        priority = MemPriority(children=[node1, node2, node3, node4])
        status = priority.tick(self.tick)

        expect(status).to(equal(BTreeStatus.RUNNING))

    with description("Error") as self:
      with it("executes a error scenario"):
        node1 = get_node(BTreeStatus.FAILURE)
        node2 = get_node(BTreeStatus.FAILURE)
        node3 = get_node(BTreeStatus.ERROR)
        node4 = get_node(BTreeStatus.SUCCESS)

        doubles.expect(node1)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node2)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node3)._execute.and_return(BTreeStatus.ERROR).once()
        doubles.expect(node4)._execute.and_return(BTreeStatus.SUCCESS).never()

        doubles.allow(self.blackboard).get.and_return(0)
        priority = MemPriority(children=[node1, node2, node3, node4])
        status = priority.tick(self.tick)

        expect(status).to(equal(BTreeStatus.ERROR))

    with description("Memorizing the call stack") as self:
      with it("remembers what was called"):
        node1 = get_node(BTreeStatus.FAILURE)
        node2 = get_node(BTreeStatus.FAILURE)
        node3 = get_node(BTreeStatus.RUNNING)
        node4 = get_node(BTreeStatus.SUCCESS)
        node5 = get_node(BTreeStatus.FAILURE)

        priority = MemPriority(children=[node1, node2, node3, node4, node5])
        priority.id = "node1"
        priority.open(self.tick)

        status = priority.tick(self.tick)

        doubles.expect(self.tick.blackboard).set('is_open', True, self.tree.id, 'node1').once()
        doubles.expect(self.tick.blackboard).set('running_child', 0, self.tree.id, 'node1').once()
        doubles.expect(self.tick.blackboard).set('running_child', 2, self.tree.id, 'node1').once()

        expect(self.blackboard.get('running_child', self.tree.id, 'node1')).to(equal(2))

      with it("can continue from memory"):
        node1 = get_node(BTreeStatus.FAILURE)
        node2 = get_node(BTreeStatus.FAILURE)
        node3 = get_node(BTreeStatus.FAILURE)
        node4 = get_node(BTreeStatus.SUCCESS)
        node5 = get_node(BTreeStatus.FAILURE)

        doubles.expect(node1)._execute.and_return(BTreeStatus.FAILURE).never()
        doubles.expect(node2)._execute.and_return(BTreeStatus.FAILURE).never()
        doubles.expect(node3)._execute.and_return(BTreeStatus.FAILURE).once()
        doubles.expect(node4)._execute.and_return(BTreeStatus.SUCCESS).once()
        doubles.expect(node5)._execute.and_return(BTreeStatus.FAILURE).never()

        priority = MemPriority(children=[node1, node2, node3, node4, node5])
        doubles.allow(self.tick.blackboard).get.and_return(2)
        status = priority.tick(self.tick)