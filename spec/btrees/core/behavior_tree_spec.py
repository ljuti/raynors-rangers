from bot.btrees.core.behavior_tree import BehaviorTree
from bot.btrees.core.base_node import BaseNode
from bot.btrees.core.blackboard import Blackboard

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above
import doubles

with description("BehaviorTree") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.tree = BehaviorTree()

    with it("can be instantiated"):
      expect(self.tree).to(be_a(BehaviorTree))
      expect(self.tree.id).not_to(equal(None))
      expect(self.tree.title).not_to(equal(None))
      expect(self.tree.description).not_to(equal(None))
      expect(self.tree.root).to(equal(None))
      expect(self.tree.properties).to(be_a(dict))

  with description("Root node") as self:
    with before.each: # pylint: disable=no-member
      self.tree = BehaviorTree()
      self.node = BaseNode()
      self.blackboard = Blackboard()
      doubles.allow(self.blackboard).get.and_return([])

    with it("has a root node"):
      target = {}

      self.tree.id = 'tree1'
      self.tree.root = self.node
      self.tree.tick(target, self.blackboard)

      doubles.expect(self.tree.root)._execute.exactly(1)

  with description("Populating the blackboard") as self:
    with before.each: # pylint: disable=no-member
      self.tree = BehaviorTree()
      self.node = BaseNode()
      self.blackboard = Blackboard()
      doubles.allow(self.blackboard).get.and_return([])

    with _it("populates the blackboard"):
      def side_effect(tick):
        tick._enter_node['node1']
        tick._enter_node['node2']

      self.node._execute.side_effect = side_effect

      target = {}

      self.tree.id = 'tree1'
      self.tree.root = self.node
      self.tree.tick(target, self.blackboard)

      # TODO: Complete the spec