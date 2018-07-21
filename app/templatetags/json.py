import json

from django import template
from django.utils.safestring import mark_safe


def dump_to_json(value):
  return mark_safe(json.dumps(value))

register = template.Library()
register.filter("json", dump_to_json)