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

        await self.main_loop(self)

        # try:
        #     # step_start = time.time()
        #     budget = self.time_budget_available
        #     if budget and budget < 0.3:
        #         print("** SKIPPING A STEP to avoid bot freezing up **")
        #     else:
        #         await self.main_loop(self)
        # except Exception as crash:
        #     print("|||||||| CRASHED ||||||||")
        #     print(crash)

    async def main_loop(self, game):
        if game.time % 10 == 0:
            game_info = await self._client.get_game_info()
            game_info.map_ramps = self._game_info._find_ramps()
            # print(game_info.map_ramps)
            # self.print_ramps(game, game_info.map_ramps)

        if game.time % 15 == 0:
            self.print_ramps(game)

    def pre_game_setup(self, game):
        pass

    def iteration_zero(self, game):
        self.print_ramps(game)

    def print_ramps(self, game, ramps=None):
        if game.game_info.map_ramps:
            game_ramps = sorted(game.game_info.map_ramps, key=lambda x: x.top_center.distance_to(self.start_location))
            close = game_ramps[0:1]

            if ramps:
                close = ramps

            print("*** RAMPS (close) ***")
            for ramp in close:
                print(f"Ramp at {ramp.top_center} (top) {ramp.bottom_center} (bottom)")
                # print(f"  points: {ramp.points}")
                print(f"  size: {ramp.size}")
                print(f"  upper: {ramp.upper}")
                print(f"  upper two: {ramp.upper2_for_ramp_wall}")
                print("\n")
