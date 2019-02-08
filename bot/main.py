import time
import json
from pathlib import Path

import sc2

class MyBot(sc2.BotAI):
    with open(Path(__file__).parent / "../botinfo.json") as f:
        NAME = json.load(f)["name"]

    async def on_step(self, iteration):
        if not iteration:
            self.pre_game_setup(self)

        if iteration == 0:
            self.iteration_zero(self)

        try:
            # step_start = time.time()
            budget = self.time_budget_available
            if budget and budget < 0.3:
                print("** SKIPPING A STEP to avoid bot freezing up **")
            else:
                await self.main_loop(self)
        except Exception as crash:
            print("|||||||| CRASHED ||||||||")
            print(crash)

    async def main_loop(self, game):
        pass

    def pre_game_setup(self, game):
        pass

    def iteration_zero(self, game):
        pass

    @property
    def time_budget_available(self):
        pass