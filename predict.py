import numpy as np
import cv2
import tensorflow as tf

def predict_brain_tumor(image_path, model, class_labels):
    # Load and preprocess image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (150, 150))  # Resize to match model input
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)

    return class_labels[predicted_class]
