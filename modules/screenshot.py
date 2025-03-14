from PIL import ImageGrab
import time
import os

def capture_screenshot():
    try:
        # Ensure the screenshots directory exists
        os.makedirs("logs/screenshots", exist_ok=True)

        # Capture the screenshot
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = f"logs/screenshots/screenshot_{timestamp}.png"
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"Error capturing screenshot: {e}")