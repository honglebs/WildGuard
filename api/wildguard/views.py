from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import UploadedImage
from .yolo_inference import detect_objects
import json
import numpy as np

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        #Handle file upload
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        #Run YOLOv5 detection
        predictions = detect_objects(fs.path(filename))

        #Convert NumPy array or other objects to JSON serializable types
        if isinstance(predictions, np.ndarray):
            predictions_list = predictions.tolist()
        elif isinstance(predictions, list):
            #Ensure all elements in the list are JSON serializable
            predictions = [[float(x) if isinstance(x, np.generic) else x for x in item] for item in predictions]

        #Save the result to the database
        uploaded_image = UploadedImage(image=uploaded_file, predictions=json.dumps(predictions_list))
        uploaded_image.save()

        return render(request, 'result.html', {
            'file_url': file_url,
            'predictions': predictions,
        })
    
    return render(request, 'upload.html')