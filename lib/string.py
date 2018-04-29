import re


def snake_case(s):
  """ Converts a CamelCase string into snake_case

  Credit: https://stackoverflow.com/a/1176023/2896976
  """
  s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
  return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()