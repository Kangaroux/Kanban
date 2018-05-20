import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "fy^pkvgi7e62&#8+2e0jq=e3%!$3)(5(&tkf*^r7d)5kyx0$pq"
DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

AUTH_USER_MODEL = "user.User"

INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",

  "app",
  "project",
  "user",
]

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
      ],
    },
  },
]

PASSWORD_HASHERS = [
  "django.contrib.auth.hashers.Argon2PasswordHasher",
]

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
  }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "build")
]
STATIC_URL = "/static/"
