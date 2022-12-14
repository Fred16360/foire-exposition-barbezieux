"""
Django settings for aacore project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dw#@$2d*3rg@)*7gb4zvq02uzn53aj-2n7ajnau_-&@q(q+1$)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['foire-exposition-barbezieux.mister-fred.fr', '127.0.0.1', 'foire-exposition-barbezieux.fr']


# Application definition

INSTALLED_APPS = [
    'sendemail.apps.SendemailConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'google_analytics',
    'captcha',
    'crispy_forms',

    'accueil',
    'actualites',
    'animation',
    'exposant',
    'infosfoire',
    'menus',
    'visiteur',
    'partenaires',
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

ROOT_URLCONF = 'aacore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'aacore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hpeu7818_foire2022',
        'USER': 'hpeu7818_foire2022',
        'PASSWORD': 'E42&B0qdL5+B',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#LOGIN_URL = 'accounts/login/'

#LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#AUTH_USER_MODEL = 'accounts.Account'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

GOOGLE_ANALYTICS = {
    'google_analytics_id': 'UA-496865531-1',
}

# CONFIGURATION ENVOI EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.foire-exposition-barbezieux.fr'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'contact@foire-exposition-barbezieux.fr'
EMAIL_HOST_PASSWORD = '7wW$7M7&EWas'
EMAIL_USE_SSL = True

# CONFIGURATION RECAPTCHA POUR FORMULAIRE
RECAPTCHA_PUBLIC_KEY = '6LfmbzwUAAAAAB-KfwBlS52fxAEBdq3DaFy87iqo'
RECAPTCHA_PRIVATE_KEY = '6LfmbzwUAAAAALdiGnbLjYrGHmAGOjUYe5Qw7voD'
