from flask_wtf import FlaskForm


class BaseForm(FlaskForm):
  FIELDS = []

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # Remove any fields which are not in the FIELDS list
    if self.FIELDS:
      for f in set(self._fields) - set(self.FIELDS):
        del self[f]

  def get_errors(self):
    """ Returns any form errors as a dictionary but ensures that each field's
    error message is a string and not a list
    """
    errors = self.errors

    for k in errors:
      if isinstance(errors[k], list):
        errors[k] = errors[k][0]

    return errors

  def add_validators(self, field, *args):
    """ Adds validators to an existing field by name """
    f = getattr(self, field)
    f.validators = [*args] + f.validators

  def set_validators(self, field, *args):
    """ Sets the validators to an existing field by name. This overwrites any
    existing validators
    """
    f = getattr(self, field)
    f.validators = [*args]

  def clear_validators(self, field):
    """ Clears any existing validators on a field by name """
    f = getattr(self, field)
    f.validators = []

  def populate_obj(self, obj, exclude=None, only=None):
    """ Populates an object with the form's data. Also accepts a list of
    fields to exclude or a list of fields to only populate with
    """
    if exclude and only:
      raise AttributeError("`exclude` and `only` are mutually exclusive")

    if exclude:
      for name, field in self._fields.items():
        if name not in exclude:
          field.populate_obj(obj, name)
    elif only:
      for name, field in self._fields.items():
        if name in only:
          field.populate_obj(obj, name)
    else:
      super().populate_obj(obj)
