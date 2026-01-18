import numpy as np
import tensorflow as tf
from PIL import Image as PILImage
from django.conf import settings
import os

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = settings.MODEL_PATH
        if not os.path.exists(model_path):
             raise FileNotFoundError(f"Model file not found at {model_path}")
        _model = tf.keras.models.load_model(model_path)
    return _model

def load_preprocessed_image(image_file, model):
    input_shape = model.input_shape
    if not (isinstance(input_shape, tuple) and len(input_shape) == 4):
        raise ValueError(f"Model input_shape must be 4D, got {input_shape}")
    _, H, W, C = input_shape

    img = PILImage.open(image_file)
    if C == 1:
        img = img.convert('L')
    else:
        img = img.convert('RGB')
    
    img = img.resize((W, H))

    arr = np.array(img, dtype=np.float32)
    if C == 1:
        arr = np.expand_dims(arr, axis=-1)
    
    arr /= 255.0
    return np.expand_dims(arr, axis=0)

def predict_fracture(image_file):
    model = get_model()
    img_array = load_preprocessed_image(image_file, model)
    preds = model.predict(img_array)
    
    # Assuming binary classification: 0=fractured, 1=not fractured or similar.
    # main2.py says: 
    # idx = int((preds > 0.5).astype('int32')[0][0])
    # class_names = ['fractured', 'not fractured']
    # label = class_names[idx]
    
    idx = int((preds > 0.5).astype('int32')[0][0])
    class_names = ['fractured', 'not fractured']
    label = class_names[idx]
    confidence = float(preds[0][0])
    
    # If 0 (fractured), confidence that it IS fractured is 1 - preds[0][0] ?
    # Wait, if idx is based on preds > 0.5:
    # If preds > 0.5 -> idx=1 -> 'not fractured'. Confidence is preds.
    # If preds <= 0.5 -> idx=0 -> 'fractured'. Confidence is preds (low for not fractured = high for fractured?)
    # Usually sigmoid output p is prob of class 1.
    # If class 1 is 'not fractured', then p is prob of not fractured.
    # If p is low, it's fractured.
    # Let's return the label and raw prediction, or interpreting it clearly.
    
    # main2.py logic:
    # idx = 0 if pred <= 0.5 else 1.
    # label = class_names[idx] (0: fractured, 1: not fractured)
    # confidence = preds[0][0]
    
    return {
        "label": label,
        "confidence": confidence,
        "raw_prediction": float(preds[0][0])
    }
