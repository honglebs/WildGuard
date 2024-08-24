# views create from after storing in database
from django.shortcuts import render
from rest_framework import viewsets
from .models import SatelliteImage, DetectionResult
from .serializers import SatelliteImageSerializer, DetectionResultSerializer

# redirect for OAuth for credentials to use GEE API
from django.http import HttpResponseRedirect
from django.urls import reverse
from google_auth_oauthlib.flow import Flow
from django.conf import settings

# views for the earth engine 
from django.http import JsonResponse
from wildguard.utils import initialize_earth_engine
import ee

from django.http import HttpResponse

# root view
def home_view(request):
    return HttpResponse("Welcome to the Home Page!")


# views stored as results in the database for detection snf satellite image
class SatelliteImageViewSet(viewsets.ModelViewSet):
    queryset = SatelliteImage.objects.all()
    serializer_class = SatelliteImageSerializer

class DetectionResultViewSet(viewsets.ModelViewSet):
    queryset = DetectionResult.objects.all()
    serializer_class = DetectionResultSerializer

# this is to handle OAuth2 callback where google will redirect the user after
# application is authroized 
def oauth2callback(request):
    flow = Flow.from_client_config({
        "web": {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uris": [settings.GOOGLE_REDIRECT_URI]
        }
    }, scopes=['https://www.googleapis.com/auth/earthengine.readonly'])

    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    
    # Save credentials in the session or database if needed
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    
    return HttpResponseRedirect(reverse('index'))  # Redirect to your desired page after authentication

# once auth is done, use GEE in views for operations and events
def get_poaching_risk(request):
    # Ensure GEE is initialized
    credentials = initialize_earth_engine()

    # Example: Define your area of interest
    aoi = ee.Geometry.Point([longitude, latitude])
    
    # Example: Calculate NDVI from Sentinel-2 data
    image = ee.ImageCollection('COPERNICUS/S2').filterBounds(aoi).first()
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')

    # Example: Apply threshold and create a mask
    poaching_risk = ndvi.lt(0.2)
    
    # Return the result as JSON
    data = {
        'poaching_risk': poaching_risk.getInfo()
    }
    
    return JsonResponse(data)

