<<<<<<< HEAD
from pathlib import Path

import msgpack
import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from PIL import Image

from users.models import Profile

pytestmarks = pytest.mark.django_db
array = [1, 2, 3]
message = b"\x93\x01\x02\x03"
message_tuple = (1, 2, 3)


def test_python_to_message_pack():
    assert msgpack.dumps(array) == message


def test_python_from_message_unpack():
    assert msgpack.loads(message, use_list=False) == message_tuple


def cleanup_image_testing(__dirname):
    import subprocess

    subprocess.run(["rm", "-rf", Path(__dirname).parent])


class TestImageProcessing(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.temp_dir = "test/profile_pics"
        cls.__dirname = Path(f"{settings.MEDIA_ROOT}/{cls.temp_dir}").mkdir(
            exist_ok=True
        )
        cls.image = f"{settings.MEDIA_ROOT}/default.png"

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cleanup_image_testing(self.temp_dir)


class TestProfile(TestCase):
    # fixtures = ["partial_users.json"]
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.profiles = Profile.objects.all()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_profiles(self):
        assert len(self.profiles) > 0


# def test_image_open():
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> 07b0ff3d47923f9eeeb106dff01ed70b8cf689f5
