
from pathlib import Path
import os



SECRET_KEY= 'django-insecure-p(c=wdc2c10@^c(y^4@9y6q*=9%8_lp6+=9leqbg4+vi20*p-#'
DEBUG = 'TRUE'

ALLOWED_HOSTS = []
ROOT_URLCONF = 'web_board.urls'
WSGI_APPLICATION = 'web_board.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



