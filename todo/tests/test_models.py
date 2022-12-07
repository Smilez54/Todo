from django.test import TestCase
from todo.models import Task


class TestModels(TestCase):

    def setUp(self):
        task1 = Task.objects.create(
            title='Grade the garden',
            description='Just get things tidy up',
            complete=True
        )

    def test_string_method(self):
        user = Task.objects.get(id=1)
        expected_string = user.title
        self.assertEquals(str(user), expected_string)