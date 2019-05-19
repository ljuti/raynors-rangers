# -*- coding: utf-8 -*-
""" Data Store

Data Store contains all data stores for the bot.
"""

from bot.stores.build_order_data import BuildOrderData
from bot.stores.economic_data import EconomicData
from bot.stores.location_data import LocationData

class DataStore():
  def __init__(self, game):
    self.game = game
    self.build_order = BuildOrderData()
    self.economic = EconomicData()
    self.locations = LocationData()

  def register(self, store):
    if isinstance(store, BuildOrderData):
      self.build_order = store
    if isinstance(store, EconomicData):
      self.economic = store
    if isinstance(store, LocationData):
      self.locations = store

  def get(self, service):
    if service is BuildOrderData:
      return self.build_order
    elif service is EconomicData:
      return self.economic
    elif service is LocationData:
      return self.locations