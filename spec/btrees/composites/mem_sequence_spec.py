from bot.btrees.composites.mem_sequence import MemSequence
from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick
from bot.btrees.core.enums import BTreeStatus

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, contain, be_empty
import doubles

def get_node(status):
  node = doubles.InstanceDouble('bot.btrees.core.base_node.BaseNode')
  doubles.allow(node)._execute.and_return(status)
  return node

with description("MemSequence") as self:
  with after.each: # pylint: disable=no-member
    doubles.verify
    doubles.teardown

  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.sequence = MemSequence()

    with it("can be instantiated"):
      expect(self.sequence).to(be_a(MemSequence))
      expect(self.sequence.id).not_to(equal(None))
      expect(self.sequence.name).to(equal("MemSequence"))
      expect(self.sequence.title).to(equal("MemSequence"))

  with description("Success scenario") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("runs through sequence successfully if all nodes return a success"):
      node1 = get_node(BTreeStatus.SUCCESS)
      node2 = get_node(BTreeStatus.SUCCESS)
      node3 = get_node(BTreeStatus.SUCCESS)

      doubles.allow(node1)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node2)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node3)._execute.and_return(BTreeStatus.SUCCESS).once()

      doubles.allow(self.blackboard).get.and_return(0)
      sequence = MemSequence(children=[node1, node2, node3])
      status = sequence.tick(self.tick)

      expect(status).to(equal(BTreeStatus.SUCCESS))

  with description("Failure scenario") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("runs through sequence and return failure on failed node"):
      node1 = get_node(BTreeStatus.SUCCESS)
      node2 = get_node(BTreeStatus.SUCCESS)
      node3 = get_node(BTreeStatus.FAILURE)
      node4 = get_node(BTreeStatus.SUCCESS)

      doubles.allow(node1)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node2)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node3)._execute.and_return(BTreeStatus.FAILURE).once()
      doubles.allow(node4)._execute.and_return(BTreeStatus.SUCCESS).never()

      doubles.allow(self.blackboard).get.and_return(0)
      sequence = MemSequence(children=[node1, node2, node3, node4])
      status = sequence.tick(self.tick)

      expect(status).to(equal(BTreeStatus.FAILURE))

  with description("Running scenario") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("runs through sequence and returns running on running node"):
      node1 = get_node(BTreeStatus.SUCCESS)
      node2 = get_node(BTreeStatus.SUCCESS)
      node3 = get_node(BTreeStatus.RUNNING)
      node4 = get_node(BTreeStatus.SUCCESS)

      doubles.allow(node1)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node2)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node3)._execute.and_return(BTreeStatus.RUNNING).once()
      doubles.allow(node4)._execute.and_return(BTreeStatus.SUCCESS).never()

      doubles.allow(self.blackboard).get.and_return(0)
      sequence = MemSequence(children=[node1, node2, node3, node4])
      status = sequence.tick(self.tick)

      expect(status).to(equal(BTreeStatus.RUNNING))

  with description("Error scenario") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("runs through sequence and returns error on errored node"):
      node1 = get_node(BTreeStatus.SUCCESS)
      node2 = get_node(BTreeStatus.SUCCESS)
      node3 = get_node(BTreeStatus.ERROR)
      node4 = get_node(BTreeStatus.SUCCESS)

      doubles.allow(node1)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node2)._execute.and_return(BTreeStatus.SUCCESS).once()
      doubles.allow(node3)._execute.and_return(BTreeStatus.ERROR).once()
      doubles.allow(node4)._execute.and_return(BTreeStatus.SUCCESS).never()

      doubles.allow(self.blackboard).get.and_return(0)
      sequence = MemSequence(children=[node1, node2, node3, node4])
      status = sequence.tick(self.tick)

      expect(status).to(equal(BTreeStatus.ERROR))

  with description("Memorizing") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()
      self.tree = BehaviorTree()
      self.tick = Tick(tree=self.tree, blackboard=self.blackboard)

    with it("remembers what has been called"):
      node1 = get_node(BTreeStatus.SUCCESS)
      node2 = get_node(BTreeStatus.SUCCESS)
      node3 = get_node(BTreeStatus.RUNNING)
      node4 = get_node(BTreeStatus.FAILURE)
      node5 = get_node(BTreeStatus.SUCCESS)

      sequence = MemSequence(children=[node1, node2, node3, node4, node5])
      sequence.id = "seq1"
      sequence.open(self.tick)

      status = sequence.tick(self.tick)

      doubles.expect(self.tick.blackboard).set('is_open', True, self.tree.id, sequence.id).once()
      doubles.expect(self.tick.blackboard).set('running_child', 0, self.tree.id, sequence.id).once()
      doubles.expect(self.tick.blackboard).set('running_child', 2, self.tree.id, sequence.id).once()

      expect(self.blackboard.get('running_child', self.tree.id, sequence.id)).to(equal(2))

    with it("remembers what has been called"):
      node1 = get_node(BTreeStatus.SUCCESS)
      node2 = get_node(BTreeStatus.SUCCESS)
      node3 = get_node(BTreeStatus.SUCCESS)
      node4 = get_node(BTreeStatus.FAILURE)
      node5 = get_node(BTreeStatus.SUCCESS)

      doubles.allow(node1)._execute.never()
      doubles.allow(node2)._execute.never()
      doubles.allow(node3)._execute.once()
      doubles.allow(node4)._execute.once()
      doubles.allow(node5)._execute.never()

      sequence = MemSequence(children=[node1, node2, node3, node4, node5])
      doubles.allow(self.tick.blackboard).get.and_return(2)
      status = sequence.tick(self.tick)