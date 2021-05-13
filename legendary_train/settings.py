from os import getenv
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

# =================================================================================
# SETUP FILES
# =================================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(find_dotenv())
DEBUG = getenv("DEBUG", True)
SECRET_KEY = getenv(
    "SECRET_KEY", "django-insecure-s^*$we@&db#iit&#l-37umbk-up=2@#tqwle%n62hr&(ojftvi"
)
ALLOWED_HOSTS = []
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
# =================================================================================
# CELERY / TASKS / MAINTENANCE
# =================================================================================
CELERY_BROKER_URL = "amqp://localhost"
CELERY_RESULT_BACKEND = "rpc://"
CELERY_RESULT_PERSISTENT = True
# =================================================================================
# TESTING SETTINGS
# =================================================================================
DJANGO_TEST_PROCESSES = 4
# =================================================================================
# ADMINISTRATIVE
# =================================================================================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD = getenv("EMAIL_PASS")
# =================================================================================
# APPLICATION
# =================================================================================
# Application definition

THIRD_PARTY_APPS = (
    "djoser",
    "channels",
    "whitenoise",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "crispy_forms",
)
DEVELOPMENT_APPS = (
    "whitenoise.runserver_nostatic",
    #    "django_extensions",
)
PROJECT_APPS = (
    "leads.apps.LeadsConfig",
    "todos.apps.TodosConfig",
    "chat.apps.ChatConfig",
    "users.apps.UsersConfig",
    "blog.apps.BlogConfig",
)
DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)
INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS
if DEBUG:
    INSTALLED_APPS += DEVELOPMENT_APPS
if "channels" in THIRD_PARTY_APPS:
    ASGI_APPLICATION = "legendary_train.asgi.application"
else:
    WSGI_APPLICATION = "legendary_train.wsgi.application"
ROOT_URLCONF = "legendary_train.urls"
PROJECT_SETTINGS = {"defaults": (("HAS_AUTOCOMPLETE", True), ("HAS_TASK_MERGE", False))}
# =================================================================================
# CHANNELS / CHAT / WEBSOCKETS
# =================================================================================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(getenv("REDIS_HOST"), getenv("REDIS_PORT"))],
            # ["unix:///path/to/redis.sock"] # unix domain socket faster than loopback
            #  "symmetric_encryption_keys": [SECRET_KEY],
        },
    },
}
# =================================================================================
# DATABASE / CACHE
# =================================================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "TEST": {
            "NAME": BASE_DIR / "db_test.sqlite3",
        },
    }
}
# =================================================================================
# INTERNATIONALIZATION
# =================================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
# =================================================================================
# REST_FRAMEWORK / API
# =================================================================================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAdminUser",
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}
# CORS_ORIGIN_WHITELIST = ('localhost')
CORS_ALLOW_ALL_ORIGINS = True
# ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_EMAIL_VERIFICATION = "none"
CSRF_COOKIE_NAME = "csrftoken"
# HOST_URL = 'http://127.0.0.1:8000' if DEBUG else 'https://justdjango-chat.herokuapp.com'
# =================================================================================
# SECURITY
# =================================================================================
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
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
# =================================================================================
# TEMPLATES / STATIC FILES / MEDIA FILES
# =================================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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
SITE_ID = 1
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # [BASE_DIR / "build.static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_REDIRECT_URL = "blog-home"
LOGIN_URL = "login"
CRISPY_TEMPLATE_PACK = "bootstrap4"
