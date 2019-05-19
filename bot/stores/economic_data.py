# -*- coding: utf-8 -*-
""" Economic Data Store

Economic Data Store tracks how many resources have been collected, spent,
and destroyed.
"""

from sc2.game_state import Common

class EconomicData():
    def __init__(self):
        self.collected_minerals = 0
        self.collected_gas = 0
        self.collection_rate_minerals = 0
        self.collection_rate_gas = 0
        self.spent_minerals = 0
        self.spent_gas = 0
        self.lost_minerals = 0
        self.lost_gas = 0
        self.killed_minerals = 0
        self.killed_gas = 0
        self.mineral_delta = 0
        self.gas_delta = 0

        self.common = Common(None)
        self.scores = None

        self.scv_minerals_per_minute = 58.75
        self.mule_minerals_per_minute = 225
        self.scv_gas_per_minute = 56.5

    def update(self, common, scores):
        self.scores = scores
        self.common = common
        self.update_economy_data(scores)
        self.update_scores(scores)

    def update_economy_data(self, score):
        self.collected_minerals = score.collected_minerals
        self.collected_gas = score.collected_vespene
        self.collection_rate_minerals = score.collection_rate_minerals
        self.collection_rate_gas = score.collection_rate_vespene

    def update_scores(self, score):
        self.spent_minerals = score.total_used_minerals
        self.spent_gas = score.total_used_vespene

    @property
    def ahead_economically(self) -> bool:
        return bool(
            (self.scores.killed_minerals_economy >
             self.scores.lost_minerals_economy)
            and (self.scores.killed_vespene_economy > self.scores.lost_vespene_economy)
        )

    @property
    def ahead_in_army(self) -> bool:
        return bool(
            (self.scores.killed_minerals_army > self.scores.lost_minerals_army)
            and (self.scores.killed_vespene_army > self.scores.lost_vespene_army)
        )

    @property
    def current_minerals(self) -> int:
        return int(self.common.minerals)

    @property
    def current_gas(self) -> int:
        return int(self.common.vespene)

    @property
    def current_supply(self) -> int:
        return int(self.common.supply_used)

    @property
    def current_supply_left(self) -> int:
        return int(self.common.supply_left)

    @property
    def current_worker_count(self) -> int:
        return int(self.common.food_workers)

    @property
    def current_idle_worker_count(self) -> int:
        return int(self.common.idle_worker_count)