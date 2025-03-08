import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ Use Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "t6861248@gmail.com"
SENDER_PASSWORD = "vhxl apkj bzqd kehn"  # Generate from Google App Passwords

def send_email(receiver_email, prediction, treatment, home_remedy):
    subject = "Brain Tumor Detection - Diagnosis, Treatment & Home Remedies"

    body = f"""
    Dear User,

    Your MRI scan analysis result is: **{prediction}**.

    
    {treatment}

   
    {home_remedy}

    📌 This is an automated message. Please do not reply.

    Thank you for using our AI-powered brain tumor detection service!
    """

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print("✅ Email Sent Successfully!")
    except Exception as e:
        print(f"❌ Error Sending Email: {e}")
