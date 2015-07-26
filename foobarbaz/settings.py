
"""
Django settings for foobarbaz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '76z*3h7a3^2%lhcr90sucwn0dxuiv28j0li7&9ryuh'

# Set the login Redirect URL
LOGIN_URL = '/login'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'foobarbaz',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'foobarbaz.urls'

WSGI_APPLICATION = 'foobarbaz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
from os import environ
from urlparse import urlparse

# Parse database configuration from 
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    #'django.template.loaders.filesystem.load_template_source',
    #'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# please replace "<sendgrid_username>" and "<sendgrid_password>" with your SendGrid credentials
SENDGRID_USERNAME = 'bmjen';
SENDGRID_PASSWORD = 'sEndgr1d4mE';

EMAIL_HOST = 'smtp.sendgrid.net'
##TO-DO: Pull these from environment variables or a config file
EMAIL_HOST_USER = 'bmjen'
EMAIL_HOST_PASSWORD = 'sEndgr1d4mE'
######
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'admin@foobar.baz'
