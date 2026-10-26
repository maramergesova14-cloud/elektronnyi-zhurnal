from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Student, Subject


class JournalApiTests(APITestCase):
    def test_students_endpoint_returns_empty_list(self):
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_can_create_student(self):
        response = self.client.post(
            "/api/students/",
            {"first_name": "Анна", "last_name": "Иванова", "class_name": "9А", "email": ""},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Student.objects.count(), 1)

    def test_can_create_subject(self):
        response = self.client.post(
            "/api/subjects/",
            {"name": "Математика", "teacher_name": "Иван Петров"},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Subject.objects.count(), 1)
