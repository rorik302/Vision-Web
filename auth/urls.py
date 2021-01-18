from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AuthViewSet

router = DefaultRouter()
router.register('', AuthViewSet)

urlpatterns = [
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', AuthViewSet.as_view({'get': 'verification'}), name='verification')
]

urlpatterns += router.urls
