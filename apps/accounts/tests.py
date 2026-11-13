from django.test import TestCase
from django.urls import reverse
from .models import User

class AccountModelTests(TestCase):
    def test_user_role_default(self):
        user = User.objects.create_user(username="student1", password="test-pass-123")
        self.assertEqual(user.role, User.Role.STUDENT)
