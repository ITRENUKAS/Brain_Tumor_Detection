(Brain Tumor Detection Project)

# 🧠 Brain Tumor Detection & Classification with Email Alerts  

This is a **Deep Learning project** that helps detect and classify brain tumors from MRI images.  
It can classify images into **four types**:  
✅ **Glioma**  
✅ **Meningioma**  
✅ **No Tumor**  
✅ **Pituitary**  

🔔 **Bonus Feature:** It can send an **email alert** with the results and treatment suggestions.  

---

## 🚀 Features  
✅ **Detect Brain Tumors:** Upload an MRI image and get instant results.  
✅ **Easy to Use:** Simple interface built using **Streamlit**.  
✅ **Email Alerts:** Get diagnosis and treatment details sent to your email.  
✅ **Fast and Accurate:** Uses Deep Learning (CNN) for classification.  

---

## 📂 Dataset  
The project uses MRI images stored in **two folders**:  
- **Training Data:** Used to train the model.  
- **Testing Data:** Used to check accuracy.  

Each folder has four categories:  
- `glioma`  
- `meningioma`  
- `notumor`  
- `pituitary`  

---

## 🛠 How to Set Up  

### 1️⃣ **Download and Install Python**  
First, install **Python (version 3.8 or later)** from:  
👉 [Python Official Website](https://www.python.org/downloads/)

### 2️⃣ **Download the Project**  
Click on **"Download ZIP"** or use this command:  
```bash
git clone https://github.com/your-username/brain-tumor-detection.git
cd brain-tumor-detection
3️⃣ Install Required Libraries
Run this command in the terminal:

pip install -r requirements.txt
4️⃣ Run the Application
Start the application using this command:


streamlit run app.py
Now, open the URL displayed in the terminal (e.g., http://localhost:8501).

🎯 How to Use
1️⃣ Upload an MRI image (JPG/PNG format).
2️⃣ The model will analyze the image and classify the tumor.
3️⃣ It will display the detected tumor type with an accuracy score.
4️⃣ Enter your email to receive a report with treatment suggestions.

📧 Email Notification System
💡 To enable email alerts, you need to configure SMTP settings:

1️⃣ Go to your Gmail account → Security → Enable 2-Step Verification
2️⃣ Generate an App Password from Google App Passwords
3️⃣ Update the email settings in email_alert.py:


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
🖥 Project Files
📁 Brain-Tumor-Detection


│── dataset/          # MRI images for training & testing
│── saved_model/      # Trained model file
│── static/           # UI images and assets
│── app.py            # Main application file (Streamlit UI)
│── model.py          # Code for training the deep learning model
│── predict.py        # Code for classifying MRI images
│── email_alert.py    # Code for sending email alerts
│── requirements.txt  # List of required Python libraries
│── README.md         # Project documentation
🔗 Technologies Used
✅ Python
✅ TensorFlow & Keras (Deep Learning)
✅ OpenCV (Image Processing)
✅ Streamlit (Web UI)
✅ SMTP (Email Service)