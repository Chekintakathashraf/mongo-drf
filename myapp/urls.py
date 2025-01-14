

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserActivityViewSet, UserLogin

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-activities', UserActivityViewSet)

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('', include(router.urls)),
]
