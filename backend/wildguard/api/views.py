from django.shortcuts import render
from rest_framework import viewsets
from .models import SatelliteImage, DetectionResult
from .serializers import SatelliteImageSerializer, DetectionResultSerializer

# Create your views here.

class SatelliteImageViewSet(viewsets.ModelViewSet):
    queryset = SatelliteImage.objects.all()
    serializer_class = SatelliteImageSerializer

class DetectionResultViewSet(viewsets.ModelViewSet):
    queryset = DetectionResult.objects.all()
    serializer_class = DetectionResultSerializer
