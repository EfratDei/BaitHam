import unittest
from volunteer.forms import AttendanceForm


class TestForms(unittest.TestCase):
    def test_Attendance_Form_valid_Data(self):
        form = AttendanceForm(data=
                         {'date': '2020-12-12',
                          'entrance_time': '11:00',
                          'leaving_time': '16:30',})
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_Attendance_Form_no_Data(self):
        form = AttendanceForm(data={})
        self.assertFalse(form.is_valid())  # form is not valid, so false expected
        self.assertEqual(len(form.errors), 3)
