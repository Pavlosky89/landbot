from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('username', 'name', 'test@test.com', '123456789', 'password')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.name, 'name')
        self.assertEqual(super_user.email, 'test@test.com')
        self.assertEqual(super_user.phone, '123456789')
        self.assertEqual(super_user.password, 'password')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)

        # Test is_staff field
        with self.assertRaises(ValueError):
            db.objects.create_superuser('username', 'name', 'test@test.com', '123456789', 'password', is_staff=False)
        # Test is_superuser
        with self.assertRaises(ValueError):
            db.objects.create_superuser('username', 'name', 'test@test.com', '123456789', 'password', is_superuser=False)

    def test_create_user(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('username2', 'name2', 'test2@test.com', '123456789', 'password')
        self.assertEqual(super_user.username, 'username2')
        self.assertEqual(super_user.name, 'name2')
        self.assertEqual(super_user.email, 'test2@test.com')
        self.assertEqual(super_user.phone, '123456789')
        self.assertEqual(super_user.password, 'password')
        self.assertFalse(super_user.is_superuser)
        self.assertFalse(super_user.is_staff)
        self.assertFalse(super_user.is_active)

        # Test with no name
        with self.assertRaises(ValueError):
            db.objects.create_superuser('username', '', 'test2@test.com', '123456789', 'password',
                                        is_superuser=False)
        # Test with no email
        with self.assertRaises(ValueError):
            db.objects.create_superuser('username', 'name', '', '123456789', 'password',
                                        is_superuser=False)
