from django.test import TestCase
from .services import get_summary

class ReportTests(TestCase):
    def test_empty_summary(self):
        data = get_summary()
        self.assertEqual(data["students_total"], 0)
        self.assertEqual(data["grades_total"], 0)
        self.assertIsNone(data["average_grade"])
