import unittest
from Taskboard.forms import TaskForm

class TestForms(unittest.TestCase):

    def test_TaskForm_from_valid_data(self):
        form = TaskForm(data={'date': '2022-1-1',
                              'name': 'Daniel',
                              'text': 'Take Rexie to get vaccinated'})
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_TaskForm_no_Data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())  # form is not valid so false expected
        self.assertEqual(len(form.errors), 3)  # form has 2 required fields

