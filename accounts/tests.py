from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsTestCase(TestCase):
    def test_create_employee(self):
        user = User.objects.create_user(
            username="testemp",
            email="emp@test.com",
            password="test123",
            role="employee"
        )
        self.assertEqual(user.role, "employee")
        self.assertTrue(hasattr(user, "employee_profile"))