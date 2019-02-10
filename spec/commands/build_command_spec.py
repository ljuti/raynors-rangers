from bot.factories.build_command import BuildCommandFactory
from bot.commands.build_command import BuildCommand
from bot.commands.requirements.build_command import BuildCommandRequirement
from bot.commands.conditions.build_command import BuildCommandGameCondition
from bot.locations.location import StructurePosition, NamedPosition, OnStructurePosition, BaseLocationPosition, NextToStructurePosition

from mamba import description, context, it, shared_context, before, after
from expects import expect, be_a, equal, be_true, be_callable, have_property, be_false
import doubles

from sc2.constants import UnitTypeId
from sc2.position import Point2

with description("BuildCommand") as self:
  with description("Initialization") as self:
    with it("can be instantiated"):
      command = BuildCommand()
      expect(command).to(be_a(BuildCommand))

  with description("Properties") as self:
    with before.each: # pylint: disable=no-member
      self.command = BuildCommand()

    with it("has an ID"):
      expect(self.command).to(have_property('command_id'))
      expect(self.command.command_id).not_to(equal(None))

    with it("has a structure property"):
      expect(self.command).to(have_property('structure'))

    with it("has a position property"):
      expect(self.command).to(have_property('position'))

    with it("has a requirements property"):
      expect(self.command).to(have_property('requirements'))

    with it("has a game conditions property"):
      expect(self.command).to(have_property('game_conditions'))

    with it("has a meta object"):
      expect(self.command).to(have_property('meta'))

    with it("has a reference to whom it's been assigned"):
      expect(self.command).to(have_property('assigned_to'))

    with it("has a flag for under execution"):
      expect(self.command).to(have_property('under_execution'))

    with it("has a flag for completed"):
      expect(self.command).to(have_property('completed'))

  with description("Validity and executability") as self:
    with description("Validity") as self:
      with before.each: # pylint: disable=no-member
        self.command = BuildCommand()
        self.data = {
          "structure": UnitTypeId.BARRACKS,
          "position": StructurePosition(Point2((50.0, 50.0)))
        }

      with it("can tell if it's valid or not"):
        expect(self.command).to(have_property('is_valid'))

      with it("is not valid if structure is missing"):
        self.command.init(self.data)
        expect(self.command.is_valid).to(be_true)
        self.command.structure = None
        expect(self.command.is_valid).not_to(be_true)
        self.command.structure = UnitTypeId.MARINE
        expect(self.command.is_valid).not_to(be_true)

      with it("is not valid is position is missing"):
        self.command.init(self.data)
        expect(self.command.is_valid).to(be_true)
        self.command.position = None
        expect(self.command.is_valid).not_to(be_true)
        self.command.position = "foo"
        expect(self.command.is_valid).not_to(be_true)

    with description("Executability") as self:
      """ TODO: Test and implement the executability in the class that actually handles commands. """
      with before.each: # pylint: disable=no-member
        self.command = BuildCommand()
        self.data = {
          "structure": UnitTypeId.BARRACKS,
          "position": StructurePosition(Point2((50.0, 50.0)))
        }

      with it("is executable right away if it's valid, has no requirements, and game conditions are OK"):
        self.command.init(self.data)
        expect(self.command.is_executable).to(be_true)

  with description("Requirements") as self:
    with before.each: # pylint: disable=no-member
      self.command = BuildCommand()
      self.data = {
        "structure": UnitTypeId.BARRACKS,
        "position": StructurePosition(Point2((50.0, 50.0))),
        "requirements": [
          {
            "type": "structure",
            "structure": UnitTypeId.SUPPLYDEPOT
          }
        ]
      }

    with it("has an array of requirement objects"):
      self.command.init(self.data)
      expect(len(self.command.requirements)).to(equal(1))
      for requirement in self.command.requirements:
        expect(requirement).to(be_a(BuildCommandRequirement))

  with description("Game conditions") as self:
    with before.each: # pylint: disable=no-member
      self.command = BuildCommand()
      self.data = {
        "structure": UnitTypeId.BARRACKS,
        "position": StructurePosition(Point2((50.0, 50.0))),
        "conditions": {
          "at_supply": 15,
          "at_game_time": 45,
        }
      }

    with it("has an array of game conditions objects"):
      self.command.init(self.data)
      expect(len(self.command.game_conditions)).to(equal(2))
      for condition in self.command.game_conditions:
        expect(condition).to(be_a(BuildCommandGameCondition))

  with description("Position") as self:
    with description("as StructurePosition") as self:
      with before.each: # pylint: disable=no-member
        self.command = BuildCommand()
        self.data = {
          "structure": UnitTypeId.BARRACKS,
          "position": StructurePosition(Point2((50.0, 50.0)))
        }

      with it("has a position as StructurePosition"):
        self.command.init(self.data)
        expect(self.command.position).to(be_a(StructurePosition))
        expect(self.command.position.coordinates).to(be_a(Point2))

    with description("as Point object") as self:
      with before.each: # pylint: disable=no-member
        self.command = BuildCommand()
        self.data = {
          "structure": UnitTypeId.BARRACKS,
          "position": Point2((50.0, 40.0))
        }

      with it("has a position as StructurePosition when given a Point as data"):
        self.command.init(self.data)
        expect(self.command.position).to(be_a(StructurePosition))
        expect(self.command.position.coordinates).to(equal(Point2((50.0, 40.0))))

    with description("as other input (e.g. from JSON)") as self:
      with description("named position") as self:
        with before.each: # pylint: disable=no-member
          self.command = BuildCommand()
          self.data = {
            "structure": UnitTypeId.STARPORT,
            "position": {
              "name": "starport_1"
            }
          }

        with it("has a NamedPosition with correct position designation"):
          self.command.init(self.data)
          expect(self.command.position).to(be_a(NamedPosition))
          expect(self.command.position.position_type).to(equal("name"))
          expect(self.command.position.designation).to(equal("starport_1"))
          expect(self.command.position.coordinates_resolved).to(be_false)

      with description("designated structure") as self:
        with before.each: # pylint: disable=no-member
          self.command = BuildCommand()
          self.data = {
            "structure": UnitTypeId.TECHLAB,
            "position": {
              "structure": "starport_1"
            }
          }

        with it("has a OnStructurePosition with correct position designation"):
          self.command.init(self.data)
          expect(self.command.position).to(be_a(OnStructurePosition))
          expect(self.command.position.position_type).to(equal("structure"))
          expect(self.command.position.designation).to(equal("starport_1"))
          expect(self.command.position.coordinates_resolved).to(be_false)

      with description("designated base") as self:
        with before.each: # pylint: disable=no-member
          self.command = BuildCommand()
          self.data = {
            "structure": UnitTypeId.REFINERY,
            "position": {
              "base": "main_cc"
            }
          }

        with it("has a BaseLocationPosition"):
          self.command.init(self.data)
          expect(self.command.position).to(be_a(BaseLocationPosition))
          expect(self.command.position.position_type).to(equal("base"))
          expect(self.command.position.designation).to(equal("main_cc"))
          expect(self.command.position.coordinates_resolved).to(be_false)

      with description("next to a structure") as self:
        with before.each: # pylint: disable=no-member
          self.command = BuildCommand()
          self.data = {
            "structure": UnitTypeId.FACTORY,
            "position": {
              "next_to": "barracks_1"
            }
          }

        with it("has a NextToStructurePosition"):
          self.command.init(self.data)
          expect(self.command.position).to(be_a(NextToStructurePosition))
          expect(self.command.position.position_type).to(equal("next_to"))
          expect(self.command.position.designation).to(equal("barracks_1"))
          expect(self.command.position.coordinates_resolved).to(be_false)
