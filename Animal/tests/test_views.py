from django.urls import reverse
from django.test import TestCase, Client
from Animal.models import animal, Stats


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = animal.objects.create(
            name='Rex',
            submitter='Afik',
            species='dog',
            breed='Boxer',
            description='very good dog',
            sex='M',
            Adoption='N',
            image='default.png')
        self.stat = Stats.objects.create(created=2, deleted=1, current=1, month=1)

    def test_all_animals_GET(self):
        response = self.client.get(reverse('Animal:all_animals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/all_animals.html')

    def test_Animal_detail_GET(self):
        response = self.client.get(reverse('Animal:animal_detail', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/animal_detail.html')

    def test_add_Animal_GET(self):
        response = self.client.get(reverse('Animal:add_Animal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/add_Animal.html')

    def test_add_Animal_POST_Valid(self):
        animal_count = animal.objects.count()
        response = self.client.post(reverse('Animal:add_Animal'), {'name': 'Rex',
                                                                   'submitter': 'Afik',
                                                                   'species': 'dog',
                                                                   'submission_date': '2021-8-8',
                                                                   'breed': 'Boxer',
                                                                   'description': 'very good dog',
                                                                   'sex': 'M',
                                                                   'Adoption': 'N',
                                                                   'image': 'default.png'})

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count + 1)  # object created so expected true

    def test_add_Animal_POST_Not_Valid(self):
        response = self.client.post(reverse('Animal:add_Animal'),
                                    {'name': '',
                                     'submitter': '',
                                     'species': 'Dog',
                                     'breed': '',
                                     'description': '',
                                     'sex': 'M',
                                     'Adoption': 'N',
                                     'image': ''})
        self.assertEqual(response.status_code, 200)  # means redirection works in case of a bad form

    def test_edit_Animal_GET(self):
        response = self.client.get(reverse('Animal:editAnimal', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/add_Animal.html')

    def test_edit_Animal_POST(self):
        response = self.client.post(reverse('Animal:editAnimal', args=[self.obj.pk]), {'name': 'Rex',
                                                                                       'submitter': 'Afik',
                                                                                       'species': 'dog',
                                                                                       'breed': 'Boxer',
                                                                                       'submission_date': '2021-8-8',
                                                                                       'description': 'very good dog',
                                                                                       'sex': 'M',
                                                                                       'Adoption': 'Y',
                                                                                       'image': 'default.png'})

        self.assertEqual(response.status_code, 302)  # means redirection works

    def test_delete_Animal_GET(self):
        response = self.client.get(reverse('Animal:deleteAnimal', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/DeleteAnimal.html')

    def test_delete_Animal_POST(self):
        animal_count = animal.objects.count()
        response = self.client.post(reverse('Animal:deleteAnimal', args=[self.obj.pk]))

        self.assertFalse(animal.objects.filter(pk=self.obj.pk).exists())
        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count - 1)  # -1 the number that been before
