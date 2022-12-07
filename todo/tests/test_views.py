from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Task


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('tasks')
        self.detail_url = reverse('task', args=[2])

    def test_list_Get(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 302)

    def test_detail_Get(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 302)
