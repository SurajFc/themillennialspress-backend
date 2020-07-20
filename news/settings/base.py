import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = "d8j!r@k)u9#vx95op=y)%ogm*tr3a4x4s^x!2*v6p_%i&5f^b1"

DEBUG = True


# Application definition
LOCAL_APPS = (
    "users",
    "superadmin",
    "articles",
)

THIRD_PARTY_APPS = (
    "rest_framework",  # rest framework
    "rest_framework.authtoken",  # rest framework auth token
    "corsheaders",  # Cors
    "image_optimizer",  # image optimizer
   'django_cleanup.apps.CleanupConfig', #cleaning unused images (Always in last)

)

INSTALLED_APPS = (
    (
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.staticfiles",
    )
    + LOCAL_APPS
    + THIRD_PARTY_APPS
)


# MiddleWares
OTHER_MIDDLEWARES = [
    "corsheaders.middleware.CorsMiddleware",  # cors
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "news.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "news.wsgi.application"
AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o644


# To use Pillow (image optimizer)
OPTIMIZED_IMAGE_METHOD = "pillow"
