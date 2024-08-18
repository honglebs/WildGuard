from django.db import models

# Create your models here.

# defining model for storing satellite images and detection results
class SatelliteImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class DetectionResult(models.Model):
    image = models.ForeignKey(SatelliteImage, on_delete=models.CASCADE)
    result = models.TextField()
    confidence = models.FloatField()
    detected_at = models.DateTimeField(auto_now_add=True)
