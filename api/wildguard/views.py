from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import UploadedImage
from .yolo_inference import detect_objects
import json

def uploaded_image(request):
    if request.method == 'POST' and request.FILES['image']:
        #Handle file upload
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        #Run YOLOv5 detection
        predictions = detect_objects(fs.path(filename))

        #Save to database
        uploaded_image = UploadedImage(image=uploaded_file, predictions=json.dumps(predictions))
        uploaded_image.save()

        return render(request, 'result.html', {
            'file_url': file_url,
            'predictions': predictions,
        })
    
    return render(request, 'upload.html')