import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject, body, to_email):

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = os.getenv("GMAIL_USER")
    msg["To"] = to_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASS"))

    server.sendmail(msg["From"], [to_email], msg.as_string())
    server.quit()
