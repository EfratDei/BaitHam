import unittest
from success_story.forms import storyForm

class TestForms(unittest.TestCase):
    def test_story_Form_valid_Data(self):
        form = storyForm(data=
                         {'name': 'story number 1',
                          'date': '2020-12-12',
                          'text': 'this is my success story!'})
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_Story_Form_no_Data(self):
        form = storyForm(data={})
        self.assertFalse(form.is_valid())  # form is not valid, so false expected
        self.assertEqual(len(form.errors), 3)
