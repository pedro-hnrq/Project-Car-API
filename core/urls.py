from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth Token JWT
    path('api/', include('accounts.urls')),

    # Endpoint
    path('api/v2/', include('cars.urls')),
    path('api-auth/', include('rest_framework.urls')),


    # JWT
    # path('api/v2/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v2/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v2/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
