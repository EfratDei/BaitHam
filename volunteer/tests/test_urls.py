import unittest
from django.urls import reverse, resolve
from volunteer.views import loginuser,logoutuser,update,export_pdf,export_excel


class TestUrls(unittest.TestCase):
    def test_login_user_url_is_resolved(self):
        url = reverse('volunteer:loginuser')
        self.assertEqual(resolve(url).func, loginuser)

    def test_logout_user_url_is_resolved(self):
        url = reverse('volunteer:logoutuser')
        self.assertEqual(resolve(url).func, logoutuser)

    def test_update_url_is_resolved(self):
        url = reverse('volunteer:update')
        self.assertEqual(resolve(url).func, update)

    def test_export_pdf_url_is_resolved(self):
        url = reverse('volunteer:export_pdf')
        self.assertEqual(resolve(url).func, export_pdf)

    def test_export_excel_url_is_resolved(self):
        url = reverse('volunteer:export_excel')
        self.assertEqual(resolve(url).func, export_excel)