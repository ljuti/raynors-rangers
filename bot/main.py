import time
import json
from pathlib import Path

from bot.command_bus import CommandBus
from bot.uplink.uplink import Uplink

import sc2
from sc2.constants import UnitTypeId

class MyBot(sc2.BotAI):
    with open(Path(__file__).parent / "../botinfo.json") as f:
        NAME = json.load(f)["name"]

    def __init__(self):
        self.command_bus = CommandBus(self)
        self.uplink = Uplink()

    def on_start(self):
        pass

    async def on_step(self, iteration):
        if not iteration:
            await self.uplink.connect()
            self.pre_game_setup(self)

        if iteration == 0:
            self.iteration_zero(self)

        await self.main_loop(self)

    async def main_loop(self, game):
        if game.time % 10 == 0:
            game_info = await self._client.get_game_info()
            game_info.map_ramps = self._game_info._find_ramps()
            scv = self.workers.random
            await self.uplink.relay(scv.build(UnitTypeId.BARRACKS, self.start_location))

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
