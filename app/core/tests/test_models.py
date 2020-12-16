# Import TestCase
from django.test import TestCase
# Import library that checks user model
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        # First we create variables to use for the test
        email = 'test@undeinveti.ro'
        password = 'Testpass123'
        # then we use get_user_model, we use the objects method and then
        # the "create_user" function, where we pass the previously
        # created email and passwords to create a new user
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # We use the assertEqual to check the email of the newly
        # created object
        self.assertEqual(user.email, email)
        # We use the assertTrue as the password is encrypted
        # so we use the method check_password that takes the password
        # as an argument
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@UNdeInvETI.ro'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@undeinveti.ro',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
