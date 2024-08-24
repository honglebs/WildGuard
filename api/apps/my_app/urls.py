# apps/my_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SatelliteImageViewSet, DetectionResultViewSet

# auth stuff
from django.urls import path
from .views import oauth2callback, get_poaching_risk

router = DefaultRouter()
router.register(r'images', SatelliteImageViewSet)
router.register(r'results', DetectionResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2callback/', oauth2callback, name='oauth2callback'),
    path('api/poaching-risk/', get_poaching_risk, name='get_poaching_risk'),
]
