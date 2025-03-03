from django.urls import path
from accounts.views import RegistrationView, LoginView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/register/', RegistrationView.as_view(), name='register'),
]
