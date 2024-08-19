from django.contrib import admin
from .models import SatelliteImage, DetectionResult

# Register your models here.

admin.site.register(SatelliteImage)
admin.site.register(DetectionResult)
