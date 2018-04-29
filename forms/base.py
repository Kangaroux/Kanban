from flask_wtf import FlaskForm


class BaseForm(FlaskForm):
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