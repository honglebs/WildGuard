# handle the OAuth / authentication flow and init the GEE with authenticated credentials
# wildguard/utils.py

import ee
from google_auth_oauthlib.flow import InstalledAppFlow
from django.conf import settings

def initialize_earth_engine():

    # Load OAuth2 credentials from the .env file 
    flow = InstalledAppFlow.from_client_config({
        "web": {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uris": [settings.GOOGLE_REDIRECT_URI]
        }
    }, scopes=['https://www.googleapis.com/auth/earthengine.readonly'])

    credentials = flow.run_local_server(port=0)  # Starts a local server to handle the OAuth flow
    ee.Initialize(credentials)  # Initialize the Earth Engine client with these credentials

    return credentials
