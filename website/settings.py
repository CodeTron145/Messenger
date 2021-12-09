"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# with(open("FBCreds.txt")) as file:
#     fb = file.read().split(sep=";")

with(open("SK.txt")) as file:
    key = file.read().split(sep=";")[0]

# with(open("DbCreds.txt")) as file:
#     string = file.read().split("\n")
#     db1 = string[0].split(";")
#     db2 = string[1].split(";")

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "social_django",
    "core.apps.CoreConfig",
    # "core, apps.",
    "sslserver",
    'chat',
    'logio',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "website.wsgi.application"
ASGI_APPLICATION = "website.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

DEFAULT_AUTO_FIELD='django.db.models.AutoField'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# if os.getenv("GAE_APPLICATION", None):
#     # Running on production App Engine, so connect to Google Cloud SQL using
#     # the unix socket at /cloudsql/<your-cloudsql-connection string>
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.mysql",
#             "HOST": db1[0],
#             "USER": db1[1],
#             "PASSWORD": db1[2],
#             "NAME": db1[3],
#         }
#     }
# else:
#     # Running locally so connect to either a local MySQL instance or connect to
#     # Cloud SQL via the proxy. To start the proxy via command line:
#     #
#     #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
#     #
#     # See https://cloud.google.com/sql/docs/mysql-connect-proxy
#     DATABASES = {
#         'default': {
#             "ENGINE": "django.db.backends.mysql",
#             "HOST": db2[0],
#             "PORT": db2[1],
#             "NAME": db2[2],
#             "USER": db2[3],
#             "PASSWORD": db2[4],
#         }
#     }

# if os.getenv("TRAMPOLINE_CI", None):
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

# SOCIAL_AUTH_FACEBOOK_KEY = fb[0]
# SOCIAL_AUTH_FACEBOOK_SECRET = fb[1]
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
# SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", "user_link"]
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     "fields": "id, name, email, picture.type(large), link"
# }
# SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
#     ("name", "name"),
#     ("email", "email"),
#     ("picture", "picture"),
#     ("link", "profile_url"),
# ]

SECURE_SSL_REDIRECT = False

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = Path(BASE_DIR / "static")

LOGIN_URL = "start"
LOGOUT_URL = "start"
LOGIN_REDIRECT_URL = "start"
LOGOUT_REDIRECT_URL = "start"