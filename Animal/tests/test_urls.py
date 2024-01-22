import unittest
from django.urls import reverse, resolve
from Animal.views import all_animals, add_Animal, editAnimal, deleteAnimal, Animal_detail


class TestUrls(unittest.TestCase):
    def test_all_animals_url_is_resolved(self):
        url = reverse('Animal:all_animals')
        self.assertEqual(url, '/Animal/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func,
                         all_animals)  # checks if the url pattern resolved to the right view function

    def test_add_Animal_url_is_resolved(self):
        url = reverse('Animal:add_Animal')
        self.assertEqual(url, '/Animal/add_Animal/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, add_Animal)  # checks if the url pattern resolved to the right view function

    def test_editAnimal_url_is_resolved(self):
        url = reverse('Animal:editAnimal', args=[8])
        self.assertEqual(url, '/Animal/editAnimal/8')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, editAnimal)  # checks if the url pattern resolved to the right view function

    def test_add_Animal_url_is_resolved(self):
        url = reverse('Animal:deleteAnimal', args=[8])
        self.assertEqual(url, '/Animal/deleteAnimal/8')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func,
                         deleteAnimal)  # checks if the url pattern resolved to the right view function

    def test_Animal_detail_url_is_resolved(self):
        url = reverse('Animal:animal_detail', args=[8])
        self.assertEqual(url, '/Animal/animal_detail/8')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func,
                         Animal_detail)  # checks if the url pattern resolved to the right view function
