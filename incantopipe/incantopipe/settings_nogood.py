# settings.py
import os
from pathlib import Path
import environ

# Inizializza environ
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'store',
    'cart',
    'orders',
    'payment',
    # Third party
    'crispy_forms',
    'crispy_bootstrap5',
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
# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='2.24.0.173'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# STATIC & MEDIA
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CRISPY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# PAYPAL SETTINGS
PAYPAL_CLIENT_ID = env('PAYPAL_CLIENT_ID')
PAYPAL_SECRET = env('PAYPAL_SECRET')
PAYPAL_MODE = env('PAYPAL_MODE', default='sandbox')  # 'live' per produzione

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')