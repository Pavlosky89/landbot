from django.test import TestCase
from django.contrib.auth import get_user_model
# Imports needed for the test case "test_user_registration
from django.urls import reverse
from rest_framework import status
import json


class CustomUserTests(TestCase):

    def test_create_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('username', 'name', 'test@test.com', '123456789', 'password')
        self.assertEqual(super_user.username, 'username')
        self.assertEqual(super_user.name, 'name')
        self.assertEqual(super_user.email, 'test@test.com')
        self.assertEqual(super_user.phone, '123456789')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)

        # Test is_staff field
        with self.assertRaises(ValueError):
            db.objects.create_superuser('username', 'name', 'test@test.com', '123456789', 'password', is_staff=False)
        # Test is_superuser
        with self.assertRaises(ValueError):
            db.objects.create_superuser('username', 'name', 'test@test.com', '123456789', 'password',
                                        is_superuser=False)

    def test_create_user(self):
        db = get_user_model()
        user = db.objects.create_user('username2', 'name2', 'test2@test.com', '123456789', 'password')
        self.assertEqual(user.username, 'username2')
        self.assertEqual(user.name, 'name2')
        self.assertEqual(user.email, 'test2@test.com')
        self.assertEqual(user.phone, '123456789')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        # Test with no name
        with self.assertRaises(ValueError):
            db.objects.create_user('username', '', 'test2@test.com', '123456789', 'password',
                                   is_superuser=False)
        # Test with no email
        with self.assertRaises(ValueError):
            db.objects.create_user('username', 'name', '', '123456789', 'password',
                                   is_superuser=False)

    ''' # Start Redis server before testing this case - It simulates a call to the endpoint "create-user" 
    def test_user_repository(self):
        url = reverse('create_user')

        data = {
            'name': 'landbottest2',
            'email': 'landbottest2@bot.com',
            'phone': 123456789
        }

        response = self.client.post(url,
                                    content_type='application/json',
                                    data=json.dumps(data))

        assert response.status_code == 201
    '''