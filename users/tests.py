from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ProtectedAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_protected_route_requires_authentication(self):
        url = '/api/users/protected/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_protected_route_with_token(self):
        url = '/api/users/protected/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'You are authenticated!')

