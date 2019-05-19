# -*- coding: utf-8 -*-
""" Bot Main Script

Guidelines:
- on_step (called by the bot runner) should only have pre-game setup
  and main loop call
- try to keep main loop to 15 lines or less
"""

import time
import json
from pathlib import Path

from bot.service_hub import ServiceHub
from bot.command_bus import CommandBus
from bot.data_store import DataStore
from bot.uplink.uplink import Uplink
from bot.registries.unit_registry import UnitRegistry
from bot.registries.structure_registry import StructureRegistry

import random
import sc2
from sc2.constants import UnitTypeId

class MyBot(sc2.BotAI):
    with open(Path(__file__).parent / "../botinfo.json") as f:
        NAME = json.load(f)["name"]

    def __init__(self):
        self.service_hub = ServiceHub(self)
        self.command_bus = CommandBus(self)
        self.unit_registry = UnitRegistry(self, self.service_hub)
        self.structures = StructureRegistry(service_hub=self.service_hub)
        self.service_hub.register(self.command_bus)
        self.uplink = Uplink()

    def on_start(self):
        pass

    async def _issue_unit_added_events(self):
        for unit in self.units.not_structure:
            if unit.tag not in self._units_previous_map:
                await self.on_unit_created(unit)
        for unit in self.units.structure:
            if unit.tag not in self._units_previous_map:
                await self.on_building_construction_started(unit)

    async def on_unit_created(self, unit):
        self.unit_registry.add(unit)

    async def on_unit_destroyed(self, unit_tag):
        self.unit_registry.remove(unit_tag)

    async def on_building_construction_started(self, unit):
        print(f"Started building {unit.name} at {unit.position}")
        self.structures.add(unit, self)

    async def on_building_construction_complete(self, unit):
        self.structures.complete(unit)

    async def on_step(self, iteration):
        if not iteration:
            # await self.uplink.connect()
            self.pre_game_setup(self)

        if iteration == 0:
            self.iteration_zero(self)

        await self.main_loop(self)

    async def main_loop(self, game):
        if self.scouting_scv is None:
            scv = random.choice(self.unit_registry.scvs())
            if scv:
                self.scouting_scv = scv
                scv.begin_scouting()

        self.unit_registry.make_decisions(self)

        if game.time % 10 == 0:
            print(self.data_store.locations.ordered_expansions)
            scv = self.workers.random

            if self.can_afford(UnitTypeId.SUPPLYDEPOT) and self.already_pending(UnitTypeId.SUPPLYDEPOT) < 1:
                placement = await self.find_placement(UnitTypeId.SUPPLYDEPOT, near=self.start_location)
                if placement:
                    await self.do(scv.build(UnitTypeId.SUPPLYDEPOT, placement))

            await self.uplink.relay(scv.build(UnitTypeId.BARRACKS, self.start_location))

        if game.time % 15 == 0:
            self.print_ramps(game)

        await self.command_bus.execute()

    def pre_game_setup(self, game):
        self.data_store = DataStore(self)
        self.data_store.locations.main = self.start_location
        self.data_store.locations.map_center = self.game_info.map_center
        self.data_store.locations.prepare_expansions(self.expansion_locations)
        self.data_store.locations.prepare_proxy_locations()
        self.service_hub.register(self.data_store.locations)
        self.scouting_scv = None

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
