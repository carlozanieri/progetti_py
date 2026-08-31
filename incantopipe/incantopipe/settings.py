# settings.py

import os
from pathlib import Path
import environ

# Inizializza environ
env = environ.Env(
    DEBUG=(bool, False)
)

# Leggi il file .env
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', default=False)

# ALLOWED HOSTS - Domini consentiti
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[
    'incantopipe.it',
    'www.incantopipe.it',
    'localhost',
    '127.0.0.1',
])

# CSRF Settings
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[
    'https://incantopipe.it',
    'https://www.incantopipe.it',
    'http://incantopipe.it',
    'http://www.incantopipe.it',
])

# Security Settings per produzione
if not DEBUG:
    # RIMUOVI SECURE_SSL_REDIRECT - Nginx gestisce il redirect HTTP->HTTPS
    # SECURE_SSL_REDIRECT = True  # COMMENTA QUESTA RIGA
    
    # Queste impostazioni vanno bene
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 31536000  # 1 anno
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
else:
    # SESSION_COOKIE_SECURE = False  # Non necessario in sviluppo
    # CSRF_COOKIE_SECURE = False  # Non necessario in sviluppo
    pass

# APPLICATIONS - Solo app, NON middleware
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'accounts',
    'store',
    'cart',
    'orders',
    'payment',
    # Third party
    'crispy_forms',
    'crispy_bootstrap5',
]

# MIDDLEWARE - I middleware vanno qui
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'incantopipe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Aggiungi questa riga
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

WSGI_APPLICATION = 'incantopipe.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'it-it'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_TZ = True

# STATIC & MEDIA

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CRISPY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# PAYPAL SETTINGS
PAYPAL_CLIENT_ID = env('PAYPAL_CLIENT_ID', default='')
PAYPAL_SECRET = env('PAYPAL_SECRET', default='')
PAYPAL_MODE = env('PAYPAL_MODE', default='sandbox')

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Per sviluppo
# Per produzione usa SMTP:
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
# EMAIL_PORT = env('EMAIL_PORT', default=587)
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

# Login/Logout URLs
LOGIN_REDIRECT_URL = 'store:product_list'
LOGOUT_REDIRECT_URL = 'store:product_list'
LOGIN_URL = 'login'