from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.utils.translation import gettext as __


class LoginTests(APITestCase):
    
    def setUp(self):
        self.valid_payload = {
            "username": "testing",
            "password": "12345678"
        }
        
        self.invalid_payload = {
            "username": "invalid_username",
            "password": "invalid_password"
        }
                
        self.user = User.objects.create_user(email="testing@email.com", **self.valid_payload)

    
    def test_get_access_token(self):
        """
        Test if we can get access token.
        """ 
        
        response = self.client.post(reverse('login'), self.valid_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get("access"))
        self.assertTrue(response.data.get("refresh"))
        
    def test_refreash_access_token(self):
        """
        Test access token refresh.
        """ 
        
        refresh = RefreshToken.for_user(self.user)
        
        response = self.client.post(reverse('token_refresh'), {'refresh': str(refresh)}, format='json')
        self.assertTrue(response.data.get("access"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_login_with_invalid_payload(self):
        """
        Test if we can get access token.
        """ 
        
        response = self.client.post(reverse('login'), self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(response.data.get('detail'), __('No active account found with the given credentials'))