from flask import Blueprint

from .user import blueprint as user_bp


blueprints = (
  user_bp,
)

for b in blueprints:
  b.url_prefix = "/api" + b.url_prefix