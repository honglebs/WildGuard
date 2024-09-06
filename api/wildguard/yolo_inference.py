import torch
import cv2
import numpy as np
from pathlib import Path

#Load the trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r"C:\Users\aurel\Downloads\WildGuard\ml-ai\yolov5\runs\train\training_elephant\weights\best.pt", force_reload=True)

def detect_objects(image_path):
    #Load image
    img = cv2.imread(image_path)

    #Perform inference
    results = model(img)

    #Get results
    predictions = results.xyxy[0].cpu().numpy()
    return predictions