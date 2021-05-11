import pytest
from django.test import TestCase
from django.utils import timezone

from todos.models import Todo

today = timezone.now()
# https://devcenter.heroku.com/articles/heroku-redis#upgrading-a-heroku-redis-version
# Create your tests here.
# def test_versioning():
#     first_check = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
#     second_check = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
#     assert True == True
pytestmark = pytest.mark.django_db


class TestTodo(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Todo.objects.create(
            title="ITM304",
            content="Quiz 6 SQL, Database Redesign",
            date_due=timezone.now() - timezone.timedelta(days=1),
            completed=True,
        )
        Todo.objects.create(
            title="ITM304",
            content="Week 9 Problem Set",
            date_due=today + timezone.timedelta(days=1),
            completed=True,
        )
        Todo.objects.create(
            title="ITM304",
            content="Week 9 Problem Set",
            date_due=today + timezone.timedelta(days=0),
            completed=True,
        )
        cls.todos = Todo.objects.all()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_first_task_title(self):
        assert self.todos[0].title == "ITM304"

    def test_is_overdue_true(self):
        assert self.todos[0].is_overdue == True

    def test_is_overdue_false(self):
        assert self.todos[1].is_overdue == False

    def test_is_due_true(self):
        assert self.todos[2].is_due == True

    def test_is_due_false(self):
        assert self.todos[0].is_due == False
