# api/apps/my_app/views.py
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
import os

# views for the earth engine 
from django.http import JsonResponse
from wildguard.utils import initialize_earth_engine
import ee
from django.http import HttpResponse
from google.oauth2.credentials import Credentials 
import logging 

logger = logging.getLogger(__name__)

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

# generate the authroization URL and redirect to Google OAuth2 CS
def start_auth(request):
    flow = Flow.from_client_secrets_file(
        os.path.join(settings.BASE_DIR, 'wildguard/secrets/client_secret.json'),
        scopes=['https://www.googleapis.com/auth/earthengine.readonly']
    )

    flow.redirect_uri = request.build_absolute_uri('/api/oauth2callback/')

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    # store the state in the session
    request.session['state'] = state

    # redirect to google OAuth page
    return HttpResponseRedirect(authorization_url)


# this is to handle OAuth2 callback where google will redirect the user after
# application is authroized 
def oauth2callback(request):

    # load the client secrets from JSON file 
    state = request.session['state']

    if not state:
        return JsonResponse({'error': 'State not found in session.'}, status=400)

    flow = Flow.from_client_secrets_file(
        os.path.join(settings.BASE_DIR, 'wildguard/secrets/client_secret.json'),
        scopes=['https://www.googleapis.com/auth/earthengine.readonly'],
        state=state
    )

    # ensure the redirect_uri matches the one registered in Google Cloud Console
    flow.redirect_uri = request.build_absolute_uri('/api/oauth2callback/')

    # handle the callback
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    # retrieve credentials and store them in the session
    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    
    return HttpResponseRedirect('/')  # Redirect to your home or another page


# # once auth is done, use GEE in views for operations and events
# def get_poaching_risk(request):

#     # ensure GEE is initialized
#     credentials_info = request.session.get('credentials')
    
#     if not credentials_info:
#         # return JsonResponse({'error': 'User is not authenticated with GEE'}, status=403)
#         return HttpResponseRedirect(reverse('oauth2callback'))  # Redirect to authentication if credentials are missing

#     try:

#         # recreate the Credentials object from the stored session data
#         credentials = Credentials(
#             token=credentials_info['token'],
#             refresh_token=credentials_info['refresh_token'],
#             token_uri=credentials_info['token_uri'],
#             client_id=credentials_info['client_id'],
#             client_secret=credentials_info['client_secret'],
#             scopes=credentials_info['scopes']
#         )

#         # init earth eginue with creds
#         initialize_earth_engine(credentials)

#         # get coordinates from request parms or use default 
#         longitude = request.GET.get('longitude', 35.6847) 
#         latitude = request.GET.get('latitude', 139.7496)

#         try:
#             longitude = float(longitude)
#             latitude = float(latitude)
#         except ValueError:
#             return JsonResponse({'error': 'Invalid coordinates provided.'}, status=400)


#         # defining area of interest
#         aoi = ee.Geometry.Point([longitude, latitude])
        
#         # get date range from request parameters or use default
#         start_date = request.GET.get('start_date', '2023-01-01')
#         end_date = request.GET.get('end_date', '2023-12-31')
        
#         # access the Sentinel-2 image collection
#         image_collection = ee.ImageCollection('COPERNICUS/S2') \
#             .filterBounds(aoi) \
#             .filterDate(start_date, end_date) \
#             .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))  # pptional, filter by cloud cover?
        
#         # Check if the image collection is empty
#         if image_collection.size().getInfo() == 0:
#             return JsonResponse({'error': 'No images found for the specified area and date range.'}, status=404)

#         # get the first image from the filtered collection
#         image = image_collection.first()
        
#         # check if image is None / Null
#         if not image:
#             return JsonResponse({'error': 'No image found after filtering.'}, status=404)
        
#         # log / output the image info 
#         image_info = image.getInfo()
#         logger.debug(f"Retrieved Image Info: {image_info}")

#         # check available bands in the image
#         band_names = image.bandNames().getInfo()
#         logger.debug(f"Available bands: {band_names}") 
        
#         # ensure that the required bands are present
#         required_bands = ['B8', 'B4']
#         for band in required_bands:
#             if band not in band_names:
#                 return JsonResponse({'error': f"Required band '{band}' not found in the image."}, status=400)
        
#         # calculate NDVI
#         ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
        
#         # apply threshold to create a mask for poaching risk
#         poaching_risk = ndvi.lt(0.2)
        
#         # Optionally, visualize or summarize the result
#         # For simplicity, we'll just return the NDVI value at the point
#         ndvi_value = ndvi.reduceRegion(
#             reducer=ee.Reducer.first(),
#             geometry=aoi,
#             scale=10
#         ).get('NDVI').getInfo()
        
#         poaching_risk_value = poaching_risk.reduceRegion(
#             reducer=ee.Reducer.first(),
#             geometry=aoi,
#             scale=10
#         ).get('NDVI').getInfo()
        
#         data = {
#             'ndvi': ndvi_value,
#             'poaching_risk': poaching_risk_value
#         }
        
#         return JsonResponse(data)
    
#     except ee.EEException as e:
#         logger.error(f"Earth Engine Error: {str(e)}")
#         return JsonResponse({'error': 'Earth Engine Error: ' + str(e)}, status=500)
#     except Exception as e:
#         logger.error(f"Unexpected Error: {str(e)}")
#         return JsonResponse({'error': 'Unexpected Error: ' + str(e)}, status=500)

"""
======================================================================================================================================
"""

# nothing makes sense, nothing is working i am crying
def analyze_poaching_risk():
    # Initialize the Earth Engine API
    ee.Initialize()

    # List of African country names
    african_countries = [
        'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi',
        'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
        'Congo', 'Côte d\'Ivoire', 'Democratic Republic of the Congo', 'Djibouti',
        'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon',
        'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia',
        'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
        'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda',
        'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia',
        'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia',
        'Uganda', 'Zambia', 'Zimbabwe'
    ]

    # Load the FAO GAUL dataset and filter African countries
    countries = ee.FeatureCollection("FAO/GAUL/2015/level0")
    africa = countries.filter(ee.Filter.inList('ADM0_NAME', african_countries))

    # Load protected areas dataset
    protected_areas = ee.FeatureCollection("WCMC/WDPA/current/polygons").filterBounds(africa)

    # Simplify protected areas by buffering and simplifying
    simplified_protected_areas = protected_areas.map(lambda feature: feature.simplify(5000))

    # Load NDVI data for vegetation analysis
    ndvi_collection = ee.ImageCollection("MODIS/006/MOD13A1") \
        .filterDate('2023-01-01', '2023-12-31') \
        .select('NDVI') \
        .mean() \
        .clip(africa)

    # Rescale NDVI values to [0, 1] range
    ndvi_scaled = ndvi_collection.unitScale(-32768, 32767)

    # Load night-time lights data to identify human activity
    night_lights = ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG") \
        .filterDate('2023-01-01', '2023-12-31') \
        .mean() \
        .select('avg_rad') \
        .clip(africa)

    # Calculate distance to protected areas
    distance_to_protected_areas = simplified_protected_areas.distance(1000).clip(africa)

    # Invert the distance to highlight areas near protected zones
    proximity_index = distance_to_protected_areas.expression('1000000 - d', {
        'd': distance_to_protected_areas
    })

    # Normalize proximity index
    proximity_normalized = proximity_index.unitScale(0, 1000000)

    # Combine NDVI and proximity data to estimate poaching risk
    poaching_risk = ndvi_scaled.multiply(proximity_normalized)

    # Apply a threshold to highlight high-risk areas
    high_risk_areas = poaching_risk.gt(0.7)

    # Simplify high-risk areas by reducing resolution
    simplified_high_risk_areas = high_risk_areas.reduceToVectors({
        'geometry': africa.geometry(),
        'geometryType': 'polygon',
        'scale': 10000,
        'geometryInNativeProjection': True
    })

    return simplified_high_risk_areas.getInfo()

def get_poaching_risk(request):
    try:
        # Call the function to analyze poaching risk
        high_risk_areas_info = analyze_poaching_risk()
        
        # Return the high-risk areas as a JSON response
        return JsonResponse(high_risk_areas_info)
    
    except ee.EEException as e:
        return JsonResponse({'error': 'Earth Engine Error: ' + str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': 'Unexpected Error: ' + str(e)}, status=500)


 # this is my last test for GEE, debug the backend, find where to put this in the front end
 # fetch map data from the Django API GEE and us it with mapping library like leaflet? 
 # find where to render map 
 
def get_map_data(request):
    region = ee.Geometry.Polygon(
        [[[-5.0, 5.0], [35.0, 5.0], [35.0, -5.0], [-5.0, -5.0], [-5.0, 5.0]]]
    )

    imagery = ee.ImageCollection('COPERNICUS/S2') \
        .filterBounds(region) \
        .filterDate('2023-01-01', '2023-12-31') \
        .sort('CLOUDY_PIXEL_PERCENTAGE') \
        .first()

    ndvi = imagery.normalizedDifference(['B8', 'B4']).rename('NDVI')
    vis_params = {'min': 0, 'max': 1, 'palette': ['white', 'green']}
    map_id = ndvi.getMapId(vis_params)

    return JsonResponse({
        'map_id': map_id['mapid'],
        'token': map_id['token'],
        'tile_url': map_id['tile_fetcher'].url_format,
    })


