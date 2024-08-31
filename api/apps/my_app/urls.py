# apps/my_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SatelliteImageViewSet, DetectionResultViewSet, start_auth, oauth2callback, get_poaching_risk, home_view

# auth stuff
from django.urls import path
from .views import oauth2callback, get_poaching_risk

router = DefaultRouter()
router.register(r'images', SatelliteImageViewSet)
router.register(r'results', DetectionResultViewSet)

urlpatterns = [

    path('', home_view, name='home'),  # Home view
    path('start/', start_auth, name='start_auth'),  # Start OAuth2 flow
    path('oauth2callback/', oauth2callback, name='oauth2callback'), #OAuth callback
    path('poaching-risk/', get_poaching_risk, name='get_poaching_risk'), # Poaching risk endpoint
    path('', include(router.urls)), # other endpoints
]
