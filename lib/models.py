import json
from itertools import chain

from datetime import datetime

from django.db import models
from django.utils import timezone


class ListField(models.TextField):
  def from_db_value(self, value, *args, **kwargs):
    return self.to_python(value)

  def to_python(self, value):
    if isinstance(value, list):
      return value

    if value is None or value == "":
      return []

    return json.loads(value)

  def get_prep_value(self, value):
    if value is None or value == "":
      return "[]"

    return json.dumps(value)


class Serializable:
  """ Interface for models which are serializable into JSON """

  # A list of fields which will be serialized. If this is blank, every field
  # will be serialized
  SERIALIZE_FIELDS = ()

  def serialize(self, only=None, exclude=None):
    if only and exclude:
      raise ValueError("Both `only` and `exclude` cannot be used for serializing")

    if self.SERIALIZE_FIELDS:
      fields = set(self.SERIALIZE_FIELDS)
    else:
      # This monstrosity is brought to you by Django 2.0
      fields = set(
          [ f.name for f in self._meta.get_fields() if hasattr(f, "attname") ]
        )

    data = {}

    if only:
      fields &= set(only)

    if exclude:
      fields -= set(exclude)

    for f in fields:
      val = getattr(self, f)

      if isinstance(val, datetime):
        data[f] = val.isoformat()
      elif isinstance(val, (list, int, float, bool)):
        data[f] = val
      elif isinstance(val, models.Model):
        data[f] = val.id
      else:
        data[f] = str(val)

    return data


class BaseModel(Serializable, models.Model):
  """ Base model class which has created and updated fields for generating timestamps """

  class Meta:
    abstract = True

  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)