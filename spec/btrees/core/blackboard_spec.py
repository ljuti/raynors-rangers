from bot.btrees.core.blackboard import Blackboard
from bot.btrees.core.tick import Tick

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false, be_above, be_empty
import doubles

with description("Blackboard") as self:
  with description("Initialization") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()

    with it("can be instantiated"):
      expect(self.blackboard).to(be_a(Blackboard))
      expect(self.blackboard._base_memory).to(be_empty)
      expect(self.blackboard._tree_memory).to(be_empty)

  with description("Reading and writing") as self:
    with before.each: # pylint: disable=no-member
      self.blackboard = Blackboard()

    with description("Simple case") as self:
      with it("can read and write to the blackboard"):
        self.blackboard.set('variable1', 'string')
        self.blackboard.set('variable2', 100)

        expect(self.blackboard.get('variable1')).to(equal('string'))
        expect(self.blackboard.get('variable2')).to(equal(100))

    with description("Within tree scope") as self:
      with it("can read and write to the blackboard"):
        self.blackboard.set('variable1', 'string', 'tree1')
        self.blackboard.set('variable2', 100, 'tree2')

        expect(self.blackboard.get('variable1', 'tree1')).to(equal('string'))
        expect(self.blackboard.get('variable2', 'tree2')).to(equal(100))

    with description("Within node scope") as self:
      with it("can read and write to the blackboard"):
        self.blackboard.set('variable1', 'value1', 'tree1')
        self.blackboard.set('variable2', 'value2', 'tree1', 'node1')
        self.blackboard.set('variable3', 'value3', 'tree1', 'node2')
        self.blackboard.set('variable4', 'value4', 'tree2')

        expect(self.blackboard.get('variable1', 'tree1')).to(equal('value1'))
        expect(self.blackboard.get('variable2', 'tree1', 'node1')).to(equal('value2'))
        expect(self.blackboard.get('variable3', 'tree1', 'node2')).to(equal('value3'))
        expect(self.blackboard.get('variable4', 'tree2')).to(equal('value4'))