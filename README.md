
# Ethical Keylogger for Parental Control

This is an **ethical keylogger** designed for **parental control** and **safety monitoring**. It captures keystrokes, takes periodic screenshots, and sends activity reports via email. The app also includes sentiment analysis to detect signs of cyberbullying or depression in typed messages(not to Accurate).

---

## Features
- **Keylogging**: Captures keystrokes and logs them to a file.
- **Screenshot Capture**: Takes periodic screenshots at a configurable interval.
- **Email Reports**: Sends activity reports (logs and screenshots) via email.
- **Sentiment Analysis**: Detects negative sentiment in typed messages.
- **System Tray Integration**: Runs in the background with a system tray icon.
- **Configuration GUI**: Allows users to update settings via a graphical interface.

---

## Installation

### Prerequisites
- Python 3.8 or higher.
- Required Python libraries: `pynput`, `Pillow`, `schedule`, `transformers`, `pystray`, `plyer`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rajm012/ethical-keylogger.git
   cd ethical-keylogger
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `config.json` file with your email settings and preferences.

4. Run the app:
   ```bash
   python main.py
   ```

---

## Configuration

### `config.json`
The `config.json` file contains the following settings:
- **`alert_keywords`**: List of keywords to trigger alerts (e.g., "bully", "suicide").
- **`email`**: Email configuration (sender, password, receiver, SMTP server, and port).
- **`screenshot_interval`**: Interval (in seconds) for capturing screenshots.
- **`report_interval`**: Interval (in seconds) for sending email reports.

Example `config.json`:
```json
{
  "alert_keywords": ["bully", "depressed", "suicide", "hate", "threat", "kill", "death"],
  "email": {
    "sender": "your_email@gmail.com",
    "password": "your_app_specific_password",
    "receiver": "parent_email@gmail.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
  },
  "screenshot_interval": 30,
  "report_interval": 60
}
```

---

## Usage

### Running the App
1. Run the app:
   ```bash
   python main.py
   ```
2. The app will run in the background with a system tray icon.

### System Tray Menu
- **Configure**: Open the configuration GUI to update settings.
- **Exit**: Stop the app.

### Logs and Screenshots
- **Keylogger Logs**: Saved in `logs/keylogs.txt`.
- **Screenshots**: Saved in `logs/screenshots/`.

### Email Reports
- Activity reports (logs and screenshots) are sent to the specified receiver at the configured interval.

---

## Packaging the App

To package the app into a standalone executable:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --icon=icon.png main.py
   ```

3. The executable will be created in the `dist/` directory.

---

## Stopping the App

### If Running as a Script
- Press **Ctrl+C** in the terminal.

### If Running as an Executable
- Right-click the system tray icon and select **Exit**.
- Use **Task Manager** to end the process.

---

## Download or Build the Executable

The standalone executable (`main.exe`) is too large to upload directly to GitHub due to file size limitations. You have two options:

### Option 1: Reassemble the Executable from Chunks

The executable has been split into smaller chunks for easy uploading. Follow these steps to reassemble it:

1. **Download the Chunks**:
   - Download all the `.part` files from the `dist/` directory:
     - `main.exe.part1`
     - `main.exe.part2`
     - `main.exe.part3`
     - (and so on...)

2. **Reassemble the Executable**:
   - Place all the `.part` files in the same directory.
   - Run the following Python script to reassemble the executable:
     ```bash
     python reassemble_file.py
     ```
   - The reassembled executable will be saved as `dist/main_reassembled.exe`.

3. **Rename the Executable**:
   - Rename `main_reassembled.exe` to `main.exe`.

### Option 2: Build the Executable from Source
If you prefer to build the executable yourself, follow these steps:

1. **Install Dependencies**:
   - Ensure you have Python 3.8 or higher installed.
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

2. **Build the Executable**:
   - Run the following command to build the executable:
     ```bash
     pyinstaller --onefile --windowed --icon=icon.png main.py
     ```
   - The executable will be created in the `dist/` directory.

3. **Run the Executable**:
   - Navigate to the `dist/` directory and run:
     ```bash
     ./main.exe
     ```

### Option 3: Download from the drive link or request from me using issues

   - [Download Executable](https://drive.google.com/file/d/1BiB5QDsH0vxoLm4Tb6VSu-yL2wrO0D7a/view?usp=sharing)

---

## Reassembly Script (`reassemble_file.py`)

If you choose to reassemble the executable, use the following Python script in the same folder as of chunks. 


## Ethical Considerations
- Use this app only for **ethical purposes** (e.g., parental control with consent).
- Ensure compliance with local laws and regulations.
- Inform users (e.g., children) about the monitoring.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

---

## Support
For questions or issues, please open an issue on GitHub or contact the maintainer.
```

---
