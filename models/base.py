from datetime import datetime

from sqlalchemy import inspect

from config.app import db
from lib import response_codes as http
from lib.response import ErrorResponse


class BaseModel:
  """ Base model class which includes some common fields """

  # A list of field names which never appear when serializing
  PRIVATE_FIELDS = []

  id = db.Column(db.Integer, primary_key=True)
  created = db.Column(db.DateTime, default=datetime.now)
  updated = db.Column(db.DateTime, onupdate=datetime.now, nullable=True)


  @classmethod
  def get_fields(cls):
    """ Returns a list of all the column names in the model """
    try:
      return cls.fields
    except AttributeError:
      cls.fields = set(col.key for col in inspect(cls).attrs)
      return cls.fields

  @classmethod
  def get_or_404(cls, pk, msg=None):
    obj = cls.query.get(pk)

    if not msg:
      msg = "%s does not exist." % cls.__name__

    if not obj:
      raise ErrorResponse(msg=msg, code=http.NOT_FOUND)

    return obj

  def serialize(self, exclude=None, only=None):
    """ Serializes the model into a dict. Also accepts a list of fields to
    exclude or a list of fields to only serialize. Field names that are listed
    in the model's `excluded` attribute are never included

    This method is intended for exporting the user data.
    For importing, see: `forms.base.BaseForm.populate_obj`
    """
    if exclude and only:
      raise AttributeError("`exclude` and `only` are mutually exclusive")

    fields = self.get_fields() - set(self.PRIVATE_FIELDS)

    # Filter out any fields we don't want
    if exclude:
      fields -= set(exclude)
    elif only:
      fields &= set(only)

    data = {}

    # Serialize the fields. Nearly every field type is good to use out of the box
    # but some (like datetime objects) need to be converted
    for f in fields:
      val = getattr(self, f)

      if isinstance(val, datetime):
        val = val.isoformat()

      data[f] = val

    return data