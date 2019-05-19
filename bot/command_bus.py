# -*- coding: utf-8 -*-
""" Command Bus

Command Bus executes queued actions to the game engine. Each game loop,
the bot evaluates state and decides some actions. These actions are
queued at the command bus which will execute them in a batch at the
end of the game loop.

API is simple:
* prioritize - execute an action right now
* queue - append an action to the execution queue
* execute - execute all actions
* execute_silently - execute actions in a batch
"""

from sc2.unit_command import UnitCommand

class CommandBus():
  def __init__(self, game):
    self.game = game
    self.actions = []
    self.silent_actions = []

  def prioritize(self, command: UnitCommand):
    return True

  def queue(self, command: UnitCommand, silent=True):
    if silent:
      self.silent_actions.append(command)
    else:
      self.actions.append(command)
    return True

  async def execute(self):
    for action in self.actions:
      await self.game.do(action)

    self.actions.clear()
    await self.execute_silently()

  async def execute_silently(self):
    await self.game.do_actions(self.silent_actions)
    self.silent_actions.clear()