from datetime import datetime

from django.db import models
from django.utils import timezone


class Serializable:
  """ Interface for models which are serializable into JSON """

  # A list of fields which will be serialized
  SERIALIZE_FIELDS = ()

  def serialize(self, only=None, exclude=None):
    if only and exclude:
      raise ValueError("Both `only` and `exclude` cannot be used for serializing")

    fields = self.SERIALIZE_FIELDS
    data = {}

    if only:
      fields &= set(only)

    if exclude:
      fields -= set(exclude)

    for f in fields:
      data[f] = getattr(self, f)

      if isinstance(data[f], datetime):
        data[f] = timezone.localtime(data[f]).isoformat()

    return data



class BaseModel(Serializable, models.Model):
  """ Base model class which has created and updated fields for generating timestamps """

  class Meta:
    abstract = True

  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)