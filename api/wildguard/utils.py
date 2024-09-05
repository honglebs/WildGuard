# wildguard/utils.py

import ee
from google_auth_oauthlib.flow import InstalledAppFlow
from django.conf import settings
import os

def initialize_earth_engine(credentials):
    # Initialize Earth Engine using the credentials from OAuth2

    if not ee.data._credentials:
        ee.Initialize(credentials)
    else:
        ee.Reset()
        ee.Initialize(credentials)
