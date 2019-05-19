# -*- coding: utf-8 -*-
""" Base Registry

Base class for registries.
"""

from collections import defaultdict

class BaseRegistry():
  def __init__(self):
    self.objects = defaultdict(dict)

  def get_with_tag(self, tag):
    if "unit" in self.objects.get(tag, {}):
      return self.objects.get(tag).get("unit", None)
    return None

  def get_with_designation(self, designation):
    keys = [k for k in self.objects.keys() if self.objects[k].get("designation", None) == designation]
    if keys:
      return self.get_with_tag(keys[0])
    return None

  def get_designated(self, designation):
    return self.get_with_designation(designation)

  def get_with_position(self, position):
    keys = [k for k in self.objects.keys() if self.objects[k].get("position", None) == position]
    if keys:
      return self.get_with_tag(keys[0])
    return None

  def add(self, object):
    """ Override in registry class """
    pass

  def remove(self, unit_tag):
    if self.get_with_tag(unit_tag):
      del self.objects[unit_tag]

  def update(self, object):
    """ Override in registry class """
    pass

  @property
  def amount(self) -> int:
    return len(self.objects)