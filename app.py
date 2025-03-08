import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from predict import predict_brain_tumor
from email_alert import send_email

# Load the trained model
model = tf.keras.models.load_model("saved_model/brain_tumor_model.h5", compile=False)

# Class labels
class_labels = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# Treatment suggestions
treatment_suggestions = {
    "Glioma": "📌 Treatment:\n- Surgery (if operable)\n- Radiation Therapy\n- Chemotherapy\n- Targeted Drug Therapy",
    "Meningioma": "📌 Treatment:\n- Surgery (if needed)\n- Observation (for slow-growing tumors)\n- Radiation Therapy",
    "No Tumor": "✅ No tumor detected. No treatment required. Maintain a healthy lifestyle!",
    "Pituitary": "📌 Treatment:\n- Medication (hormone regulation)\n- Surgery (for large tumors)\n- Radiation Therapy"
}

# Home Remedies
home_remedies = {
    "Glioma": "🏠 Home Remedies:\n- Eat antioxidant-rich foods (berries, spinach, nuts)\n- Reduce processed foods & sugar intake\n- Stay hydrated\n- Manage stress through meditation & yoga",
    "Meningioma": "🏠 Home Remedies:\n- Maintain a balanced diet with fresh fruits & vegetables\n- Avoid excessive caffeine & processed foods\n- Practice deep breathing exercises",
    "No Tumor": "🏠 Home Remedies:\n- Maintain a healthy diet\n- Stay physically active\n- Regular health check-ups",
    "Pituitary": "🏠 Home Remedies:\n- Consume foods rich in vitamin D & calcium\n- Avoid excessive stress & get quality sleep\n- Engage in regular physical exercise"
}

st.title("🧠 Brain Tumor Detection & Treatment Recommendation")

uploaded_file = st.file_uploader("Upload an MRI Scan (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded MRI Scan", use_column_width=True)

    # Save uploaded file for processing
    file_path = "temp_image.jpg"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Make prediction
    prediction = predict_brain_tumor(file_path, model, class_labels)
    
    # Display prediction
    st.subheader(f"🩺 Diagnosis: **{prediction}**")
    
    # Show treatment suggestion
    st.write(treatment_suggestions[prediction])

    # Show home remedies
    st.write(home_remedies[prediction])

    # Get user email for notification
    email = st.text_input("Enter Your Email for Notification")

    if st.button("Submit and Get Email Notification") and email:
        send_email(email, prediction, treatment_suggestions[prediction], home_remedies[prediction])
        st.success(f"📧 Notification sent to {email}")
