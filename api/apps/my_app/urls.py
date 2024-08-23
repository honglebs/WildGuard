# apps/my_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SatelliteImageViewSet, DetectionResultViewSet

router = DefaultRouter()
router.register(r'images', SatelliteImageViewSet)
router.register(r'results', DetectionResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
