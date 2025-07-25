from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # Redirect root URL to signup page
    path('', RedirectView.as_view(url='signup/', permanent=False)),
    
    # Admin and API endpoints
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include authentication URLs
    path('', include('Authentication.urls')),
]
