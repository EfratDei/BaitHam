from django.urls import reverse
from django.test import TestCase, Client
from Article.models import articles


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = articles.objects.create(id=1,
                                           name='food for dogs',
                                            text = 'dogs eat bones',
                                            type ='dog',
                                            link='https://www.ynet.co.il/articles/0,7340,L-5378553,00.html',
                                            genre = 'information')

    def test_all_articles_GET(self):
        response = self.client.get(reverse('Article:articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Article/articles.html')

