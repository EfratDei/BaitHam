import unittest
from Animal.forms import Add_Animal_Form


class TestForms(unittest.TestCase):
    def test_Add_Animal_Form_valid_Data(self):
        form = Add_Animal_Form(data={
            'name': 'Rex',
            'submitter': 'Afik',
            'species': 'dog',
            'breed': 'Boxer',
            'description': 'very good dog',
            'sex': 'M',
            'Adoption': 'N',
            'submission_date': '2020-12-12',
            'image': 'default.png'})
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_Add_Animal_Form_no_Data(self):
        form = Add_Animal_Form(data={})
        self.assertFalse(form.is_valid())  # form is not valid so false expected
        self.assertEqual(len(form.errors), 7)  # form has 4 required fields
