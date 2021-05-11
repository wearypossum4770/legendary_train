from pathlib import Path

import pytest
from django.conf import settings
from django.test import TestCase

from users.models import Profile

# pytestmarks = pytest.mark.django_db
# class TestProfile(TestCase):
#     # fixtures = ["partial_users.json"]
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.profiles = Profile.objects.all()

#     @classmethod
#     def tearDownClass(cls):
#         super().tearDownClass()

#     def test_profiles(self):
#         assert len(self.profiles) > 0


# def test_image_open():
