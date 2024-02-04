
import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

model = AccidentDetectionModel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX

# Email configuration
sender_email = "Sender Mail"
sender_password = "app_password"
receiver_email = "Enter the Receiver Mail Here"
subject = "Accident Alert"
body = "Accident happend at the Location .......!"

email_sent = False

def send_email():
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

def startapplication(use_webcam=False):
    global email_sent  

    if use_webcam:
        # Replace 'your_ip_address' and 'your_port_number' with the values from the IP Webcam app
        url = 'http://192.168.43.1:8080/video'   # Enter the Url here (IP)
        video = cv2.VideoCapture(url)
    else:
        video = cv2.VideoCapture('cars5.mp4')  # Input Video File

    while True:
        ret, frame = video.read()

        # Check if the frame is empty (end of video stream)
        if not ret:
            print("Video stream ended.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if pred == "Accident":
            prob = (round(prob[0][0] * 100, 2))

            if prob > 50 and not email_sent:  
                send_email()
                email_sent = True  

            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred + " " + str(prob), (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

        cv2.imshow('Video', frame)

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    use_webcam = False
    startapplication(use_webcam)
