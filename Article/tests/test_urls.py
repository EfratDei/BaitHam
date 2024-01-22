import unittest
from django.urls import reverse, resolve
from Article.views import all_articles


class TestUrls(unittest.TestCase):
    def test_all_articles_url_is_resolved(self):
        url = reverse('Article:articles')
        self.assertEqual(url, '/Article/articles/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func,all_articles)  # checks if the url pattern resolved to the right view function


