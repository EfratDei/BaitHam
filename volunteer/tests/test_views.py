from django.urls import reverse, resolve
from django.test import TestCase, Client
from volunteer.models import attendance
from volunteer.views import *
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('volunteer:loginuser')
        self.logout_url = reverse('volunteer:logoutuser')
        self.user = User.objects.create_user(username='testuser', password='password')
        self.attend_url = reverse('volunteer:update')
        self.obj = attendance.objects.create(user = self.user,
                                             date='2021-11-24',
                                             entrance_time='09:00',
                                             leaving_time='12:55')

        return super().setUp()


class AuthTest(BaseTest):

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'volunteer/loginuser.html')

    def test_login_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)  # if login is successful need to get 302
        self.assertTrue(User.objects.filter(username='testuser').exists())  # true if the test user is exist

    def test_cantlogin_with_no_username(self):
        response = self.client.post(self.login_url, {'password': 'vdjkfkv'}, format='text/html')
        self.assertEqual(response.status_code, 200)  # missing field causing to render a page-- code 200
        self.assertNotEqual(response.status_code, 302)

    def test_cantlogin_with_no_password(self):
        response = self.client.post(self.login_url, {'username': 'vjdkfvb'}, format='text/html')
        self.assertEqual(response.status_code, 200)  # missing field causing to render a page-- code 200
        self.assertNotEqual(response.status_code, 302)

    def test_logout_success(self):
        response = self.client.post(self.logout_url, {'username': 'testuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)


class AttendanceTest(BaseTest):

    def test_update_GET(self):
        response = self.client.get(self.attend_url)
        self.assertEqual(response.status_code, 200)

    def test_update_POST_Valid(self):
        attendance_count = attendance.objects.count()
        self.client.post(self.login_url, {'username': 'testuser', 'password': 'password'})
        response = self.client.post(reverse('volunteer:update'), {
                                                                 'date': '2021-11-24',
                                                                 'entrance_time': '09:00',
                                                                 'leaving_time': '12:55'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(attendance.objects.count(), attendance_count + 1)

    def test_update_POST_NOT_Valid(self):
        attendance_count = attendance.objects.count()
        self.client.post(self.login_url, {'username': 'testuser', 'password': 'password'})
        response = self.client.post(reverse('volunteer:update'), {
                                                                 'date': '2021-13-24', # not a valid date
                                                                 'entrance_time': '09:00',
                                                                 'leaving_time': '12:55'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(attendance.objects.count(), attendance_count)
