from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
