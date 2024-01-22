import unittest

from django.urls import reverse
from django.test import TestCase, Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/home.html')
        self.assertTemplateUsed(response, 'adopter/Base.html')

    def test_admin_GET(self):
        response = self.client.get(reverse('admin_page'))
        self.assertEqual(response.status_code, 302)

