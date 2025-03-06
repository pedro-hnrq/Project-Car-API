from django.test import TestCase
from accounts.models import User
from accounts.serializers import LoginSerializer, RegistrationSerializer, CustomTokenRefreshSerializer, CustomTokenVerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


class SerializerTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            first_name='Test',
            last_name='User'
        )

    def test_login_serializer(self):
        serializer = LoginSerializer(data={'email': 'test@example.com', 'password': 'testpassword'})
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertIn('access_token', validated_data)
        self.assertIn('refresh_token', validated_data)
        self.assertIn('user', validated_data)
        self.assertEqual(validated_data['user']['email'], 'test@example.com')

    def test_login_serializer_invalid_credentials(self):
        serializer = LoginSerializer(data={'email': 'test@example.com', 'password': 'wrongpassword'})
        with self.assertRaises(AuthenticationFailed):
            serializer.is_valid(raise_exception=True)

    def test_registration_serializer(self):
        data = {
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'first_name': 'New',
            'last_name': 'User'
        }
        serializer = RegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, 'newuser@example.com')
        self.assertTrue(user.check_password('newpassword'))

    def test_custom_token_refresh_serializer(self):
        refresh = RefreshToken.for_user(self.user)
        serializer = CustomTokenRefreshSerializer(data={'refresh': str(refresh)})
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertIn('access_token', validated_data)

    def test_custom_token_verify_serializer_valid(self):
        refresh = RefreshToken.for_user(self.user)
        access = refresh.access_token
        serializer = CustomTokenVerifySerializer(data={'token': str(access)})
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertEqual(validated_data['message'], 'Token Válido')

    def test_custom_token_verify_serializer_invalid(self):
        serializer = CustomTokenVerifySerializer(data={'token': 'invalid_token'})
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data
        self.assertEqual(validated_data['message'], 'Token Inválido')
        self.assertIn('error', validated_data)

    def test_custom_token_refresh_serializer_no_refresh(self):
        serializer = CustomTokenRefreshSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_custom_token_verify_serializer_no_token(self):
        serializer = CustomTokenVerifySerializer(data={})
        self.assertFalse(serializer.is_valid())
