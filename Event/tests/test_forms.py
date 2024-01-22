import unittest
from Event.forms import EventForm


class TestForms(unittest.TestCase):
    def test_Event_Form_valid_Data(self):
        form = EventForm(data=
                         {'name': 'event number 2',
                          'date': '2020-12-12',
                          'text': 'wow! this is my event',
                          'image': 'event.png'})
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_Event_Form_no_Data(self):
        form = EventForm(data={})
        self.assertFalse(form.is_valid())  # form is not valid, so false expected
        self.assertEqual(len(form.errors), 2)
