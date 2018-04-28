import os

PROD = bool(os.environ.get("PROD", False))
DEVELOPMENT = not PROD