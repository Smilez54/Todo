from django.contrib.auth.views import LogoutView
from django.test import TestCase
from django.urls import reverse, resolve
from todo.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage


class TestUrls(TestCase):

    def test_list_url(self):
        path = reverse('tasks')
        self.assertEquals(resolve(path).func.view_class, TaskList)

    def test_detail_url(self):
        url = reverse('task', args=[20])
        self.assertEquals(resolve(url).func.view_class, TaskDetail)

    def test_create_url(self):
        url = reverse('task-create')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)

    def test_update_url(self):
        url = reverse('task-update', args=[2])
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)

    def test_delete_url(self):
        url = reverse('task-delete', args=[20])
        self.assertEquals(resolve(url).func.view_class, TaskDelete)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterPage)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)
