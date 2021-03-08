from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_succesful(self):
        """test creating user with E_mail"""
        email = "testing@testing.com"
        password = "Testing@123456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normal(self):
        """test if E_mail is not case sensetive"""
        email = "testing@TESTING.COM"
        user = get_user_model().objects.create_user(email, 'testing123456')

        self.assertEqual(user.email, email.lower())

    def test_valid_email(self):
        """Raise error if no email is provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testing123456")

    def test_creating_super_user(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            "testing@TESTING.COM",
            "testing123456"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
