from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, RegistrationSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import generics

@extend_schema(tags=['Auth'])
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

@extend_schema(tags=['Auth'])
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    authentication_classes = []  
    permission_classes = [] 