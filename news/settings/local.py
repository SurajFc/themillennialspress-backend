from .base import *

# Email
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"


ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test",
        "USER": "testuser",
        "PASSWORD": "Admin@123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = "/static/"


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "500/min",
        "user": "1000/min",
        "loginAttempts": "100/hr",
    },
     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
     'PAGE_SIZE':10,
    
}

# cors Settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
