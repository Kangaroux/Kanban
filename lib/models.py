import json
from datetime import datetime
from itertools import chain

from django.core import serializers
from django.db import models
from django.utils import timezone


class ListField(models.TextField):
  empty_strings_allowed = False

  def from_db_value(self, value, *args, **kwargs):
    return self.to_python(value)

  def to_python(self, value):
    if isinstance(value, list):
      return value

    if not value:
      return []

    return json.loads(value)

  def get_prep_value(self, value):
    if not value:
      return "[]"

    return json.dumps(value, separators=(',', ':'))


class Serializable:
  """ Interface for models which are serializable into JSON """

  # A list of fields which will be serialized. If this is blank, every field
  # will be serialized
  SERIALIZE_FIELDS = ()

  @classmethod
  def serialize(cls, objects, only=None, exclude=None):
    if only and exclude:
      raise ValueError("Both `only` and `exclude` cannot be used for serializing")

    if cls.SERIALIZE_FIELDS:
      fields = set(cls.SERIALIZE_FIELDS)
    else:
      fields = set(
        [ f.name for f in cls._meta.get_fields() if hasattr(f, "attname") ]
      )

    if only:
      fields &= set(only)

    if exclude:
      fields -= set(exclude)

    try:
      data = json.loads(serializers.serialize("json", objects, fields=fields))

      for instance in range(len(data)):
        data[instance]["fields"]["id"] = data[instance]["pk"]
        data[instance] = data[instance]["fields"]
    except TypeError:
      # This handles the case where `objects` is a single object
      data = json.loads(serializers.serialize("json", [objects], fields=fields))[0]
      data["fields"]["id"] = data["pk"]
      data = data["fields"]

    return data


class BaseModel(Serializable, models.Model):
  """ Base model class which has created and updated fields for generating timestamps """

  class Meta:
    abstract = True

  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)