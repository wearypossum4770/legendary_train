import importlib

import pytest
from django.test import TestCase


def channels_import():
    channels = importlib.import_module("channels")
    major, minor, patch = [int(val) for val in channels.__version__.split(".")]
    return {"major": major, "minor": minor, "patch": patch}


channels = channels_import()


def test_channels_installation_major():
    assert channels.get("major") >= 2


def test_channels_installation_minor():
    assert channels.get("minor") >= 0


def test_channels_installation_patch():
    assert channels.get("patch") >= 2
