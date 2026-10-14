from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),

    # Register: POST /auth/users/
    path('auth/', include("djoser.urls")),
    # Login: POST /auth/jwt/create/
    path('auth/', include("djoser.urls.jwt")),
    # Logout: POST /auth/jwt/logout/
    path('auth/jwt/logout/', TokenBlacklistView.as_view()),
]
