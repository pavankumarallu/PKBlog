

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y7m&mx$vnpv7dhb@nu(=_#9n758o9*tl08skqd_!j*x)#z6d)4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.sites',
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

ROOT_URLCONF = 'PKBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PKBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CKEDITOR_UPLOAD_PATH = "blog/uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_THUMBNAIL_SIZE = (200, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = True
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]),
    },
}

# CUSTOM_TOOLBAR = [
    # {
        # "name": "document",
        # "items": [
            # "Styles", "Format", "Bold", "Italic", "Underline", "Strike", "-",
            # "TextColor", "BGColor",  "-",
            # "JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock",
        # ],
    # },
    # {
        # "name": "widgets",
        # "items": [
            # "Undo", "Redo", "-",
            # "NumberedList", "BulletedList", "-",
            # "Outdent", "Indent", "-",
            # "Link", "Unlink", "-",
            # "Image", "CodeSnippet", "Table", "HorizontalRule", "Smiley", "SpecialChar", "-",
        # ],
    # },
# ]
# 
# CKEDITOR_CONFIGS = {
    # "default": DEFAULT_CONFIG,
    # "my-custom-toolbar": {
        # "skin": "moono-lisa",
        # "toolbar": 'special',
        # "toolbarGroups": None,
        # "extraPlugins": ",".join(["image2", "codesnippet"]),
        # "removePlugins": ",".join(["image"]),
        # "codeSnippet_theme": "xcode",
    # },
# }
# 
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'