"""
Django settings for jxc project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = os.getenv("ENV", "DEFAULT")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&l@!!)mx@_9f3_1wa()lc1ugt3&i5vbcl_(h094h1roq_*9uq9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "INFO")

# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'customers.apps.CustomersConfig',
    'repos.apps.ReposConfig',
    'tickets.apps.TicketsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.exception_middleware.ExceptionReportMiddleware',
    'utils.request_parse_middleware.RequestBodyMiddleware',
    'utils.users_auth_middleware.UsersAuthMiddleWare',
]

ROOT_URLCONF = 'jxc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jxc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(filename)s %(lineno)d %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'access': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'filename': '/var/log/dec_server/dec.log',
            'formatter': 'verbose',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',  # this specifies the interval
            'interval': 7,  # defaults to 1, only necessary for other values
            'backupCount': 10,  # how many backup file to keep, 10 days
        },
        'console': {
            'level': LOGGING_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
        'access_file': {
            'filename': '/var/log/dec_server/access.log',
            'formatter': 'access',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',  # this specifies the interval
            'interval': 7,  # defaults to 1, only necessary for other values
            'backupCount': 10,  # how many backup file to keep, 10 days
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': LOGGING_LEVEL,
            'propagate': True,
        },
        'access': {
            'handlers': ['access_file', ],
            'level': LOGGING_LEVEL,
            'propagate': False,
        }
    },
}

if os.environ.get("CONSOLE_LOG_ONLY"):
    LOGGING["handlers"]["access_file"] = LOGGING["handlers"]["console"]
    LOGGING["handlers"]["file"] = LOGGING["handlers"]["console"]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 86400

DEFAULT_DB_HOST = os.getenv('DEFAULT_DB_HOST')
DEFAULT_DB_PORT = os.getenv('DEFAULT_DB_PORT')
DEFAULT_DB_USERNAME = os.getenv('DEFAULT_DB_USERNAME')
DEFAULT_DB_PASSWORD = os.getenv('DEFAULT_DB_PASSWORD')
DEFAULT_DB_NAME = os.getenv('DEFAULT_DB_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': DEFAULT_DB_HOST,
        'PORT': DEFAULT_DB_PORT,
        'NAME': DEFAULT_DB_NAME,
        'USER': DEFAULT_DB_USERNAME,
        'PASSWORD': DEFAULT_DB_PASSWORD,
        'CONN_MAX_AGE': 3000,
        'RECYCLE_TIME': 3000,
    }
}

if ENV == "LOCAL":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
