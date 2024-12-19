from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTestCase(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.list_users_url = reverse('list_all_users')

        # Create users for testing
        User.objects.create_user(
            first_name="Test One", last_name="User", username="testuser1", password="securepassword123", email="testuser1@example.com")
        User.objects.create_user(
            first_name="Test Two", last_name="User", username="testuser2", password="securepassword456", email="testuser2@example.com")
    
    def test_register_user_success(self):
        data = {
            "first_name": "Test One Test",
            "last_name": "Test Test",
            "username": "testuser_test",
            "password": "securepassword123",
            "email": "testusertest@example.com"
        }
        
        response = self.client.post(self.register_url, data, format='json')
        # Log the response data to inspect
        print(f"Response data for user registration: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User created successfully")
        self.assertTrue('password' not in response.data)

    def test_register_user_missing_fields(self):
        data = {
            "first_name": "Test One",
            "username": "testuser"
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_register_user_invalid_email(self):
        data = {
            "first_name": "Test One",
            "last_name": "Test",
            "username": "testuser",
            "password": "securepassword123",
            "email": "invalidemail"
        }

        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_list_all_users(self):
        response = self.client.get(self.list_users_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['username'], "testuser1")
        self.assertEqual(response.data[1]['username'], "testuser2")
