from subprocess import run
from sys import executable
from importlib import import_module

needs_install = [
    "psycopg2",
    "psycopg3",
    "lark",
    "coverage",
    "pytest-cov",
    "'coverage[toml]'",
    "'celery[eventlet,msgpack,librabbitmq,redis,gevent]'",
]


def is_celery_installed():
    try:
        import_module("celery")
    except ModuleNotFoundError:
        needs_install.append(
            "celery",
        )


def is_dropbox_installed():
    try:
        import_module("dropbox")
    except ModuleNotFoundError:
        needs_install.append(
            "dropbox",
        )


def is_django_heroku_installed():
    try:
        import_module("django_heroku")
    except ModuleNotFoundError:
        needs_install.append(
            "django-heroku",
        )


def is_isort_installed():
    try:
        import_module("isort")
    except ModuleNotFoundError:
        needs_install.append(
            "isort",
        )


def is_channels_redis_installed():
    try:
        import_module("channels_redis")
    except ModuleNotFoundError:
        needs_install.append(
            "channels-redis",
        )


def is_channels_installed():
    try:
        import_module("channels")
    except ModuleNotFoundError:
        needs_install.append(
            "channels",
        )


def is_pyjwt_installed():
    try:
        import_module("jwt")
    except ModuleNotFoundError:
        needs_install.append(
            "pyjwt",
        )


def is_beatserver_installed():
    try:
        import_module("beatserver")
    except ModuleNotFoundError:
        needs_install.append(
            "beatserver",
        )


def is_whitenoise_installed():
    try:
        import_module("whitenoise")
    except ModuleNotFoundError:
        needs_install.append(
            "whitenoise",
        )


def is_pillow_installed():
    try:
        import_module("PIL")
    except ModuleNotFoundError:
        needs_install.append(
            "pillow",
        )


def is_python_dotenv_installed():
    try:
        import_module("dotenv")
    except ModuleNotFoundError:
        needs_install.append(
            "python-dotenv",
        )


def is_django_installed():
    try:
        import_module("django")
    except ModuleNotFoundError:
        needs_install.append(
            "django",
        )


def is_djoser_installed():
    try:
        import_module("djoser")
    except ModuleNotFoundError:
        needs_install.append(
            "djoser",
        )


def is_gunicorn_installed():
    try:
        import_module("gunicorn")
    except ModuleNotFoundError:
        needs_install.append(
            "gunicorn",
        )


def is_django_cors_headers_installed():
    try:
        import_module("corsheaders")
    except ModuleNotFoundError:
        needs_install.append(
            "django-cors-headers",
        )


def is_djangorestframework_installed():
    try:
        import_module("rest_framework")
    except ModuleNotFoundError:
        needs_install.append(
            "djangorestframework",
        )


def is_cuid_installed():
    try:
        import_module("cuid")
    except ModuleNotFoundError:
        needs_install.append(
            "cuid",
        )


def is_django_crispy_forms_installed():
    try:
        import_module("crispy_forms")
    except ModuleNotFoundError:
        needs_install.append(
            "django-crispy-forms",
        )


def is_pytest_installed():
    try:
        import_module("pytest")
    except ModuleNotFoundError:
        needs_install.append("pytest")


def is_pytest_asyncio_installed():
    try:
        import_module("pytest_asyncio")
    except ModuleNotFoundError:
        needs_install.append("pytest-asyncio")


def is_pytest_emoji_installed():
    try:
        import_module("pytest_emoji")
    except ModuleNotFoundError:
        needs_install.append("pytest-emoji")


def is_pytest_clarity_installed():
    try:
        import_module("pytest_clarity")
    except ModuleNotFoundError:
        needs_install.append(
            "pytest-clarity",
        )


def is_psycopg_installed():
    try:
        import_module("psycopg")
    except ModuleNotFoundError:
        needs_install.append("psycopg2")


def check_package_installation():
    return [
        is_dropbox_installed(),
        is_django_heroku_installed(),
        is_isort_installed(),
        is_channels_redis_installed(),
        is_channels_installed(),
        is_pyjwt_installed(),
        is_beatserver_installed(),
        is_whitenoise_installed(),
        is_pillow_installed(),
        is_python_dotenv_installed(),
        is_django_installed(),
        is_djoser_installed(),
        is_gunicorn_installed(),
        is_django_cors_headers_installed(),
        is_djangorestframework_installed(),
        is_cuid_installed(),
        is_django_crispy_forms_installed(),
        is_pytest_clarity_installed(),
        is_psycopg_installed(),
        is_pytest_installed(),
        is_pytest_asyncio_installed(),
        is_pytest_emoji_installed(),
        is_celery_installed(),
    ]


packages = check_package_installation()


def install_missing_packages():
    if len(packages) < 1:
        installation = [
            executable,
            "-m",
            "pip",
            "install",
        ] + needs_install
        run(installation)
    return "installation check completed"


# python3-dev gcc libpq-dev
# check doesn't return error code pg_config
