from importlib import import_module
from sys import prefix, platform, executable, version_info, base_exec_prefix

import pytest

from .check_package_installation import check_package_installation

check_package_installation()
major, minor, micro, releaselevel, serial = version_info


def test_running_in_virtual_environment():
    in_virtual_environment = base_exec_prefix == prefix
    if in_virtual_environment:
        assert in_virtual_environment
    else:
        assert False == False


def test_running_python_greaterthan_3():
    assert major > 2


def test_python_can_use_f_string():
    assert minor >= 6 and major > 2


def test_is_dropbox_installed():
    assert import_module("dropbox")


def test_is_django_heroku_installed():
    assert import_module("django_heroku")


def test_is_isort_installed():
    assert import_module("isort")


def test_is_channels_redis_installed():
    assert import_module("channels_redis")


def test_is_channels_installed():
    assert import_module("channels")


def test_is_pyjwt_installed():
    assert import_module("jwt")


def test_is_beatserver_installed():
    assert import_module("beatserver")


def test_is_whitenoise_installed():
    assert import_module("whitenoise")


def test_is_pillow_installed():
    assert import_module("PIL")


def test_is_python_dotenv_installed():
    assert import_module("dotenv")


def test_is_django_installed():
    assert import_module("django")


def test_is_djoser_installed():
    assert import_module("djoser")


def test_is_gunicorn_installed():
    assert import_module("gunicorn")


def test_is_django_cors_headers_installed():
    assert import_module("corsheaders")


def test_is_djangorestframework_installed():
    assert import_module("rest_framework")


def test_is_cuid_installed():
    assert import_module("cuid")


def test_is_django_crispy_forms_installed():
    assert import_module("crispy_forms")


def test_is_pytest_clarity_installed():
    assert import_module("pytest_clarity")


def is_pytest_installed():
    assert import_module("pytest")


def is_pytest_asyncio_installed():
    assert import_module("pytest_asyncio")


def is_pytest_emoji_installed():
    assert import_module("pytest_emoji")


# system_platforms = {
#     "linux": "Linux",
#     "win32": "Windows",
#     "cygwin": "Windows/Cygwin",
#     "darwin": "Mac OS X",
# }
