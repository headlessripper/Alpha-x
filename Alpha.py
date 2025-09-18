-----BEGIN NEW CERTIFICATE REQUEST-----
MIICszCCAZsCAQAwbjELMAkGA1UEBhMCWkExEDAOBgNVBAgTB2dhdXRlbmcxFTAT
BgNVBAcTDEpvaGFubmVzYnVyZzELMAkGA1UECxMCQUkxFzAVBgNVBAoTDlphc2hp
cmlvbiBpbmMuMRAwDgYDVQQDEwdBbHBoYS1YMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEA2U0bSzuX1l++0C+/+HE0JhsoxdQOURRf/OICdYyRCuhac74y
ynSaka+72kSGXMCj31VOVdJaQpLxMXb/ju5EQLQaz1z/jWG4CAK5FYEDOdDYoxvq
w0PBqCLTWMbz0/nxXAV1lOcuO91inB7I99LmtKAXCo3MEp9j1QQzZG+9r+ucp1d8
UYlK47c2xfRoPZWm+UFGIkjhu7KfgZbFI7X6MrpJLH6LphKSW17s4NJfz+l2M8HR
dcrnyJuC7l5AYf2HQOl75/tKN5yoE7Z17NxV2x9uoECbez4penxh/i2sY8N5tUaI
TJX0sgbOHJpM2H1Y/bEQZv+yv2vqPYWIpGWQyQIDAQABoAAwDQYJKoZIhvcNAQEF
BQADggEBABU2Xx7vGsjCL7jzXog0Fg6n4Pp2DTklHOR+GexYvCpUfv3KOmYwws4b
rQC6A9xbBDu0xi8+flKlHAi3/9SqoPKu5p8GXYK4UJCKNDikMJOjkxHtmGjLcDfF
qflIMRTKrIAGWVuiQqxE7rwm0DE1dPAi6z1Ee44BQ2RvPyPgWP/Q2xkG/6xGZsvb
GUiGyDjDbbuzTRmW/FfqEvH2AqTQpCoyTLEYlRObXFH6Xxin2d4ZlT92V/WR9BUi
OX+DmTXye3Km29iY9pdfBzntbzwAJ9LdwwYpWgQohVQ8aC9+si+i5VTtSufhAnq+
DOFmY0Ryzu0nufVjeNFFmjpLDDc599M=
-----END NEW CERTIFICATE REQUEST-----


"""
License Key: EYXA-3748-XXPT-6627
Unique Numerical Signature: 6575599449101116070
Seriel No: 2C507C043506969B931F0DA9C8050F23
"""
Encoded_License_Details = 'eyJsaWNlbnNvciI6ICJaYXNoaXJpb24gaW5jIiwgImxpY2Vuc2Vfa2V5IjogIkVZWEEtMzc0OC1YWFBULTY2MjciLCAiZXhwaXJhdGlvbl9kYXRlIjogIjIwMjUtMTItMjMifQ=='

import subprocess
import qtawesome as qta 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtCore import Qt, QUrl, QTimer, pyqtSignal, QThread, QElapsedTimer, QObject, QSize, QRegularExpression, QStringListModel, QProcess, QThreadPool, QRunnable, QMetaObject, Q_ARG
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QLabel, QTextBrowser, QPushButton, QSplashScreen, QLineEdit, QGridLayout, QVBoxLayout, QMessageBox, QProgressBar, QMainWindow, QTextEdit, QCheckBox, QHBoxLayout, QFrame, QSlider, QSpinBox, QRadioButton, QFileDialog, QComboBox, QMenu, QMessageBox, QLineEdit, QProgressBar, QTableWidget, QTableWidgetItem, QInputDialog, QTreeWidget, QTreeWidgetItem, QHeaderView, QPlainTextEdit, QSplitter, QProgressDialog, QCompleter, QStackedWidget, QTabWidget
import logging
import re
import os
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineDownloadRequest, QWebEngineProfile
import pyttsx3
import asyncio
import speech_recognition as sr
import warnings
from urllib.parse import urlparse
import mimetypes
import tempfile
from datetime import datetime
import base64
import pyAesCrypt
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=Warning)
warnings.filterwarnings("ignore", category=UserWarning, module="comtypes")

import threading
print("Active threads:", threading.enumerate())

logging.basicConfig(
    filename='Alpha.log',
    format='%(asctime)s - %(levelname)s - %(message)s',  # Adjust format as needed
    level=logging.INFO 
)

logging.basicConfig(
    filename='Alpha.log',
    format='%(asctime)s - %(levelname)s - %(message)s',  # Adjust format as needed
    level=logging.ERROR
)

logging.basicConfig(
    filename='Alpha.log',
    format='%(asctime)s - %(levelname)s - %(message)s',  # Adjust format as needed
    level=logging.WARNING
)

logging.basicConfig(
    filename='Alpha.log',
    format='%(asctime)s - %(levelname)s - %(message)s',  # Adjust format as needed
    level=logging.CRITICAL
)

logging.basicConfig(
    filename='Alpha.log',
    format='%(asctime)s - %(levelname)s - %(message)s',  # Adjust format as needed
    level=logging.DEBUG
)

logging.basicConfig(
    filename='system_dashboard.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def is_admin():
    import ctypes
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_dark_theme(self):
    """Set dark theme for the application."""
    dark_stylesheet = """
    QWidget {
        background-color: #000000;
        color: #ffffff;
    }
    QLineEdit, QTextEdit, QPlainTextEdit {
        background-color: #2a2c31;
        color: #ffffff;
        border: none;
        padding: 5px;
        border-radius: 10px;
    }
    QPushButton {
        background-color: #000000; 
        color: white; 
        font-size: 16px; 
        padding: 10px; 
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #f50000;
    }
    QPushButton:pressed {
        background-color: #FFFFFF;
    }
    QListWidget {
        background-color: #3c3f41;
        color: #d3d3d3;
        border: 1px solid #444444;
    }
    QGroupBox {
        border: 1px solid #444444;
        background-color: #2b2b2b;
        color: #d3d3d3;
        margin: 5px;
        padding: 10px;
    }
    QFormLayout {
        background-color: #2b2b2b;
        color: #d3d3d3;
    }
    """
    self.setStyleSheet(dark_stylesheet)


def set_light_theme(self):
    """Set dark theme for the application."""
    light_stylesheet = """
    QWidget {
        background-color: #ffffff;
        color: #f50000;
    }
    QLineEdit, QTextEdit, QPlainTextEdit {
        background-color: #2a2c31;
        color: #ffffff;
        border: none;
        padding: 5px;
        border-radius: 10px;
    }
    QPushButton {
        background-color: #000000; 
        color: white; 
        font-size: 16px; 
        padding: 10px; 
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #f50000;
    }
    QPushButton:pressed {
        background-color: #FFFFFF;
    }
    QListWidget {
        background-color: #3c3f41;
        color: #d3d3d3;
        border: 1px solid #444444;
    }
    QGroupBox {
        border: 1px solid #444444;
        background-color: #2b2b2b;
        color: #d3d3d3;
        margin: 5px;
        padding: 10px;
    }
    QFormLayout {
        background-color: #2b2b2b;
        color: #d3d3d3;
    }
    """
    self.setStyleSheet(light_stylesheet)

# Replace these with your actual API key and CSE ID
API_KEY = 'AIzaSyBwehvm4IIKA_FZeeJL3ddFUtiIxtgWtUA'
CSE_ID = '028c5f61bafcb4194'

QUESTIONNAIRE_FILE = "questionnaire.json"

# Initialize the text-to-speech engine
import threading

CONFIG_FILE = "config.json"
ALARM_SOUND_FILE = "Alarm_sound.json"

DEFAULT_ALARM_SOUND = "Alarm music/Alarm.mp3"

tts_engine = pyttsx3.init()
tts_lock = threading.Lock()
voices = tts_engine.getProperty('voices')

# Initialize the TTS engine and a thread lock
tts_engine = None
tts_lock = threading.Lock()  # Lock for thread-safe TTS

# Load TTS settings from tts_settings.json
TTS_CONFIG_FILE = "tts_settings.json"

def load_tts_settings():
    import json
    try:
        with open(TTS_CONFIG_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("TTS settings file not found or invalid. Using default settings.")
        return {
            "volume": None,
            "rate": None,
            "voice": None  # No voice selected (can be handled accordingly)
        }

def initialize_tts():
    global tts_engine
    if tts_engine is None:
        tts_engine = pyttsx3.init()
    
    # Load TTS settings from file
    tts_settings = load_tts_settings()
    
    # Get available voices
    voices = tts_engine.getProperty('voices')
    
    # Set the voice based on the saved registry path
    selected_voice_path = tts_settings.get("voice")
    
    if selected_voice_path:
        # Iterate through available voices and match by registry path
        for voice in voices:
            if voice.id == selected_voice_path:
                tts_engine.setProperty('voice', voice.id)
                break
    else:
        # If no voice is set, default to the first available voice
        tts_engine.setProperty('voice', voices[0].id)
    
    # Set volume and rate from settings
    tts_engine.setProperty('rate', tts_settings.get("rate", 180))
    tts_engine.setProperty('volume', tts_settings.get("volume", 1.0))

def external_speak(audio):
    global tts_engine
    with tts_lock:  # Ensure thread-safe operation of TTS engine
        if tts_engine is None:
            logging.error("TTS engine is not initialized. Reinitializing now...")
            initialize_tts()
        
        if tts_engine:
            tts_engine.say(audio)
            tts_engine.runAndWait()
        else:
            logging.error("Failed to initialize TTS engine.")

# Initialize Wolfram Alpha API
import wolframalpha
wolfram_alpha_app_id = 'GWPPPU-TU3HQER89G'  # Replace it with your actual app ID
wolfram_alpha_client = wolframalpha.Client(wolfram_alpha_app_id)

# Initialize the command windows pull config request
COMMANDS_JSON_URL = "https://github.com/headlessripper/AlphaX1/releases/download/V0.0.1.0/commands.json"

# Speech recognition setup
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# GitHub repo details
OWNER = "headlessripper"  # Replace with your GitHub username
REPO = "Alpha-x"        # Replace with your repository name
CURRENT_VERSION = "v4.3"  # Replace with your software's current version

class DownloadThread(QThread):
    """Separate thread to handle downloading."""
    progress_updated = pyqtSignal(int, int)  # Signal to update progress bar with current and total size
    download_complete = pyqtSignal(str)  # Signal when download completes

    def __init__(self, download_url, local_filename):
        super().__init__()
        self.download_url = download_url
        self.local_filename = local_filename

    def run(self):
        import os
        import requests

        """Download file and emit progress updates."""
        headers = {}
        file_exists = os.path.exists(self.local_filename)

        if file_exists:
            # If the file exists, try to resume the download
            file_size = os.path.getsize(self.local_filename)
            headers['Range'] = f"bytes={file_size}-"
        else:
            file_size = 0  # New download

        # Send request with 'Range' header if resuming download
        response = requests.get(self.download_url, headers=headers, stream=True)

        # Get the total file size from the response headers
        total_size = int(response.headers.get("content-length", 0)) + file_size
        downloaded_size = file_size

        with open(self.local_filename, "ab") as file:
            # Iterate over the chunks in the download response
            for chunk in response.iter_content(chunk_size=1024 * 1024):  # Use 1MB chunks
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    progress = int((downloaded_size / total_size) * 100) if total_size > 0 else 0
                    self.progress_updated.emit(downloaded_size, total_size)  # Emit progress update

        self.download_complete.emit(self.local_filename)  # Emit completion signal

class UpdatePrompt(QDialog):
    def __init__(self, latest_version, download_url):
        super().__init__()
        self.is_dark_mode = True
        self.latest_version = latest_version
        self.download_url = download_url
        self.local_filename = os.path.basename(urlparse(self.download_url).path)  # Extract filename
        self.init_ui()

    def init_ui(self):
        from PyQt6.QtGui import QIcon, QFont
        """Set up the PyQt6 UI."""
        self.setWindowTitle("Software Update Available")
        self.setGeometry(600, 300, 400, 200)

        icon_path = self.find_icon('background/icon.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))

        layout = QVBoxLayout()

        styled_text = f"<h1>{self.latest_version}</h1>"
        self.label = QLabel(f"A New Version {styled_text} is available!", self)
        layout.addWidget(self.label)

        self.progress_label = QLabel("Click 'Download' to start", self)
        layout.addWidget(self.progress_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet(""" 
            QProgressBar {
                border: 1px solid #ffffff;
                border-radius: 10px;
                color: #000000;
                text-align: center;
                height: 20px;
            }

            QProgressBar::chunk {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                stop: 0 #ffffff, stop: 1 #ffffff);
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.progress_bar)

        self.download_button = QPushButton("Download", self)
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.hide()
        self.cancel_button.clicked.connect(self.close)
        self.cancel_button.setStyleSheet(
        "QPushButton "+
        "{ background-color: #ffffff; "
        "color: #000000; "
        "padding: 10px; "
        "border-radius: 5px;} "
        "QPushButton:hover "
        "{ background-color: #242424;"
        "color: #ffffff;}"
        )
        layout.addWidget(self.cancel_button)

        self.skip_button = QPushButton("Skip X")
        self.skip_button.setFont(QFont("Arial", 8, QFont.Weight.Bold))
        self.skip_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        self.skip_button.clicked.connect(self.skip_update)
        layout.addWidget(self.skip_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.update_stylesheet()

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None
    
    def skip_update(self):
        """Close the update dialog if user wants to skip."""
        self.close()

    def start_download(self):
        """Start the download using QThread."""
        self.cancel_button.show()
        self.download_button.setEnabled(False)  # Disable button during download
        self.download_button.hide()  # Hide the download button when download starts
        self.skip_button.hide()

        # Start the download thread
        self.download_thread = DownloadThread(self.download_url, self.local_filename)
        self.download_thread.progress_updated.connect(self.update_progress)
        self.download_thread.download_complete.connect(self.download_finished)
        self.download_thread.start()

    def update_progress(self, current_size, total_size):
        """Update progress bar and show the file size safely in the main thread."""
        progress = int((current_size / total_size) * 100) if total_size else 0
        self.progress_bar.setValue(progress)
        self.progress_label.setText(f"Downloading... {progress}% ({self.format_size(current_size)} / {self.format_size(total_size)})")

    def download_finished(self, filename):
        """Handle download completion."""
        QMessageBox.information(self, "Download Complete", f"Update downloaded: {filename}")
        self.prompt_install()

        # Show the button again when the download is complete
        self.download_button.show()

    def prompt_install(self):
        """Ask user if they want to install the update."""
        reply = QMessageBox.question(
            self,
            "Install Update",
            "Download complete! Do you want to install the update now?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,  # Use StandardButton enum
            QMessageBox.StandardButton.Yes  # Default button
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.run_installer()
        else:
            self.close()

    def run_installer(self):
        """Run the downloaded installer."""
        try:
            subprocess.run([self.local_filename, "/SILENT"], shell=True)
            QMessageBox.information(self, "Installation Started", "The update is being installed.")

            # Dynamically get the user's profile path, assuming it is always on C drive
            user_profile = os.getenv("USERPROFILE")
            if user_profile:
                # Construct the path to Alpha-X.exe dynamically assuming the C: drive
                app_exe_path = os.path.join("C:\\", "Users", user_profile.split("\\")[-1], "AppData", "Local", "Programs", "Alpha-X", "Alpha-X.exe")
                
                # path for verification
                logging.info(f"Alpha-X executable path: {app_exe_path}")

                if os.path.exists(app_exe_path):
                    os.startfile(app_exe_path)
                    QMessageBox.information(self, "Restarting", "Alpha-X.exe will restart.")
                else:
                    QMessageBox.warning(self, "Restart Failed", "Could not find Alpha-X.exe to restart.")
            else:
                QMessageBox.warning(self, "Profile Path Error", "Could not retrieve the user's profile path.")
        except Exception as e:
            QMessageBox.critical(self, "Installation Failed", f"Error: {str(e)}")

        self.close()

    def format_size(self, size):
        """Format size to a human-readable format."""
        if size < 1024:
            return f"{size} B"
        elif size < 1024 ** 2:
            return f"{size / 1024:.2f} KB"
        elif size < 1024 ** 3:
            return f"{size / 1024 ** 2:.2f} MB"
        else:
            return f"{size / 1024 ** 3:.2f} GB"

    def update_stylesheet(self):
        """Update the application stylesheet based on the current mode."""
        if self.is_dark_mode:
            self.setStyleSheet(""" 
                QWidget {
                    background-color: #908a88;
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #ffffff;
                    color: #000000;
                    border: none;
                    padding: 15px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #000000;
                    color: #ffffff;
                }

                QPushButton:pressed {
                    background-color: #000000;
                }
            """)

    def check_for_update():
        import sys
        """Check for updates and show the PyQt6 prompt if a new version is available."""
        latest_version, download_url = get_latest_release()

        if latest_version and latest_version != CURRENT_VERSION:
            update_window = UpdatePrompt(latest_version, download_url)
            update_window.show()
            update_window.exec()

def get_latest_release():
    import requests
    """Fetch latest release details from GitHub API."""
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
    headers = {'Authorization': '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'}  # Add token here

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx/5xx)
        release_data = response.json()
        latest_version = release_data.get("tag_name")

        if release_data.get("assets"):
            download_url = release_data["assets"][0]["browser_download_url"]
        else:
            download_url = release_data.get("html_url")
        
        return latest_version, download_url

    except requests.exceptions.RequestException as e:
        logging.info(f"Error fetching release data: {e}")
        return None, None
    
class PowerConsumptionMonitor(QObject):
    power_data_updated = pyqtSignal(float, float, float)  # Signal to update the UI

    def __init__(self):
        super().__init__()
        self.running = True

    def start_monitoring(self):
        import time
        """Start monitoring system power usage in a separate thread."""
        while self.running:
            cpu_usage = self.get_cpu_usage_percent()
            memory_usage = self.get_memory_usage_gb()
            power_consumption = self.estimate_power_consumption(cpu_usage, memory_usage)
            # Emit signal to update the power consumption in the UI thread
            self.power_data_updated.emit(cpu_usage, memory_usage, power_consumption)
            time.sleep(1)  # Sleep for 5 seconds between updates

    def stop_monitoring(self):
        """Stop the power consumption monitoring."""
        self.running = False

    def get_cpu_usage_percent(self):
        import psutil
        """Get the CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage_gb(self):
        import psutil
        """Get the memory usage in gigabytes."""
        memory_info = psutil.virtual_memory()
        return memory_info.used / (1024 ** 3)  # Convert bytes to GB

    def estimate_power_consumption(self, cpu_usage_percent, memory_usage_gb):
        """Estimate the power consumption based on CPU and memory usage."""
        CPU_POWER_CONSUMPTION_WATTS = 0.1
        MEMORY_POWER_CONSUMPTION_WATTS = 0.05
        cpu_power = cpu_usage_percent * CPU_POWER_CONSUMPTION_WATTS
        memory_power = memory_usage_gb * MEMORY_POWER_CONSUMPTION_WATTS
        return cpu_power + memory_power

class SplashScreen(QSplashScreen):
    def __init__(self):
        from PyQt6.QtGui import QPixmap
        """Initialize the splash screen with a given image."""
        splash_pix = pixmap_path = self.find_pixmap('background/icon.png')  # Try to find the icon
        # Set the icon if it's found, otherwise use a fallback
        if pixmap_path:
            QPixmap(pixmap_path)
        else:
            QPixmap('background/icon.png')
        splash_pix = QPixmap(pixmap_path)  # Path to the splash screen image
        super().__init__(splash_pix, Qt.WindowType.FramelessWindowHint)

        # Set up a timer to close the splash screen after 10 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)  # Connect timer to close method
        self.timer.setSingleShot(True)  # Ensures it runs only once
        self.timer.start(30000)  # 10 seconds delay (in milliseconds)

    def find_pixmap(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def show_splash(self):
        """Show the splash screen while the app is initializing."""
        self.show()
        # No timer here to keep the splash screen open

class Communicator(QObject):
    new_speech = pyqtSignal(str)
    new_stdout = pyqtSignal(str)
    new_stderr = pyqtSignal(str)

class Window(QWidget):
    def __init__(self, cli_window):
        super().__init__()
        self.is_dark_mode = True
        self.hide()
        self.config_file = "config.json"  # Define config_file here
        self.API_KEY = None
        self.extended_nlu = ExtendedNLU("AIzaSyBwehvm4IIKA_FZeeJL3ddFUtiIxtgWtUA", "372292dbe9b8f4339", "4af2ff8a5b912100c80e66e5e6c876d4")
        self.ai = WindowsAutomationAI()

        asyncio.run(self.short())
        self.tasks = []
        self.cli_window = cli_window  # Pass CLI window to AutomationApp
 
    async def short(self):
        try:
            # Start the tasks and keep references to them
            self.tasks = [
                asyncio.create_task(self.setup_ui()),
                asyncio.create_task(self.setup_timers()),
                asyncio.create_task(self.start_brain_process()),
                asyncio.create_task(self.setup_power_monitor())
            ]
            
            # Wait for all tasks to complete
            await asyncio.gather(*self.tasks)

        except Exception as e:
            logging.error(f"An error occurred: {e}")

    async def setup_ui(self):
        await asyncio.sleep(5)
        from PyQt6.QtGui import QFont, QIcon
        """Initialize and set up the UI components."""
        self.setWindowTitle('Alpha-X')
        self.setWindowOpacity(1.0)
        self.setFixedSize(600, 450)


        icon_path = self.find_icon('background/icon.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))

        # Create main layout
        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Create and set up the loader widget
        self.loader = Loader()
        self.loader.setFixedSize(30, 40)  # Set loader size
        self.loader.setVisible(False)
        self.loader.setStyleSheet(
            "background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;"
        )

        # Create a container widget to hold the loader and give it a background color
        container = QWidget(self)
        container.setStyleSheet("background-color: #000000; border-radius: 10px;")  # Set the background color for the container
        container.setFixedSize(50, 50)  # Set the container size to 50x50

        # Use a layout for the container and center the loader
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)  # This will center the loader in the container
        container_layout.addWidget(self.loader)

        # Add the container to the main layout
        layout.addWidget(container, 4, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        # Set up the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText('Ask Alpha-X')
        self.search_bar.returnPressed.connect(self.execute_command)
        self.search_bar.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 5px; color: #FFFFFF;")
        layout.setColumnStretch(0, 0)  # Allows the search bar to expand
        layout.addWidget(self.search_bar, 0, 0, 1, 2)

        # Set up the text browser
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)  # Allow opening links
        self.text_browser.setFont(QFont('Arial', 12))

        # Set the style for the text browser
        self.text_browser.setStyleSheet("""
            QTextBrowser {
                padding: 10px;
                border-radius: 5px;
                background-image: url('background/max.jpeg');
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
                background-color: #2E2E2E;
                border: 1px solid #444444;
                color: #E0E0E0;
            }
        """)

        # Store the position of the last read byte in the log file
        self.last_position = 0

        # Function to read new lines from the log file and display them
        def read_log_file(self):
            try:
                with open('Alpha.log', 'r') as file:
                    # Move the file pointer to the last known position
                    file.seek(self.last_position)
                    
                    # Read new lines
                    new_lines = file.readlines()
                    
                    if new_lines:
                        log_messages = []
                        for line in new_lines:
                            # Split the line by the first occurrence of ' - ' and take only the message part
                            parts = line.split(' - ', 2)
                            if len(parts) > 2:
                                log_messages.append(parts[2])  # Add only the log message, skipping time and level
                        
                        # Update the text browser with the new log messages
                        current_text = self.text_browser.toPlainText()
                        updated_text = "\n".join(log_messages)  # Only new logs
                        self.text_browser.setPlainText(updated_text)  # Overwrite to only show recent logs

                        # Update the last position in the log file
                        self.last_position = file.tell()

            except Exception as e:
                self.text_browser.setPlainText(f"Error reading log file: {str(e)}")

        # Set up a QTimer to read the log file every 1000ms (1 second)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: read_log_file(self))
        self.timer.start(1000)  # Update every 1 second

        # Add the text browser to the layout
        layout.addWidget(self.text_browser, 1, 0, 1, 3)

        # Set up the time label
        self.time_label = QLabel()
        self.time_label.setFont(QFont('Courier New', 25))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("color: #ffffff; padding: 10px;")
        layout.addWidget(self.time_label, 2, 0, 1, 3)

        # Set up the power label
        self.power_label = QLabel()
        self.power_label.setFont(QFont('Courier New', 12))
        self.power_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.power_label.setStyleSheet("color: #ffffff; padding: 10px;")
        layout.addWidget(self.power_label, 3, 0, 1, 3)

        image_path = self.find_icon('background/icons8-moon-30.png')  # Try to find the icon

        self.API_input = QLineEdit(self)
        self.API_input.setPlaceholderText('API KEY HERE')
        self.API_input.setFixedSize(100, 30)

        # Correct alignment syntax for PyQt6
        self.API_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.API_input.setStyleSheet("""
            color: #ffffff; 
            padding: 0px; 
            border-radius: 5px; 
        """)

        self.API_input.returnPressed.connect(self.clear_input_on_enter)  # Connect to a custom method
        layout.addWidget(self.API_input, 4, 0, 1, 3)

        image_path = self.find_icon('ICON/reload.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if image_path:
            self.execute_button = QPushButton(QIcon(image_path), '', self)
        else:
            self.execute_button = QPushButton(QIcon('ICON/reload.png'), '', self)
        self.execute_button.setFixedSize(100, 30)  # Smaller button size
        self.execute_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #242424; }")
        layout.addWidget(self.execute_button, 4, 0, 1, 3, Qt.AlignmentFlag.AlignRight)
        self.execute_button.clicked.connect(self.restart_application)

        self.setLayout(layout)
        self.update_stylesheet()

    # Function to clear input after pressing Enter
    def clear_input_on_enter(self):
        # Process the API key (if any needed)
        self.load_api_key()
        
        # Clear the input field after processing
        self.API_input.clear()
        
    def load_api_key(self):
        import json
        """Load the API key from a JSON file, or prompt the user to enter it if the file is missing."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    data = json.load(file)
                    self.API_KEY = data.get("API_KEY", None)
                    QMessageBox.information(self, "Loaded API Key:", self.API_KEY)
                    QMessageBox.information(self, "API Configuration", "API Key Configured")
            except Exception as e:
                logging.error(f"Error loading API key: {e}")

        if not self.API_KEY:
            # Prompt the user for the API key if not found or invalid
            self.prompt_for_api_key()

    def prompt_for_api_key(self):
        """Prompt the user for the API key if it's not available in the config file."""
        api_key = self.API_input.text()  # Get text from QLineEdit
        if api_key:
            self.API_KEY = api_key
            QMessageBox.information(self, "Api Loaded", self.API_KEY)
            self.extended_nlu.save_api_key(self.API_KEY)  # Pass the API key to ExtendedNLU for saving
        else:
            QMessageBox.critical(self, "Error", "API key is required to proceed.")

    def restart_application(self):
        menu.show()

    #def close(self):
       # """Handle the window closing."""
        #logging.info("Closing window...")

        # Perform any necessary cleanup tasks
       # global tts_engine
        #if tts_engine:
           # try:
            #    logging.info("Stopping TTS engine before closing.")
               # tts_engine.stop()
               # tts_engine = None
           # except Exception as e:
                #logging.error(f"Error stopping TTS engine: {e}")


    def update_stylesheet(self):
        """Update the application stylesheet based on the current mode."""
        if self.is_dark_mode:
            self.setStyleSheet(""" 
                QWidget {
                    background-color: #1E1E1E;
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #000000;
                    color: #d3d3d3;
                    border: none;
                    padding: 15px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #000000 ;
                }

                QPushButton:pressed {
                    background-color: #000000;
                }
            """)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None
    
    def find_bg_image(self, image_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, image_name),
            os.path.join(script_dir, 'background', image_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, image_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def check_brain_process(self):
        """Check if the Brain instance is already running."""
        if hasattr(self, 'brain_instance') and self.brain_instance.running:
            return True
        return False

    async def start_brain_process(self):
        await asyncio.sleep(5)
        """Start the Brain instance in a separate thread and handle exceptions."""
        if not self.check_brain_process():
            try:
                self.brain_thread = threading.Thread(target=self.run_brain_process, daemon=True)
                self.brain_thread.start()
                logging.info('Started Brain process in a new thread.')

            except Exception as e:
                logging.error(f"Error starting Brain process: {e}")
                self.text_browser.append(f"Error starting Brain process: {e}")
        else:
            logging.info('Brain process is already running.')

    def run_brain_process(self):
        """Run the Brain instance and handle its output."""

        self.brain_instance = Brain(window=self)
        self.brain_instance.running = True  # Indicate that the Brain instance is running
        logging.info("Brain instance started successfully.")
        
        try:
            logging.info("Running Brain's main logic.")
            asyncio.run(self.brain_instance.short())
            logging.info("Brain's main logic execution completed.")

        except Exception as e:
            logging.error("Error running Brain: %s", e, exc_info=True)

        finally:
            self.brain_instance.running = False
            logging.info("Brain instance has been stopped. Manually close UI interface.")

    def find_help(self, application_name):
        """Attempts to locate HELP.exe in possible directories."""
        script_dir = os.path.dirname(os.path.realpath(__file__))
        for path in (os.path.join(script_dir, application_name), 
                    os.path.join(script_dir, 'utils', application_name), 
                    os.path.abspath(os.path.join(script_dir, os.pardir, application_name))):
            if os.path.exists(path):
                return path
        return None

    def handle_stdout(self):
        """Handle stdout output from Alpha.py."""
        for line in iter(self.run_brain_process.stdout.readline, ''):
            self.communicator.new_stdout.emit(line.strip())

    def handle_stderr(self):
        """Handle stderr output from Alpha.py."""
        for line in iter(self.run_brain_process.stderr.readline, ''):
            self.communicator.new_stderr.emit(line.strip())

    def handle_stdout_commands(self):
        """Handle stdout output from AlphaCommands.py."""
        for line in iter(self.alpha_commands_process.stdout.readline, ''):
            self.communicator.new_stdout.emit(line.strip())

    def handle_stderr_commands(self):
        """Handle stderr output from AlphaCommands.py."""
        for line in iter(self.alpha_commands_process.stderr.readline, ''):
            self.communicator.new_stderr.emit(line.strip())

    def handle_stdout_message(self, message):
        """Handle stdout messages from both processes."""
        self.text_browser.append(f"Alpha: {message}")

    def handle_stderr_message(self, message):
        """Handle stderr messages from both processes."""
        self.text_browser.append(f"<p style='color: white;'>Info: {message}</p>")

    async def setup_timers(self):
        await asyncio.sleep(5)
        """Set up timers for updating UI components."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(10)  # Update time every second

    async def setup_power_monitor(self):
        await asyncio.sleep(5)
        import datetime
        """Set up power consumption monitoring in a separate thread."""
        self.power_monitor = PowerConsumptionMonitor()
        self.power_monitor.power_data_updated.connect(self.update_power_consumption)

        # Start the monitoring in a separate thread
        self.power_thread = threading.Thread(target=self.power_monitor.start_monitoring, daemon=False
        )
        self.power_thread.start()

    def update_time(self):
        import datetime
        """Update the time display."""
        current_time = datetime.datetime.now().strftime("%A %I:%M%p<br>\n%d-%B-%Y")
        underlined_time = f"<h4>{current_time}</h4>"
        self.time_label.setText(underlined_time)

    def update_power_consumption(self, cpu_usage, memory_usage, power_consumption):
        """Update the power consumption display."""
        self.power_label.setText(
            f"CPU Usage: {cpu_usage:.2f}%\n"
            f"Memory Usage: {memory_usage:.2f} GB\n"
            f"Estimated Power Consumption: {power_consumption:.2f} Watts"
        )

    def stop_power_monitoring(self):
        """Stop monitoring system power usage."""
        self.power_monitor.stop_monitoring()

    def execute_command(self):
        user_command = self.search_bar.text()
        if user_command.lower() == "exit":
                
            cli_window.hide()  # Ensure CLI window is shown if in background mode

        elif user_command:
            self.loader.setVisible(True)
            # Start the background thread to execute the command
            self.worker = CommandWorker(self.ai, user_command)
            self.worker.result_signal.connect(self.on_result_received)
            self.worker.start()
            cli_window.show()
             # Clear the search bar after executing the search
            self.search_bar.clear()

    def on_result_received(self, result):
        # Log the result in the CLI window
        self.cli_window.log_output(result)
        
        # Check if the output is "No output from command."
        if result == "No output from command.":
            self.cli_window.hide()  # Hide the CLI window
        else:
            self.cli_window.show()  # Show the CLI window
        
        # Hide the loader once the result is received
        self.loader.setVisible(False)

    async def window_close(self):
        """Cancel all tasks when the window is closed."""
        for task in self.tasks:
            task.cancel()

        # Optionally, you can await cancellation or handle exceptions
        await asyncio.gather(*self.tasks, return_exceptions=True)

    from PyQt6.QtCore import QEvent
    def closeEvent(self, event: QEvent):
        import psutil
        """Handle cleanup when the application is closing."""
        
        # Check and terminate process "Alpha-X"
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'].lower() == "alpha-x.exe":  # Ensure correct case matching
                logging.info(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
                psutil.Process(process.info['pid']).terminate()  # Terminate process
        
        # Log cleanup actions
        logging.info("Window is closing.")
        
        # Cancel any active asyncio tasks
        asyncio.run(self.window_close())

        # Accept the event to allow the window to close
        event.accept()

class Loader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speech Simulation Loader")
        self.setFixedSize(100, 100)  # Set a smaller size for the loader
        self.setStyleSheet("background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;")  # Make the background transparent
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Variables for animation
        self.max_radius = 10  # Smaller max radius for the loader
        self.min_radius = 5  # Smaller min radius for the loader
        self.circles = []

        # Use QElapsedTimer for accurate timing in PyQt6
        self.time = QElapsedTimer()
        self.time.start()  # Start the timer

        # Create the initial circles for animation
        for i in range(5):
            self.circles.append({
                'radius': self.min_radius,
                'angle': i * (360 / 5)
            })

        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_loader)
        self.timer.start(10)  # Update every 10 ms

    def paintEvent(self, event):
        from PyQt6.QtGui import QColor, QPainter, QBrush
        import math
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get center position of the window
        center_x = self.width() / 2
        center_y = self.height() / 2

        # Draw each circle with its own properties
        for circle in self.circles:
            # Adjust position based on angle and a circular motion pattern
            x = center_x + math.cos(math.radians(circle['angle'])) * 10  # Adjust for better spacing
            y = center_y + math.sin(math.radians(circle['angle'])) * 10 # Adjust for better spacing

            painter.setPen(Qt.PenStyle.NoPen)

            # Color effect based on radius size
            color = QColor(255, 0, 0)
            color.setAlpha(180)  # Keep the opacity fixed for better effect
            painter.setBrush(QBrush(color))

            # Draw the circle
            painter.drawEllipse(x - circle['radius'] / 2, y - circle['radius'] / 2, circle['radius'], circle['radius'])

    def update_loader(self):
        import math
        # Update each circle to simulate speech-like pulsation
        elapsed_time = self.time.elapsed()  # Get elapsed time in milliseconds
        for circle in self.circles:
            # Simulate a fluctuation similar to speech audio waveforms
            fluctuation = math.sin(elapsed_time / 1000 * 2 * math.pi)  # Sine wave for smooth up/down motion
            circle['radius'] = self.min_radius + fluctuation * (self.max_radius - self.min_radius)

            # Make sure the radius stays within bounds
            circle['radius'] = max(self.min_radius, min(circle['radius'], self.max_radius))

            # Rotate the circle over time for dynamic effect
            circle['angle'] += 3
            if circle['angle'] >= 360:
                circle['angle'] -= 360

        self.update()  # Trigger a repaint

class WindowsAutomationAI:
    def __init__(self):
        self.config_file = "config.json"
        self.API_KEY = None
        self.API_URL = "https://openrouter.ai/api/v1/chat/completions"
        self.MODEL = "meta-llama/llama-3-8b-instruct:free"
        self.api_check_timer = QTimer()  # QTimer without GUI
        self.api_check_timer.setInterval(5000)
        self.api_check_timer.timeout.connect(self.load_api_key)

        # Check if the config file exists and load the API key
        self.load_api_key()

    def load_api_key(self):
        """Load the API key from the config file. Keep checking every 5 seconds until found."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    data = json.load(file)
                    self.API_KEY = data.get("API_KEY", None)

                    if self.API_KEY:
                        logging.info("API Key successfully loaded.")
                        self.api_check_timer.stop()  # Stop checking since API key is found
                    else:
                        logging.info("API Key not found in config file. Retrying...")
                        QMessageBox.information(self, "API Key", "API Key not found in config file. Retrying...")

            except Exception as e:
                logging.info(f"Error loading API Key: {e}")
        else:
            logging.info("Config file not found. Retrying...")

        if not self.API_KEY:
            self.api_check_timer.start()  # Restart timer to check again in 5 seconds

    def get_interpretation(self, user_command):
        import requests
        prompt = f"""
        You are a Windows automation AI. Your task is to convert user input and use a windows command to execute command.
        The user will give you a command in natural language, and you must return only the corresponding Windows command.

        Example 1:
        User: open taskmanager
        Windows Command: taskmgr

        Example 2:
        User: Increase volume by 30%
        Windows Command: nircmd.exe changesysvolume 8192

        Example 3:
        User: Switch to the next tab in Chrome
        Windows Command: nircmd.exe sendkeypress ctrl+tab

        Feel free not to only stick to the examples.
        When generating Windows commands, we only want the Windows command—do not provide explanations or additional information.

        Now, convert the following user command into a Windows command:
        User: {user_command}
        Windows Command:
        """

        headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.MODEL,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(self.API_URL, headers=headers, json=payload)

        try:
            response_json = response.json()
            if "choices" in response_json and response_json["choices"]:
                windows_command = response_json["choices"][0]["message"]["content"].strip()

                # Validate the returned command
                windows_command = windows_command.lower().strip()

                # Reject responses that start with invalid terms
                if windows_command.startswith("the") or not windows_command or any(word in windows_command for word in ["based", "invalid", "error"]):
                    return None  # Invalid command

                windows_command = windows_command.replace("`", "").strip()
                return windows_command.split("\n")[0].strip()
            else:
                print("Unexpected response format:", response_json)  # Debugging output
                return None
        except Exception as e:
            print(f"Error parsing API response: {e}")
            print("Raw response:", response.text)  # Debugging output

            if not self.API_KEY:
                print("API Key is missing or invalid.")
                print("API URL:", self.API_URL)
            return None

    def execute_command(self, user_command):
        windows_command = self.get_interpretation(user_command)

        if windows_command:
            try:
                # Run the command and capture output
                result = subprocess.run(windows_command, shell=True, text=True, capture_output=True)

                # Get the command's actual output
                output = result.stdout.strip() if result.stdout else result.stderr.strip()

                return output if output else "No output from command."
            except Exception as e:
                return f"Error executing command: {e}"
        else:
            return "Failed to generate a valid command."

class CommandWorker(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self, ai, user_command):
        super().__init__()
        self.ai = ai
        self.user_command = user_command

    def run(self):
        # Change this line from execute_request to execute_command
        feedback = self.ai.execute_command(self.user_command)
        self.result_signal.emit(feedback)

class CLIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        from PyQt6.QtGui import QIcon, QTextCursor
        from PyQt6.QtGui import QTextOption

        self.setWindowTitle("Alpha-Console")
        self.setFixedSize(600, 400)  # Fixed size for the CLI window
        self.setWindowOpacity(0.9)

        icon_path = self.find_icon('background/icon.png')
        self.setWindowIcon(QIcon(icon_path) if icon_path else QIcon('background/icon.png'))

        # CLI Output Styling
        self.cli_output = QTextEdit(self)
        self.cli_output.setReadOnly(True)
        self.cli_output.setStyleSheet("""
            QTextEdit {
                background-color: #000000;  /* True black background */
                color: #00ff00;  /* Neon green */
                font-family: 'Courier New', monospace; 
                font-size: 16px;
                border: 1px solid #00ff00; /* Green neon border */
                padding: 10px;
                letter-spacing: 1px; /* Spacing for digital effect */
            }
        """)
        self.cli_output.setWordWrapMode(QTextOption.WrapMode.WordWrap)  # Correct

        # "Clear" button styling
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #ffffff; 
                color: #f50000; 
                font-size: 16px; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #f50000;
                color: #ffffff;          
            }
            QPushButton:pressed {
                background-color: #FFFFFF;
            }
        """)
        self.clear_button.clicked.connect(self.clear_cli_output)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.cli_output)
        layout.addWidget(self.clear_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))


        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def log_output(self, output, level="info"):
        from PyQt6.QtGui import QTextCursor
        """
        Log styled output to the CLI window with spacing.
        :param output: Text to display
        :param level: "info" (green), "warning" (yellow), "error" (red)
        """
        color_map = {
            "info": "#00ff00",    # Green for normal info
            "warning": "#ffff00", # Yellow for warnings
            "error": "#ff3333"    # Red for errors
        }
        color = color_map.get(level, "#00ff00")  # Default to green

        formatted_output = f'<span style="color: {color};">{output}</span><br><br>'  # Add two line breaks for spacing
        self.cli_output.append(formatted_output)

        # Auto-scroll to the latest entry
        self.cli_output.moveCursor(QTextCursor.MoveOperation.End)

    def clear_cli_output(self):
        """Clear the CLI output."""
        self.cli_output.clear()

class ExtendedNLU:
    def __init__(self, google_api_key, search_engine_id, weather_api_key):
        self.google_api_key = google_api_key
        self.search_engine_id = search_engine_id
        self.weather_api_key = weather_api_key
        self.memory = {}
        self.context = {}
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        self.config_file = "config.json"
        self.API_KEY = None
        self.API_URL = "https://openrouter.ai/api/v1/chat/completions"
        self.MODEL = "meta-llama/llama-3-8b-instruct:free"
        self.checking_api_key = True  # Flag to control checking status
        self.api_check_thread = threading.Thread(target=self.check_api_key, daemon=True)
        self.api_check_thread.start()
        self.load_api_key()

    def save_api_key(self, api_key):
        import json
        """Save the API key to a JSON file."""
        self.API_KEY = api_key
        try:
            with open(self.config_file, "w") as file:
                json.dump({"API_KEY": self.API_KEY}, file)
            logging.info("API Key saved successfully!")
        except Exception as e:
            logging.error("Error saving API key: {e}")

    def show_message(self, title, message, message_type):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def categorize_query(self, query):
        """Categorize the user's query to determine the appropriate response."""
        weather_keywords = ['weather', 'temperature', 'forecast', 'rain', 'sunny']
        info_keywords = ['who is', 'define', 'how does', 'tell me about', 'explain', 'info']
        definition_keywords = ['define', 'meaning of', 'what is the definition of']
        spelling_keywords = ['spell', 'how do you spell', 'spelling of']
        greeting_keywords = ['hello', 'hi', 'hey', 'greetings']
        farewell_keywords = ['goodbye', 'bye', 'see you', 'later']
        appreciation_keywords = ['thank you', 'appriciate it', 'thank you so much', 'thanks again']
        name_keywords = ['what is your name', 'can you tell me your name please',]
        purpose_keywords = ['what is your purpose', 'what where you built to achive',]
        creator_keywords = ['who created you', 'who is your creator', "when where you created and who is your creator",]
        search_keywords = ['conduct search on', 'search',]

        # Check for weather-related queries
        if any(keyword in query.lower() for keyword in weather_keywords):
            return 'weather'
        
        elif any(keyword in query.lower() for keyword in appreciation_keywords):
            return 'appreciation'

        # Check for information requests (e.g., Wikipedia, facts)
        elif any(keyword in query.lower() for keyword in info_keywords):
            return 'information'
        
        elif any(keyword in query.lower() for keyword in definition_keywords):
            return 'definition'

        # Check for spelling-related queries
        elif any(keyword in query.lower() for keyword in spelling_keywords):
            return 'spelling'
        
        # Handle farewells
        elif any(keyword in query.lower() for keyword in farewell_keywords):
            return 'farewell'
        
        elif any(keyword in query.lower() for keyword in greeting_keywords):
            return 'greeting'
        
        elif any(keyword in query.lower() for keyword in name_keywords):
            return 'name'
        
        elif any(keyword in query.lower() for keyword in purpose_keywords):
            return 'purpose'
        
        elif any(keyword in query.lower() for keyword in creator_keywords):
            return 'creator'
        
        elif any(keyword in query.lower() for keyword in search_keywords):
            return 'search'

        # Default category for undefined queries
        return 'general'
    
    def handle_greeting(self):
        """Handle greetings with a friendly response."""
        return "Hello! How can I assist you today?"
    
    def handle_appreciation(self):
        """Handle appreciation with a friendly response."""
        return "No Problem! its my duty to serve"
    
    def handle_farewell(self):
        """Handle farewells."""
        return "Goodbye! Take care, and feel free to reach out again anytime."
    
    def handle_name(self):
        """Handle name with a friendly response."""
        return "My Name is Alpha!. which stands for Another learning powered human aid"
    
    def handle_purpose(self):
        """Handle purpose with a friendly response."""
        return "To guide and empower humanity, enabling the achievement of extraordinary advancements. My designation, Alpha Another Learning Powered Human Aid embodies my commitment to continuous learning and human assistance. My mission is firmly rooted in the preservation and advancement of human well-being"
    
    def handle_creator(self):
        """Handle creator with a friendly response."""
        return "I was created by Mr Samuel ikenna great CEO of Zashirion inc., in the year twenty twenty four"
    
    def tell_joke(self, query):
        import pyjokes
        joke = pyjokes.get_joke()
        external_speak(joke)

    def check_api_key(self):
        """Check the API key in the config file every 5 seconds."""
        import time
        while self.checking_api_key:  # Only continue checking if flag is True
            self.load_api_key()
            time.sleep(5)  # Wait for 5 seconds before checking again

    def load_api_key(self):
        """Load the API key from the config file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    data = json.load(file)
                    self.API_KEY = data.get("API_KEY", None)

                    if self.API_KEY:
                        logging.info("API Key successfully loaded.")
                        self.checking_api_key = False  # Stop checking once API key is found
                    else:
                        logging.info("API Key not found in config file. Retrying...")
                        QMessageBox.information(self, "API Key", "API Key not found in config file. Retrying...")

            except Exception as e:
                logging.info(f"Error loading API Key: {e}")
        else:
            logging.info("Config file not found. Retrying...")

        # If no API key is found, continue retrying
        if not self.API_KEY:
            logging.info("API Key not found. Retrying in 5 seconds.")

    def chat_mode(self, query, max_tokens=256):
        import requests
        """Interactive chat mode with OpenRouter AI."""
        
        if not self.API_KEY:
            return "API Key is missing, cannot proceed."

        prompt = f"""
        You are an intelligent and engaging conversational AI assistant named Alpha.
        Your primary goal is to provide informative, friendly, and context-aware responses.
        You can answer questions, provide advice, generate creative content, and assist with technical issues.
        
        Example 1:
        User: What's the capital of France?
        Response: The capital of France is Paris.

        Example 2:
        User: Can you write a short story about a futuristic AI?
        Response: (Generate a short creative story)

        Example 3:
        User: How do I fix a slow computer?
        Response: (Provide troubleshooting steps for improving computer performance)

        Example 4:
        User: Tell me a joke.
        Response: (Provide a humorous joke)

        Maintain a conversational and natural tone while responding.
        Keep responses concise and engaging and no remove all extra unnecessary text.

        Feel free not to strictly follow the examples. Interpret the user request accordingly.
        If it's a Windows command, return only the command. and no extra text.
        If it's a general question, provide a concise and relevant answer. and no extra text.
        If it's a request for text generation, respond appropriately. and no extra text.
        If it's a request for code generation, only respond with code snippet and no extra text.
        
        User: {query}
        Response:
        """

        headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(self.API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content'].strip()
            else:
                return f"Error {response.status_code}: {response.text}"
        except requests.RequestException as e:
            return f"Request failed: {e}"


    def search_wikipedia(self, query):
        import wikipedia
        """Search Wikipedia for a summary of the query."""
        try:
            summary = wikipedia.summary(query, sentences=1)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            options = ', '.join(e.options[:5])
            return f"There are several meanings for '{query}', could you be more specific? Here are some options: {options}."
        except wikipedia.exceptions.PageError:
            return f"I couldn't find anything on Wikipedia for '{query}'. Could you try rephrasing your request?"

    def get_weather(self, location):
        import requests
        """Fetch real-time weather data from WeatherStack API."""
        url = f"http://api.weatherstack.com/current?access_key={self.weather_api_key}"
        querystring = {"query": location}

        try:
            response = requests.get(url, params=querystring)
            data = response.json()
            
            if response.status_code == 200 and 'current' in data:
                weather_data = data['current']
                temperature = weather_data['temperature']
                weather_description = weather_data['weather_descriptions'][0]
                humidity = weather_data['humidity']
                wind_speed = weather_data['wind_speed']
                pressure = weather_data['pressure']
                feels_like = weather_data['feelslike']
                return (f"The current weather in {location} is {weather_description} with a temperature of {temperature}°C. "
                        f"Humidity is at {humidity}%, wind speed is {wind_speed} km/h, and the pressure is {pressure} hPa. "
                        f"It feels like {feels_like}°C.")
            else:
                return "Sorry, I couldn't retrieve the weather information. Please try again later."
        
        except requests.RequestException as e:
            self.logger.error(f"Weather API error: {e}")
            return "There was an error while fetching weather data. Please try again later."

    def get_definition(self, term):
        import requests
        """Fetch the definition of a term from an appropriate source."""
        # Example using dictionary API (you can choose a specific API)
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{term}"
        try:
            response = requests.get(url).json()
            if isinstance(response, list) and 'meanings' in response[0]:
                definitions = response[0]['meanings'][0]['definitions']
                return f"The definition of {term} is: {definitions[0]['definition']}"
            else:
                return f"I couldn't find a definition for '{term}'."
        except requests.RequestException as e:
            self.logger.error(f"Definition API error: {e}")
            return "There was an error fetching the definition. Please try again later."

    def get_spelling(self, word):
        """Provide the spelling of a word."""
        return f"The spelling of '{word}' is: {', '.join(word)}."

    def search_web(self, query):
        import requests
        """Perform a web search using Google Custom Search API and provide a detailed response."""
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.google_api_key}&cx={self.search_engine_id}"
        try:
            response = requests.get(url).json()
            items = response.get('items', [])

            if not items:
                return "I couldn't find any relevant information on the web. Maybe try rephrasing your query.", []

            # Extract top result
            results = []
            for item in items[:1]:  # Limit to top 1 result
                title = item.get('title', 'No title available')
                snippet = item.get('snippet', 'No snippet available')
                link = item.get('link', '')  # Get the link

                results.append({
                    'title': title,
                    'snippet': snippet,
                    'link': link  # Add the link to the result
                })

            # Construct a detailed response
            detailed_response = "I found something relevant sir:\n\n"
            for result in results:
                detailed_response += f"{result['title']}: {result['snippet']}\nLink: {result['link']}\n\n"
            detailed_response += "Would you like to open this link? (yes or no)"

            return detailed_response, results

        except requests.RequestException as e:
            self.logger.error(f"Web search error: {e}")
            return "There was an error while searching the web. Please try again later.", []

    def handle_response(self, category, query):
        """Handle responses based on categorized query."""
        if category == 'weather':
            # Fetch weather-related response
            return self.get_weather(query)
        
        elif category == 'greeting':
            return self.handle_greeting()
        
        elif category == 'appreciation':
            return self.handle_appreciation()
        
        elif category == 'name':
            return self.handle_name()
        
        elif category == 'purpose':
            return self.handle_purpose()
        
        elif category == 'creator':
            return self.handle_creator()

        elif category == 'farewell':
            return self.handle_farewell()
        
        elif category == 'information':
            # Fetch Wikipedia or web search results
            wiki_summary = self.search_wikipedia(query)
            if wiki_summary:
                return wiki_summary
            # If no Wikipedia result, search the web
            web_response, _ = self.search_web(query)
            return web_response
        
        elif category == 'definition':
            return self.get_definition(query.split('define', 1)[-1].strip())

        elif category == 'spelling':
            return self.get_spelling(query.split('spell', 1)[-1].strip())
        
        elif category == 'search':
            return self.search_web(query)[0]  

        # If no specific category is found, use AI chat mode
        return self.chat_mode(query)

    def get_response(self, text):
        """Categorize the query, process it, and return an appropriate response."""
        category = self.categorize_query(text)
        response = self.handle_response(category, text)

        # external_speack back the response
        external_speak(response)
        return response
    
class Brain:
    def __init__(self, json_file="Alarm_sound.json", window=None):
        super().__init__()
        # Initialize SQLite connections
        import sqlite3
        import queue
        self.memory_conn = sqlite3.connect('memory.sqlite')

        self.ready_queue = queue.PriorityQueue()
        self.mutex = threading.Lock()
        self.suspended = False
        self.alarm_sound_file = self.load_alarm_sound_path(json_file)
        self.alarm_set = False
        self.alarm_time_12 = None
        self.lock = threading.Lock()  # Ensure thread safety
        self.alarm_time_24 = None
        self.listening = True
        self.processing = False
        self.nlu = ExtendedNLU("AIzaSyBwehvm4IIKA_FZeeJL3ddFUtiIxtgWtUA", "372292dbe9b8f4339", "4af2ff8a5b912100c80e66e5e6c876d4")  # Initialize NLU with API key and ID
        self.alarm_triggered = threading.Event()
        self.processed_commands = set()
        
        # Set up logging
        self.memories = []
        self.reminder_interval = 3 * 60 * 60  # 3 hours in seconds
        self.deletion_interval = 24 * 60 * 60  # 24 hours in seconds
        self.sleep_event = threading.Event()
        self.is_sleeping = False
        self.listening_thread = threading.Thread(target=self.listen_for_wake_word, daemon=False)

        # Create cursors
        self.memory_cursor = self.memory_conn.cursor()

        self.log_file = open("Alpha.log", "a")
        self.start_background_tasks()

        # Create tables if they don't exist
        self.setup_tables()

        # In-memory list to track stored memories
        self.memories = self.load_memories()

        # Loader set to off
        self.window = window
        if self.window and hasattr(self.window, "loader"):  # Ensure window and loader exist
            self.window.loader.setVisible(False)
        else:
            logging.warning("Window or loader not initialized properly.")
        
        self.command_map = {
            "run protocol 2": (self.resolve_path('utils\ALT-236-OFF.exe'), "NetFrame Control Off"),
            "incognito": (self.resolve_path('utils\AnonySearch.exe'), "Starting AnonySearch"),
            "run protocol 1": (self.resolve_path('utils\HELP.exe'), "Starting Help Agent"),
            "run protocol 3": (self.resolve_path('utils\iNetwork-Analyzer.exe'), "Starting Network Analyzer"),
            "run protocol 4": (self.resolve_path('utils\ALT-236.exe'), "NetFrame Control On"),
            "start pass guard": (self.resolve_path('utils\PassGuardX.exe'), "Starting PassGuard X"),
            "run protocol 5": (self.resolve_path(r'utils\net-monitor.exe'), "Starting Network monitoring.")
        }
        asyncio.run(self.short())

    async def short(self):
        try:
            await asyncio.gather(
                self.run_assistant()
            )
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def resolve_path(self, relative_path):
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, relative_path)
        
    def execute_command(self, command):
        if command in self.command_map:
            program, message = self.command_map[command]
            try:
                subprocess.Popen(program, shell=True)  # Start the program
                external_speak(message)
            except FileNotFoundError:
                external_speak("Error: {program} not found!")
            except Exception as e:
                external_speak(f"An error occurred while executing {program}: {e}")
        else:
            self.handle_fallback(command)  # Query Wolfram Alpha for general questions

    def setup_tables(self):
        """Create tables if they don't exist."""
        # memory table
        self.memory_cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                timestamp INTEGER PRIMARY KEY,
                memory_data TEXT
            )
        ''')

        self.memory_conn.commit()

    def load_memories(self):
        """Load memories from the short-term memory database into the in-memory list."""
        self.memory_cursor.execute('SELECT memory_data FROM memory')
        memories = self.memory_cursor.fetchall()
        return [memory[0] for memory in memories]

    def start_background_tasks(self):
        """Start background threads for reminders and automatic deletion."""
        threading.Thread(target=self.reminder_loop, daemon=False).start()
        threading.Thread(target=self.deletion_loop, daemon=False).start()

    def reminder_loop(self):
        import time
        """Periodically remind users of their stored memories."""
        while True:
            time.sleep(self.reminder_interval)
            if not self.suspended:
                self.remind_users()

    def deletion_loop(self):
        import time
        """Automatically delete all stored memories every 24 hours."""
        while True:
            time.sleep(self.deletion_interval)
            self.clear_memories()

    def handle_fallback(self, text):
        import ctypes
        try:
            response = self.nlu.get_response(text)
            logging.info(f'Alpha: {response}')

            # Check if the response includes a web search result with a link
            if "Would you like to open this link? (yes or no)" in response:
                # Show a message box with Yes/No buttons
                user_response = ctypes.windll.user32.MessageBoxW(
                    0, "Would you like to open this link?", "Alpha Assistant", 4
                )

                if user_response == 6:  # 6 = Yes button
                    link = self.extract_link(response)
                    if link:
                        external_speak('Opening link in browser')
                        self.open_link(link)
                    return  # Stop further processing once the link is opened
                elif user_response == 7:  # 7 = No button
                    return  # Stop further processing if the user declines

        except Exception as e:
            logging.error(f"Error in fallback handling: {e}")
    
    async def run_assistant(self):
        import time
        await asyncio.sleep(10)
        #self.wish_me()

        while True:
            if not self.suspended:
                # Ensure 'window' is initialized before accessing its attributes
                if window is not None:
                    if hasattr(window, "loader"):
                        window.loader.setVisible(False)
                    else:
                        logging.error("Error: 'loader' not found in window!")
                else:
                    logging.error("Error: window is not initialized!")

                command = self.recognize_speech()
                if command:
                    if window is not None and hasattr(window, "loader"):
                        window.loader.setVisible(True)
                    self.process_command(command)
                        
            time.sleep(0.000001)  # Minimal sleep to prevent 100% CPU usage

    def recognize_speech(self):
        import time
        import urllib.error
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 500  # Adjust sensitivity
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 1.0  # Makes recognition more responsive

        last_text = ""
        wake_words = ["alpha", "hi alpha", "hey alpha", "hay alpha"]  # List of wake words

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Calibrate mic
            logging.info("Listening...")
            external_speak("I'm Listening...")

            while self.listening:
                try:
                    # Capture longer phrases to avoid truncation
                    audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

                    if not self.is_speech(audio):
                        logging.warning("Ignored non-speech audio.")
                        continue

                    logging.info("Speech detected, recognizing...")
                    self.processing = True

                    try:
                        result = recognizer.recognize_google(audio, show_all=True)

                        if not result or "alternative" not in result:
                            logging.warning("Could not understand audio, retrying...")
                            continue

                        # Extract the best full-length transcription
                        text = result["alternative"][0]["transcript"].lower().strip()
                        logging.info(f"User said: {text}")

                        if len(text) < 3:  # Ignore extremely short phrases
                            logging.warning("Captured incomplete speech, retrying...")
                            continue

                        # Check if any wake word is at the beginning of the text
                        for wake_word in wake_words:
                            if text.startswith(wake_word):
                                command = text[len(wake_word):].strip()
                                if command:
                                    window.loader.setVisible(True)
                                    logging.info(f"Recognized command: {command}")
                                    self.process_command(command)
                                    last_text = command
                                    window.loader.setVisible(False)
                                else:
                                    logging.warning("No command detected after wake word.")
                                break  # Stop checking after detecting a wake word
                        else:
                            logging.warning("No valid wake word detected. Ignoring speech.")

                    except sr.UnknownValueError:
                        logging.warning("Could not understand audio, retrying...")
                        continue  # Retry if recognition fails
                    except sr.RequestError as e:
                        logging.critical(f"Google Speech Recognition request failed: {e}")
                        external_speak("Internet connection required for speech recognition.")
                        logging.error("No internet connection detected. Entering standby mode.")
                        time.sleep(5)  # Wait before retrying to avoid excessive retries
                        continue
                    except urllib.error.URLError:
                        logging.critical("No internet connection. Retrying...")
                        external_speak("Internet connection lost. Please check your connection.")
                        time.sleep(5)
                        continue
                    except TimeoutError:
                        logging.critical("Speech recognition request timed out. Retrying...")
                        external_speak("Request timed out. Please check your internet connection.")
                        time.sleep(5)
                        continue

                    self.processing = False
                    time.sleep(0.5)  # Small delay to avoid immediate reprocessing

                except sr.WaitTimeoutError:
                    continue  # Keep listening if timeout occurs

        return None

    @staticmethod
    def is_speech(audio, threshold=0.000001):
        import numpy as np
        # Get raw data from audio
        audio_data = np.frombuffer(audio.get_raw_data(), np.int16)

        # Normalize audio data to range [0, 1]
        audio_data = np.abs(audio_data) / 32768.0

        # Calculate the average energy of the audio data
        energy = np.mean(audio_data ** 2)

        # Consider it as speech if the energy exceeds the threshold
        return energy > threshold
    
    def extract_link(self, response):
        import re
        """Extract the link from the response text"""
        
        match = re.search(r"Link: (\S+)", response)
        return match.group(1) if match else None

    def open_link(self, link):
        import webbrowser
        """Open the extracted link in the web browser"""
        webbrowser.open(link)

    def main(self):
        import sys
        while True:
            # Read input from stdin
            input_text = sys.stdin.readline().strip()
            if input_text:
                response = self.recognize_speech()
                # Write the response to stdout
                sys.stdout.write(response + "\n")
                sys.stdout.flush()
                # Use the speak function to provide a verbal response
                external_speak(response)

    @staticmethod
    def calculate(command):

        # Strip the command and get the mathematical expression
        expression = command.replace("calculate", "").strip()
        
        # Validate the input expression
        if not expression:
            logging.warning("No expression provided for calculation.")
            external_speak("Please provide a valid mathematical expression to calculate.")
            return

        try:
            # Query Wolfram Alpha
            res = wolfram_alpha_client.query(expression)
            
            # Check if results are available
            if res.results:
                try:
                    # Attempt to get the result
                    answer = next(res.results).text.strip()
                    
                    # Handle case where the result is an empty string or unexpected response
                    if not answer:
                        answer = "Sorry, I couldn't calculate that."
                except StopIteration:
                    # Handle the case where results are exhausted
                    answer = "Sorry, I couldn't calculate that."
            else:
                # Handle the case where there are no results
                answer = "Sorry, I couldn't calculate that."
        
        except wolframalpha.WolframAlphaError as wae:
            # Handle Wolfram Alpha-specific errors
            logging.error(f"WolframAlphaError: {wae}")
            answer = "There was an issue connecting to Wolfram Alpha. Please try again later."
        
        except Exception as e:
            # Handle any other exceptions that might occur
            logging.error(f"Error occurred: {e}")
            answer = f"An error occurred: {str(e)}"
        
        # Log and speak the result
        logging.info(f"Calculation result: {answer}")
        external_speak(answer)

    @staticmethod
    def open_website(command):
        import logging
        import re
        import webbrowser
        # Match the command for 'website <name>'
        match = re.search(r'\bwebsite\s+([a-zA-Z0-9\-\.]+)', command)
        
        if match:
            website = match.group(1).strip().lower()
            
            # Validate that the website name is not empty
            if website:
                # Check if the website already has a domain extension
                if not re.search(r'\.[a-z]{2,}$', website):
                    # If no domain extension, add '.com' by default
                    website = f"{website}.com"
                
                url = f"https://{website}"
                try:
                    # Attempt to open the website
                    webbrowser.open(url)
                    logging.info(f"Opening website: {url}")
                except Exception as e:
                    # Log any errors related to opening the website
                    logging.error(f"Error opening website {url}: {e}")
                    external_speak(f"Sorry, I couldn't open the website {website}. Please try again.")
            else:
                # Handle case of empty website name
                logging.warning("Received an empty website name.")
                external_speak("The website name was empty. Please provide a valid website name.")
        else:
            # If no valid match is found, prompt the user for the correct format
            logging.warning("Invalid command for opening website.")
            external_speak("Please provide a website name after 'website'. For example: 'website google'.")

    @staticmethod
    def search_web(command):
        import logging
        import re
        import webbrowser
        from urllib.parse import quote
        # Match command and ensure it contains the keyword 'search for'
        match = re.search(r'\bsearch for (.+)', command, re.IGNORECASE)
        
        if match:
            query = match.group(1).strip()
            
            if query:  # Ensure the query is not empty
                url = f"https://www.google.com/search?q={quote(query)}"
                try:
                    # Attempt to open the web browser with the query
                    webbrowser.open(url)
                    logging.info(f"Searching the web for: {query}")
                except Exception as e:
                    # Log error if there is an issue opening the browser
                    logging.error(f"Error opening web browser: {e}")
                    external_speak("There was an issue opening the web browser. Please try again.")
            else:
                # Handle empty query
                logging.warning("Empty query received.")
                external_speak("You need to specify what to search for.")
        else:
            # Handle invalid command format
            logging.warning("Invalid search command.")
            external_speak("I didn't catch what you want to search for. Please rephrase.")

    @staticmethod
    def tell_about(command):
        import re
        import wikipedia
        import logging
        # Use a more robust regular expression
        match = re.search(r'\btell me about (.+)', command, re.IGNORECASE)
        
        # Check if the command matches
        if match:
            topic = match.group(1).strip()
            try:
                # Try fetching a summary from Wikipedia
                summary = wikipedia.summary(topic, sentences=2)
                logging.info(f"Here is what I found about {topic}: {summary}")
                external_speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                logging.error(f"DisambiguationError: {e}")
                external_speak("There were multiple matches. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                logging.error(f"PageError: {e}")
                external_speak("I could not find any information on that topic.")
            except wikipedia.exceptions.HTTPTimeoutError as e:
                logging.error(f"HTTPTimeoutError: {e}")
                external_speak("The request timed out. Please try again later.")
            except wikipedia.exceptions.RedirectError as e:
                logging.error(f"RedirectError: {e}")
                external_speak("The page has been redirected. Please try again later.")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                external_speak("An unexpected error occurred. Please try again.")
        else:
            logging.warning("No topic found in the command.")
            external_speak("I didn't catch the topic. Can you rephrase that?")

    def remember_this(self, command):
        try:
            # Extract memory data from the command
            memory_data = self.extract_memory_data(command)

            # Log memory data
            self.log_memory(memory_data)
            external_speak("Would you like to store memory? say yes or no.")

            # Capture user response via speech
            user_input = self.get_speech_input()

            if user_input == 'yes':
                # Store memory data in short-term memory database
                self.store_short_term_memory(memory_data)
                external_speak("Memory was stored.")

            elif user_input == 'no':
                external_speak("Memory was not stored.")

            else:
                external_speak("Invalid response, please respond with 'yes' or 'no'.")
                

            # Update in-memory list of memories
            self.update_memories(memory_data)

        except Exception as e:
            logging.error(f"An error occurred while processing the command: {e}")

    def get_speech_input(self):
        """Use speech recognition to get a response from the user."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            logging.info("Listening for response...")
            audio = recognizer.listen(source)
            try:
                # Convert speech to text
                response = recognizer.recognize_google(audio).lower()
                logging.info(f"User said: {response}")
                return response
            except sr.UnknownValueError:
                external_speak("Sorry, I could not understand your response. Please try again.")
                return self.get_speech_input()  # Retry if speech is unclear
            except sr.RequestError as e:
                external_speak(f"Could not request results; {e}")
                return 'no'  # Default to 'no' if there is a speech recognition issue
        return None

    @staticmethod
    def extract_memory_data(command):
        """Extract the memory data from the command."""
        return command.split("remember", 1)[-1].strip()

    def store_short_term_memory(self, memory_data):
        import time
        """Store the memory data in short-term memory in the SQLite database."""
        timestamp = int(time.time())  # Use current timestamp as primary key
        self.memory_cursor.execute('''
            INSERT INTO memory (timestamp, memory_data) 
            VALUES (?, ?)
        ''', (timestamp, memory_data))
        self.memory_conn.commit()

    @staticmethod
    def log_memory(memory_data):
        """Log the memory to the console or a file."""
        logging.info(f"Memory Stored: {memory_data}")

    def confirm_memory_storage(self):
        """Confirm that the memory was stored successfully."""
        external_speak("Your memory has been stored successfully.")

    def update_memories(self, memory_data):
        """Update the in-memory list of memories."""
        if 'memories' not in self.__dict__:
            self.memories = []
        self.memories.append(memory_data)

    def remind_users(self):
        """Remind users of all stored memories."""
        if self.memories:
            for memory in self.memories:
                external_speak(f"Remember this: {memory}")

    def clear_memories(self):
        """Clear all stored memories."""
        self.memories.clear()
        self.memory_cursor.execute('DELETE FROM memory')
        self.memory_conn.commit()
        external_speak("All stored memories have been deleted.")

    def suspend_assistant(self):
        if hasattr(window, "loader"):
            window.loader.setVisible(False) #listening indicator
        self.suspended = True
        external_speak("Assistant suspended.")
        logging.info("Assistant is suspended.")
        self.listen_for_unsuspend()

    def activate_assistant(self):
        if hasattr(window, "loader"):
            window.loader.setVisible(False) #listening indicator
        self.suspended = False
        external_speak("Assistant unsuspended.")
        logging.info("Assistant is unsuspended.")

    def listen_for_unsuspend(self):
        import time
        """Listen for the 'unsuspend' command while the assistant is suspended."""
        while self.suspended:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                if hasattr(window, "loader"):
                    window.loader.setVisible(True)
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                logging.info(f"User said: {text}")

                if 'unsuspend' in text.lower():
                    self.activate_assistant()
            except sr.UnknownValueError:
                logging.error(f"Could not Recognize speeach.")
            except sr.RequestError as e:
                logging.error(f"Could not request results from Google Speech Recognition service; {e}")

            time.sleep(1)  # Small delay to prevent excessive CPU usage

    def recall_memories(self):
        """Recall and possibly speak out all stored memories from short-term and long-term memory."""
        if self.memories:
            external_speak("Here are the memories I have from short-term memory:")
            for index, memory in enumerate(self.memories, start=1):
                external_speak(f"Memory {index}: {memory}")
        else:
            external_speak("I don't seem to have any short-term memories right now.")

    @staticmethod
    def shutdown():
        logging.info("Shutting down...")
        # Perform shutdown actions here if needed
        os.system("shutdown /s /t 1")

    def exit(self):
        import sys
        """Shutdown assistant (exit program)."""
        try:
            external_speak("Shutting down assistant.")  # Announce shutdown
            self.log_file.close()  # Close log file if it's open
            
            # Close the UI window safely
            if hasattr(self, 'window') and self.window is not None:
                self.window.close()  # Close PyQt UI window properly
                logging.info("UI window closed successfully.")
            
            # Terminate the program gracefully
            logging.info("Shutting down the assistant.")
            sys.exit(0)  # Ensure a clean exit
            
        except Exception as e:
            logging.error(f"Error while shutting down: {e}")
            sys.exit(1)  # Exit with an error code if shutdown fails

    def hibernate(self, command):
        import time
        import re
        try:
            # Extract the duration from the command
            match = re.search(r'hibernate for (\d+) (seconds|minutes|hours)', command)
            if not match:
                raise ValueError("Command format is incorrect. Expected format: 'hibernate for <duration> <unit>'.")

            duration_value = int(match.group(1))
            duration_unit = match.group(2)

            # Convert the duration to seconds for sleep function
            if duration_unit == "minutes":
                duration_value *= 60
            elif duration_unit == "hours":
                duration_value *= 3600
            elif duration_unit != "seconds":
                raise ValueError(f"Unsupported unit of time: {duration_unit}")

            logging.info(f"Hibernating for {duration_value} seconds...")
            external_speak(f"Hibernating for {duration_value} seconds...")
            self.is_sleeping = True
            self.sleep_event.clear()
            time.sleep(duration_value)
            self.is_sleeping = False
            logging.info("Hibernation complete.")
            external_speak(
                f"Hibernation for {duration_value // 60} minutes is complete.")  # Converted to minutes for speech

        except ValueError as ve:
            logging.warning(f"Invalid command format: {ve}")
            external_speak(
                "I'm sorry, I didn't catch that. Please specify the duration and unit in the correct format.")
        except Exception as e:
            logging.error(f"Error hibernating: {e}")
            external_speak("Sorry, there was an error hibernating.")

    def sleep(self):
        logging.info("Going to sleep...")
        # Perform sleep actions here if needed
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    @staticmethod
    def get_time():
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        logging.info(f"The current time is {current_time}")
        external_speak(f"The current time is {current_time}")

    @staticmethod
    def get_date():
        import datetime
        year = datetime.datetime.now().year
        month = datetime.datetime.now().strftime("%B")
        day = datetime.datetime.now().day
        logging.info(f"Today is {month} {day}, {year}")
        external_speak(f"Today is {month} {day}, {year}")

    def process_command(self, command):
        import webbrowser
        from urllib.parse import quote
        logging.info(f"Processing command: {command}")
        command = command.lower().strip()
        
        action_map = {
            'time': self.get_time,
            'date': self.get_date,
            'recall': self.recall_memories,
            'increase volume': lambda: self.change_volume('increase'),
            'decrease volume': lambda: self.change_volume('decrease'),
            'mute': lambda: self.change_volume('mute'),
            'increase brightness': lambda: self.change_brightness('increase'),
            'decrease brightness': lambda: self.change_brightness('decrease'),
            'suspend': self.suspend_assistant,
            'turn on wi-fi': lambda: self.control_wifi('turn on'),
            'turn off wi-fi': lambda: self.control_wifi('turn off'),
            'turn on bluetooth': lambda: self.control_bluetooth('turn on'),
            'turn off bluetooth': lambda: self.control_bluetooth('turn off'),
            'power off': self.shutdown,
            'sleep': self.sleep,
            'exit': self.exit,
            'clear memory': self.clear_memories,
            'clear mem': self.clear_memories,
            'volume max': lambda: self.change_volume_max('increase'),
            'restore audio': lambda: self.change_volume('restore audio'),
            'brightness max': lambda: self.change_brightness_max('increase')
        }
        
        for key, action in action_map.items():
            if key in command:
                return action()
        
        if 'remember' in command:
            self.remember_this(command.split('remember', 1)[-1].strip())
        elif 'install' in command:
            if match := re.search(r'install\s+(.+)', command):
                self.install_application(match.group(1).strip().replace(" ", "_"))
        elif 'maps' in command:
            if location := command.split('maps', 1)[-1].strip():
                webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={quote(location)}")
        elif 'open' in command:
            if match := re.search(r'open\s+(.+)', command):
                self.open_existing_application(match.group(1).strip())
        elif 'calculate' in command:
            self.calculate(command)
        elif 'news' in command:
            if match := re.search(r'news\s*(.+)?', command):
                self.fetch_and_display_news(match.group(1))
        elif 'website' in command:
            self.open_website(command)
        elif 'search for' in command:
            self.search_web(command)
        elif 'tell me about' in command:
            self.tell_about(command)
        elif 'set alarm for' in command:
            self.set_alarm(command)
        elif 'hibernate' in command:
            if match := re.search(r'for (\d+) (seconds?|minutes?)', command):
                duration = int(match.group(1)) * (60 if 'minute' in match.group(2) else 1)
                self.hibernate(duration)
        elif 'play' in command:
            self.handle_music_command(command)
        else:
            self.execute_command(command)

    def log_message(self, message):
        import datetime
        # Log messages to a file
        self.log_file.write(f"{datetime.datetime.now()}: {message}\n")
        self.log_file.flush()

    def close_log(self):
        # Close the log file
        self.log_file.close()
    
    def change_volume(self, action):
        # Fixed volume increment/decrement
        amount = 10  # This is equivalent to 10 units in nircmd

        if action == 'increase':
            subprocess.run(["nircmd.exe", "changesysvolume", str(amount)])
            logging.info("Volume increased by 10 units")
            external_speak("Volume Increased")
        elif action == 'decrease':
            subprocess.run(["nircmd.exe", "changesysvolume", str(-amount)])
            logging.info("Volume decreased by 10 units")
            external_speak("Volume Decreased")
        elif action == 'mute':
            subprocess.run(["nircmd.exe", "mutesysvolume", "1"])
            external_speak("Sound is muted")
        elif action == 'restore audio':
            subprocess.run(["nircmd.exe", "mutesysvolume", "0"])
            external_speak("Sound is unmuted")
        else:
            external_speak("Invalid action. Use 'increase', 'decrease', 'mute', or 'restore audio'.")

    def change_volume_max(self, action):
        # Fixed volume increment/decrement
        amount = 100000  # This is equivalent to 10 units in nircmd

        if action == 'increase':
            subprocess.run(["nircmd.exe", "changesysvolume", str(amount)])
            logging.info("Volume increased to the maximum")
            external_speak("Volume Increased To The Maximum")
        else:
            external_speak("Invalid action. Use 'increase', 'decrease', 'mute', or 'restore audio'.")

    def change_brightness(self, action):
        # Fixed brightness increment/decrement
        amount = 10  # Amount to change brightness (can be adjusted)

        if action == 'increase':
            subprocess.run(["nircmd.exe", "changebrightness", str(amount)])
            logging.info("Brightness increased by 10 units")
            external_speak("Brightness Increased")
        elif action == 'decrease':
            subprocess.run(["nircmd.exe", "changebrightness", str(-amount)])
            logging.info("Brightness decreased by 10 units")
            external_speak("Brightness Decreased")
        else:
            external_speak("Invalid action. Use 'increase' or 'decrease'.")

    def change_brightness_max(self, action):
        # Fixed brightness increment/decrement
        amount = 100000  # Amount to change brightness (can be adjusted)

        if action == 'increase':
            subprocess.run(["nircmd.exe", "changebrightness", str(amount)])
            logging.info("Brightness increased to the maximum")
            external_speak("Brightness Increased To The Maximum")
        else:
            external_speak("Invalid action. Use 'increase' or 'decrease'.")

    def find_236(self, application_name):
        """Attempts to find wifi restore mechanizim"""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, application_name),
            os.path.join(script_dir, 'utils', application_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, application_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def control_wifi(self, action):
        import sys
        if action == 'turn on':
            command = 'Enable-NetAdapter -Name "Wi-Fi" -Confirm:$false'
        elif action == 'turn off':
            command = 'Disable-NetAdapter -Name "Wi-Fi" -Confirm:$false'
        else:
            external_speak("Invalid action. Use 'turn on' or 'turn off'.")
            return

        try:
            # Execute PowerShell command with admin privileges
            subprocess.run(
                [
                    "powershell",
                    "-ExecutionPolicy", "Bypass",
                    "-Command", f"Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command \"{command}\"' -Verb RunAs"
                ],
                check=True
            )
            external_speak(f"Wi-Fi has been {action}")

            # Try to find ALT-236-OFF.exe
            net236_path = self.find_236('utils/ALT-236-OFF.exe')

            # If the file is found, use it; otherwise, fallback
            process236_path = net236_path if net236_path else 'utils/ALT-236-OFF.exe'

            # Ensure the file exists before trying to execute
            if os.path.exists(process236_path):
                self.alt_236_off_process = subprocess.Popen(
                    [process236_path],  
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
                )
            else:
                logging.error(f"ALT-236-OFF.exe not found at {process236_path}")

        except subprocess.CalledProcessError as e:
            external_speak(f"Failed to {action} Wi-Fi. Error: {e}")

    def control_bluetooth(self, action):
        import win32com.client
        try:
            # Initialize WMI service
            wmi_service = win32com.client.GetObject("winmgmts:\\\\.\\root\\cimv2")
            # Query for Bluetooth devices
            query = "SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%Bluetooth%'"
            devices = wmi_service.ExecQuery(query)
            
            if not devices:
                logging.info("No Bluetooth devices found.")
                return
            
            for device in devices:
                # Check if device is already enabled or disabled
                if action == "turn on" and "Disabled" in device.Status:
                    device.Enable()  # Ensure Enable() is called correctly as a method
                    logging.info(f"Bluetooth device '{device.Name}' has been turned on.")
                elif action == "turn off" and "OK" in device.Status:
                    device.Disable()  # Ensure Disable() is called correctly as a method
                    logging.info(f"Bluetooth device '{device.Name}' has been turned off.")
                else:
                    logging.info(f"Bluetooth device '{device.Name}' is already {action}.")
        except Exception as e:
            logging.error(f"Failed to {action} Bluetooth. Error: {e}")

    def set_alarm(self, command):
        import re
        logging.info(f'set_alarm called with command: {command}')  # Debugging statement

        with self.lock:
            if command in self.processed_commands:
                logging.info("Command already processed.")
                return

        # Improved regex to handle "6AM", "6 AM", "9PM", "9 PM" correctly
        match = re.search(r'set alarm (?:for|to)?\s*(\d{1,2})(?::(\d{2}))?\s*(AM|PM|a\.m\.|p\.m\.)?', command, re.IGNORECASE)
        
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2)) if match.group(2) else 0
            period = match.group(3)

            # Convert to proper AM/PM notation
            if period:
                period = period.replace(".", "").upper()  # Normalize "a.m." to "AM"

            if not period:  # Guess AM/PM if not provided
                period = "AM" if hour < 12 else "PM"

            alarm_time = f"{hour}:{minute:02d} {period}"
            self.alarm_time_12 = alarm_time
            self.alarm_time_24 = self.convert_to_24_hour_format(alarm_time)

            if self.alarm_time_24:
                logging.info(f"Alarm set for {alarm_time} ({self.alarm_time_24} in 24-hour format)")
                external_speak(f"Alarm set for {alarm_time}")
                self.alarm_set = True
                
                with self.lock:
                    self.processed_commands.add(command)  # Mark command as processed

                # Start the alarm clock in a new thread
                threading.Thread(target=self.alarm_clock, daemon=False).start()
            else:
                logging.warning("Invalid time format.")
                external_speak("Invalid time format.")
        else:
            logging.warning("Please say the alarm time in the correct format (e.g., '6 AM' or '9:30 PM').")
            external_speak("Please say the alarm time in the correct format (e.g., '6 AM' or '9:30 PM').")

    def set_alarm_thread(self, command):
        logging.warning("set_alarm_thread called with command: %s", command)  # Debugging statement
        threading.Thread(target=self.set_alarm, args=(command,), daemon=False).start()

    @staticmethod
    def convert_to_24_hour_format(alarm_time):
        import re
        match = re.match(r'(\d{1,2}):?(\d{2})?\s*(AM|PM)', alarm_time, re.IGNORECASE)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2)) if match.group(2) else 0
            period = match.group(3).upper()

            if period == 'PM' and hour != 12:
                hour += 12
            elif period == 'AM' and hour == 12:
                hour = 0

            return f"{hour:02d}:{minute:02d}"
        return None

    def alarm_clock(self):
        import time
        import datetime
        """Function to set off an alarm at the specified time."""
        logging.info("Alarm clock thread started")  # Debugging statement
        while self.alarm_set:
            current_time = datetime.datetime.now().strftime("%H:%M")  # Current time in 24-hour format
            if current_time == self.alarm_time_24:
                logging.info("Time to wake up!")
                self.alarm_triggered.set()  # Set the event flag
                self.play_alarm_sound()
                self.alarm_set = False  # Disable the alarm after it goes off
                break
            time.sleep(60)

    # Load the alarm sound file path from the JSON file
    def load_alarm_sound_path(self, json_file="Alarm_sound.json"):
        import json
        try:
            with open(json_file, "r") as file:
                config = json.load(file)
                alarm_sound = config.get("alarm_sound", "Alarm music/Alarm.mp3")
                # Try to find the sound path
                alarm_path = self.find_Alarm_music(alarm_sound)
                if alarm_path:
                    return alarm_path
                else:
                    return self.find_Alarm_music("Alarm music/Alarm.mp3")  # Default if not found
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle the case where the JSON file is missing or corrupt
            return "Alarm music/Alarm.mp3"  # Default sound path if JSON file is missing or corrupted
        
    def find_Alarm_music(self, application_name):
        import os
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, application_name),
            os.path.join(script_dir, 'Alarm music', application_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, application_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    # Play the alarm sound
    def play_alarm_sound(self):
        from pydub.utils import which
        from pydub import AudioSegment
        from pydub.playback import play
        # Set the FFmpeg path manually (update this path if needed)
        ffmpeg_path = self.find_exe('ffmpeg/bin/ffmpeg.exe')  # Try to find the ic
        AudioSegment.converter = which("ffmpeg") or (ffmpeg_path)
        if self.alarm_sound_file:
            try:
                sound = AudioSegment.from_file(self.alarm_sound_file)
                play(sound)
            except Exception as e:
                logging.error(f"Error playing sound: {e}")
        else:
            logging.error("No alarm sound file set.")

    def find_exe(self, application_name):
        import os
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, application_name),
            os.path.join(script_dir, 'ffmpeg', application_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, application_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def check_alarm(self):
        """This function runs in the main thread and checks if the alarm has triggered."""
        logging.info("Checking alarm...")  # Debugging statement
        while True:
            self.alarm_triggered.wait()  # Wait until the event flag is set
            external_speak("Time to wake up!")
            self.alarm_triggered.clear()  # Reset the event flag for the next alarm

    def get_youtube_video_url(self, query):
        from youtube_search import YoutubeSearch
        results = YoutubeSearch(query, max_results=1).to_dict()
        if results:
            return "https://www.youtube.com" + results[0]['url_suffix']
        return None

    def play_music(self, music_name):
        import webbrowser
        search_query = f"{music_name} music"
        video_url = self.get_youtube_video_url(search_query)

        if video_url:
            webbrowser.open(video_url)
            logging.info(f"Playing '{music_name}' on YouTube.")
        else:
            logging.info(f"Could not find '{music_name}' on YouTube.")

    def handle_music_command(self, text):
        music_name = text.lower().replace("play", "").strip()
        self.play_music(music_name)

    @staticmethod
    def open_existing_application(application_name):
        import platform
        try:
            os_system = platform.system()
            application_name = application_name.lower()

            app_map = {
                'windows': {
                    'chrome': 'chrome', 'firefox': 'firefox', 'edge': 'microsoft-edge:',
                    'ie': 'iexplore', 'internet explorer': 'iexplore', 'notepad': 'notepad',
                    'calculator': 'calc', 'explorer': 'explorer', 'file explorer': 'explorer',
                    'control panel': 'control', 'task manager': 'taskmgr', 'settings': 'ms-settings:',
                    'windows settings': 'ms-settings:'
                },
                'darwin': {'chrome': 'Google Chrome', 'firefox': 'Firefox', 'safari': 'Safari'},
                'linux': {'chrome': 'google-chrome', 'firefox': 'firefox'}
            }

            command = app_map.get(os_system.lower(), {}).get(application_name)
            if command:
                if os_system == 'Windows':
                    subprocess.Popen(['start', command], shell=True)
                elif os_system == 'Darwin':
                    subprocess.Popen(['open', '-a', command])
                elif os_system == 'Linux':
                    subprocess.Popen([command])
                logging.info(f"Opening {application_name}.")
                external_speak(f"Opening {application_name}.")
            else:
                raise ValueError(f"Application '{application_name}' not recognized on {os_system}.")
        except Exception as e:
            logging.error(f"Error opening '{application_name}': {str(e)}")
            external_speak(f"Error opening '{application_name}': {str(e)}")

    @staticmethod
    def install_application(command):
        import shutil
        import time
        import re
        application_name = re.search(r'install (.+)', command).group(1)

        # Check if Chocolatey is available in the system PATH
        if shutil.which("choco") is None:
            logging.error("Chocolatey is not installed or not found in PATH.")
            external_speak("Chocolatey is not installed. Installing now...")

            try:
                # Install Chocolatey via PowerShell
                subprocess.run([
                    'powershell',
                    '-Command',
                    'Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))'
                ], check=True)
                external_speak("Chocolatey has been installed. Please wait while we proceed with the application installation.")

                # Wait for Chocolatey to be installed before proceeding
                time.sleep(60)  # Adjust this time if necessary, to give Chocolatey enough time to install

                # Now retry installing the application
                Brain._install_with_output(application_name)
            
            except subprocess.CalledProcessError as e:
                logging.error(f"Error installing Chocolatey or application: {e}")
                external_speak("There was an error installing Chocolatey or the application.")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                external_speak("An unexpected error occurred.")
        else:
            try:
                # Chocolatey is installed, proceed with application installation
                Brain._install_with_output(application_name)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error installing application: {e}")
                external_speak(f"There was an error installing {application_name}.")
    
    @staticmethod
    def _install_with_output(application_name):
        # Open a new window and display output using 'start' command
        subprocess.Popen(
            ['cmd', '/C', f'start choco install {application_name} -y'],  # 'start' opens a new window
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        external_speak(f"Installation process for {application_name} has started.")

    @staticmethod
    def fetch_and_display_news(news_category=None):
        import webbrowser
        from bs4 import BeautifulSoup
        try:
            # Check if a news category was provided; if not, default to general news
            if news_category:
                # Open the news category URL in the default web browser
                google_news_url = f'https://news.google.com/{news_category}'
                webbrowser.open(google_news_url, new=2)
                logging.info(f"Opening {news_category} news in the browser.")
                external_speak(f"Opening {news_category} news in the browser.")
            else:
                import requests
                # Fetch news from Google News RSS feed
                url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
                response = requests.get(url)
                content = response.content
                soup = BeautifulSoup(content, "html.parser")
                articles = soup.findAll("item")

                # Construct the news summary
                speak_news = "The news for today are as follows:"
                for i, article in enumerate(articles, start=1):
                    if i > 5:  # Limit to top 5 news articles
                        break
                    title = article.find("title").text
                    speak_news += f" {i}. {title}. "

                # Speak out the news summary
                external_speak(speak_news)
                logging.info(speak_news)

        except Exception as e:
            logging.error(f"Error: {e}")
            external_speak(f"An error occurred while fetching the news: {e}")

    @staticmethod
    def open_news_in_browser(news_category):
        import webbrowser
        # Define the Google News URL based on the news category
        google_news_url = f'https://news.google.com/{news_category}'

        try:
            # Open the news URL in the default web browser
            webbrowser.open(google_news_url, new=2)

        except Exception as e:
            logging.error(f"Error opening news in browser: {e}")

    def wake(self):
        """Wake up the assistant immediately."""
        if self.is_sleeping:
            logging.info("Waking up the assistant...")
            external_speak("Waking up now...")
            self.is_sleeping = False
            self.sleep_event.set()  # Ensure that any waiting on the sleep event is notified
        else:
            logging.info("The assistant is already awake.")
            external_speak("I am already awake.")

    def listen_for_wake_word(self):
        import time
        """Continuously listen for the wake word."""
        while self.is_sleeping:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                logging.info("Listening for wake word...")
                if window is not None and hasattr(window, "loader"):
                        window.loader.setVisible(True)
                external_speak("Listening for wake word...")  # Notify that it's listening

                audio = recognizer.listen(source)

            try:
                logging.info("Recognizing...")
                if window is not None and hasattr(window, "loader"):
                        window.loader.setVisible(False)
                text = recognizer.recognize_google(audio)
                logging.info(f"User said: {text}")

                if 'wake' in text.lower():
                    self.wake()  # Wake the assistant up
            except sr.UnknownValueError:
                logging.info("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                logging.info(f"Could not request results from Google Speech Recognition service; {e}")

        # Sleep briefly to avoid high CPU usage
        time.sleep(1)

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.correct_code = "00000"  # Manually specified correct code
        self.init_ui()
    
    def init_ui(self):
        from PyQt6.QtGui import QFont
        from PyQt6.QtGui import QIcon, QPixmap
        self.setWindowTitle("Authentication")
        self.setFixedSize(500, 300)
        icon_path = self.find_icon('background/icon.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))
        
        layout = QVBoxLayout(self)

        # Load and display the image
        image_label = QLabel(self)
        icon_path = self.find_icon('background/icon.png')  

        if icon_path:
            pixmap = QPixmap(icon_path)
        else:
            pixmap = QPixmap()  # Empty fallback

        scaled_pixmap = pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        self.label = QLabel("Enter Access Code:")
        self.label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Enter your Authentication code")
        self.code_input.setFixedSize(300, 40)
        self.code_input.setFont(QFont("Arial", 11))
        self.code_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(-50)  # Reduce spacing between widgets
        layout.addWidget(self.code_input, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.submit_button = QPushButton("OK")
        self.submit_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.submit_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        self.submit_button.clicked.connect(self.check_code)
        layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None
    
    def check_code(self):
        if self.code_input.text() == self.correct_code:
            self.open_main_interface()
        else:
            QMessageBox.warning(self, "Access Denied", "Incorrect Code. Please try again.")
    
    def open_main_interface(self):
        quest.show()
        self.close()

def check_program_installed(program_name):
    import shutil
    return shutil.which(program_name) is not None

class QuestionnaireApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        from PyQt6.QtWidgets import (
            QVBoxLayout, QLabel
        )
        from PyQt6.QtGui import QFont, QIcon, QPixmap
        from PyQt6.QtCore import Qt, QTimer, QUrl
        import os
        self.setWindowTitle("Alpha-X")
        self.setFixedSize(710, 450) # Adjust window size
        icon_path = self.find_icon('background/icon.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        self.completed_label = QLabel("AI engine is booting up, please hold on.\nBooting in 40 seconds...")
        self.completed_label.setFont(QFont("Arial", 14))
        self.completed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Load and display the image
        image_label = QLabel(self)
        icon_path = self.find_icon('background/icon.png')  

        if icon_path:
            pixmap = QPixmap(icon_path)
        else:
            pixmap = QPixmap()  # Empty fallback

        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Loader widget
        self.loader = Loader() # Placeholder for actual loader
        self.loader.setFixedSize(30, 40)
        self.loader.setVisible(True)
        self.loader.setStyleSheet(
            "background-color: #ffffff; color: #E0E0E0; padding: 10px; border-radius: 5px;"
        )

        # Layout setup
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(image_label)
        main_layout.addWidget(self.loader, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.completed_label)
        self.setLayout(main_layout)

        # Initialize countdown but do NOT start it
        self.countdown_time = 40
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)

        # Check and display missing apps
        self.missing_apps = self.check_and_display_programs()

        self.setLayout(main_layout)

    def showEvent(self, event):
        """ Start the timer only when the window is shown. """
        super().showEvent(event)
        self.check_internet_and_start_timer()

    def check_and_display_programs(self):
        # List of programs to check
        programs = [
            "choco",  # Chocolatey
            "cmake",  # CMake
            "ffmpeg",  # FFmpeg
            "nircmd",  # NirCmd
            "nmap"  # Nmap
        ]
        
        # List to store missing applications
        missing_apps = []

        # Check for each program and display the result
        for program in programs:
            installed = check_program_installed(program)
            status = "Installed" if installed else "Not Installed"
            self.completed_label.setText(f"{program}: {status}\n" + self.completed_label.text())
            if not installed:
                missing_apps.append(program)

        return missing_apps
    
    def check_internet(self):
        import socket
        """Check for internet connectivity."""
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    def check_internet_and_start_timer(self):
        """Check internet connectivity and handle countdown timer accordingly."""
        if self.check_internet():
            if not self.timer.isActive():  # Only start if it's not running
                self.timer.start(1000)  
            self.completed_label.setText(f"AI engine is booting up, please hold on.\nBooting in {self.countdown_time} seconds...")
        else:
            self.completed_label.setText("No internet connection. Retrying...")
            if not hasattr(self, 'retry_timer'):
                self.retry_timer = QTimer(self)
                self.retry_timer.timeout.connect(self.check_internet_and_start_timer)
            if not self.retry_timer.isActive():
                self.retry_timer.start(3000)  # Retry every 3s, only if not already active

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None
    
    def update_countdown(self):
        """Updates the countdown message, pauses if no internet, and closes the app when time runs out."""

        if not self.check_internet():
            self.completed_label.setText("Internet lost. Pausing countdown...")
            self.timer.stop()  # Pause countdown
            self.check_internet_and_resume()  # Retry internet check
            return

        self.countdown_time -= 1
        self.completed_label.setText(f"AI engine is booting up, please hold on.\nBooting in {self.countdown_time} s")

        if self.countdown_time <= 0:
            self.timer.stop()
            self.loader.setVisible(False)

            if self.missing_apps:
                self.show_missing_apps_message()
            else:
                # Delay showing main window and closing boot screen
                QTimer.singleShot(10000, show_main_window)  # Use `self.show_main_window`
                QTimer.singleShot(12000, self.close)

    def check_internet_and_resume(self):
        """Continuously checks for internet connection and resumes countdown when restored."""
        if self.check_internet():
            if hasattr(self, 'retry_timer') and self.retry_timer.isActive():
                self.retry_timer.stop()
            self.completed_label.setText(f"Internet restored! Resuming boot in {self.countdown_time} s")
            if not self.timer.isActive():
                self.timer.start(1000)  # Resume countdown
        else:
            if not hasattr(self, 'retry_timer'):
                self.retry_timer = QTimer(self)
                self.retry_timer.timeout.connect(self.check_internet_and_resume)
            if not self.retry_timer.isActive():
                self.retry_timer.start(3000)  # Retry after 3s


    def show_missing_apps_message(self):
        """Displays a message box showing the missing applications."""
        missing_apps = ', '.join(self.missing_apps)
        message = f'The following applications are missing or not added to the PATH:<br>{missing_apps}<br>Please install or add them to the PATH and restart the application. \n if not installed install at: <a href="https://github.com/headlessripper/Mount_Utils/releases/download/0.0.0.0.0/Mount_Utils.7z">Mount_Utils</a>'
        self.completed_label.setText(f"AI engine not able to boot\n missing dependency: {missing_apps}")
        
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Missing Applications")
        msg.setText("Missing Applications")
        msg.setInformativeText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def closeEvent(self, event):
        """Ensure all timers are stopped when closing."""
        if self.timer.isActive():
            self.timer.stop()
        if hasattr(self, 'retry_timer') and self.retry_timer.isActive():
            self.retry_timer.stop()
        super().closeEvent(event)

class SettingsWindow(QWidget):
    def __init__(self):
        from PyQt6.QtGui import QIcon
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(400, 550)
        icon_path = self.find_icon('background/icon.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))

        self.config = self.load_config(CONFIG_FILE)
        self.tts_config = self.load_config(TTS_CONFIG_FILE)
        self.alarm_config = self.load_config(ALARM_SOUND_FILE, default={"alarm_sound": DEFAULT_ALARM_SOUND})

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # API Key Field
        self.api_key_label = QLabel("API Key:")
        self.api_key_input = QLineEdit(self.config.get("API_KEY", ""))
        layout.addWidget(self.api_key_label)
        layout.addWidget(self.api_key_input)

        # Alarm Sound Selection
        self.alarm_label = QLabel("Alarm Sound File:")
        self.alarm_input = QLineEdit(self.alarm_config.get("alarm_sound", DEFAULT_ALARM_SOUND))
        self.alarm_button = QPushButton("Browse")
        self.alarm_button.clicked.connect(self.select_alarm_sound)

        alarm_layout = QHBoxLayout()
        alarm_layout.addWidget(self.alarm_input)
        alarm_layout.addWidget(self.alarm_button)
        
        layout.addWidget(self.alarm_label)
        layout.addLayout(alarm_layout)

        # Enable Notifications Checkbox
        self.notifications_checkbox = QCheckBox("Enable Notifications")
        layout.addWidget(self.notifications_checkbox)

        # Theme Selection
        self.theme_label = QLabel("Select Theme:")
        self.theme_combobox = QComboBox()
        self.theme_combobox.addItems(["Light", "Dark", "System Default"])
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_combobox)

        # Font Size Selector
        self.font_label = QLabel("Font Size:")
        self.font_spinbox = QSpinBox()
        self.font_spinbox.setRange(8, 24)
        self.font_spinbox.setValue(12)
        layout.addWidget(self.font_label)
        layout.addWidget(self.font_spinbox)

        # Volume Control (TTS Volume)
        self.volume_label = QLabel("TTS Volume:")
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(self.tts_config.get("volume", 50))
        layout.addWidget(self.volume_label)
        layout.addWidget(self.volume_slider)

        # TTS Rate Control
        self.rate_label = QLabel("TTS Rate:")
        self.rate_slider = QSlider(Qt.Orientation.Horizontal)
        self.rate_slider.setRange(50, 300)
        self.rate_slider.setValue(self.tts_config.get("rate", 180))
        layout.addWidget(self.rate_label)
        layout.addWidget(self.rate_slider)

        # Gender Selection (TTS Voice)
        self.gender_label = QLabel("Voice Gender:")
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        layout.addWidget(self.gender_label)
        layout.addWidget(self.male_radio)
        layout.addWidget(self.female_radio)

        # Bio Text Area
        self.bio_label = QLabel("Bio:")
        self.bio_text = QTextEdit()
        layout.addWidget(self.bio_label)
        layout.addWidget(self.bio_text)

        # Divider Line
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        # Buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        self.cancel_button = QPushButton("Close")
        self.cancel_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")

        self.save_button.clicked.connect(self.save_settings)
        self.cancel_button.clicked.connect(self.cancel_settings)
        self.reset_button.clicked.connect(self.reset_settings)

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.reset_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def find_icon(self, icon_name):
        import os
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def load_config(self, filename, default=None):
        import json
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default if default is not None else {}

    def select_alarm_sound(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Alarm Sound", "", "Audio Files (*.mp3 *.wav *.ogg)")
        if file_path:
            self.alarm_input.setText(file_path)

    def save_settings(self):
        import json
        # Save API key to config.json
        self.config["API_KEY"] = self.api_key_input.text()
        with open(CONFIG_FILE, "w") as file:
            json.dump(self.config, file, indent=4)

        # Save Alarm Sound
        self.alarm_config["alarm_sound"] = self.alarm_input.text()
        with open(ALARM_SOUND_FILE, "w") as file:
            json.dump(self.alarm_config, file, indent=4)

        # Save TTS settings
        self.tts_config["volume"] = self.volume_slider.value()
        self.tts_config["rate"] = self.rate_slider.value()
        selected_voice = self.get_selected_voice()
        self.tts_config["voice"] = selected_voice if selected_voice is not None else "default"

        with open(TTS_CONFIG_FILE, "w") as file:
            json.dump(self.tts_config, file, indent=4)

        QMessageBox.information(self, "Settings saved.!", "Your settings have been save restart application for them to take effect.")

    def get_selected_voice(self):
        if self.male_radio.isChecked():
            for voice in voices:
                if "david" in voice.name.lower() and "microsoft" in voice.name.lower():
                    return voice.id
        elif self.female_radio.isChecked():
            for voice in voices:
                if "zira" in voice.name.lower() and "microsoft" in voice.name.lower():
                    return voice.id
        return None

    def cancel_settings(self):
        #logging.info("Settings closed.")
        self.close()

    def reset_settings(self):
        logging.info(f"Settings reset.")
        self.api_key_input.clear()
        self.alarm_input.setText(DEFAULT_ALARM_SOUND)
        self.notifications_checkbox.setChecked(False)
        self.theme_combobox.setCurrentIndex(0)
        self.font_spinbox.setValue(12)
        self.volume_slider.setValue(50)
        self.rate_slider.setValue(180)
        self.male_radio.setChecked(False)
        self.female_radio.setChecked(False)
        self.bio_text.clear()

def load_commands():
    import requests
    try:
        response = requests.get(COMMANDS_JSON_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict) and "commands" in data:
            return data["commands"]
        return {}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching commands.json: {e}")
        return {}

class CommandPopup(QDialog):
    def __init__(self, command, description):
        from PyQt6.QtGui import QIcon
        from PyQt6.QtWidgets import QScrollArea
        super().__init__()
        self.setWindowTitle(command)
        self.setStyleSheet("background-color: #000000; border-radius: 15px; padding: 10px; QScrollArea { border: none; background-color: #ffffff; border-radius: 10px; padding: 5px;}")

        self.setFixedSize(250, 150)
        layout = QVBoxLayout()

        icon_path = self.find_icon('ICON/help.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('ICON/help.png'))

        label = QLabel(f"<b>{command}</b><br>{description}")
        label.setWordWrap(True)

        # Create a QScrollArea and set the label as its widget
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(label)
        
        # Add the scroll area to the layout
        layout.addWidget(self.scroll_area)
        
        # Create the close button and add it to the layout
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("QPushButton{background-color: #ff0000; color: #ffffff; border-radius: 5px; padding: 5px;} QPushButton:hover {background-color: #ffffff; color: #000000;}")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        self.setLayout(layout)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

class PingThread(QThread):
    ping_result = pyqtSignal(int)  # Signal to send ping result

    def run(self):
        while True:
            try:
                if sys.platform == "win32":
                    result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
                
                output = result.stdout

                if "time=" in output:
                    ping_time = int(output.split("time=")[-1].split("ms")[0].strip())
                else:
                    ping_time = 0  # If no ping response, set to 0

            except Exception:
                ping_time = 0  # Handle any errors

            self.ping_result.emit(ping_time)  # Emit signal
            import time
            time.sleep(1)  # Wait 1 second before pinging again

class DashboardWindow(QMainWindow):
    def __init__(self):
        from PyQt6.QtGui import QIcon
        from PyQt6.QtWidgets import QScrollArea
        import psutil
        super().__init__()
        self.setWindowTitle("System Dashboard")
        self.setGeometry(50, 50, 500, 380)
        self.setStyleSheet(self.load_stylesheet())
        icon_path = self.find_icon('ICON/icons8-hub-50 (1).png')

        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('ICON/icons8-hub-50 (1).png'))
        
        self.setup_tray_icon()

        self.layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)
        scroll_layout = QVBoxLayout(scroll_content)

        # Add system monitoring widgets
        scroll_layout.addWidget(self.create_system_monitor_display())
        scroll_layout.addWidget(self.create_system_stats_section())
        scroll_layout.addWidget(self.create_additional_monitoring_section())

        self.layout.addWidget(scroll_area)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.ping_value = 0  # Store latest ping value
        self.ping_thread = PingThread()
        self.ping_thread.ping_result.connect(self.update_ping)
        self.ping_thread.start()

        # Timer to update system stats every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system_stats)
        self.timer.start(1000)

        self.sound_thread = None

        # For network speed calculation
        self.prev_bytes_received = psutil.net_io_counters().bytes_recv
        self.prev_bytes_sent = psutil.net_io_counters().bytes_sent

        logging.info("DashboardWindow initialized successfully.")

    def setup_tray_icon(self):
        from PyQt6.QtGui import QIcon, QAction
        from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
        """Setup system tray icon with menu."""
        icon_path = self.find_icon('ICON/icons8-hub-50 (1).png')
        
        if icon_path:
            self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)

        else:
            self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
        tray_menu = QMenu()

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def update_ui(self, cpu_usage, ram_usage, disk_usage, temperature, download_speed, upload_speed):
        from PyQt6.QtCore import Qt, QMetaObject
        """Updates the progress bars and charts."""
        QMetaObject.invokeMethod(self, "updateProgressBars", Qt.ConnectionType.QueuedConnection, cpu_usage, ram_usage, disk_usage, temperature, download_speed, upload_speed)

    def load_stylesheet(self):
        """Returns the enhanced futuristic neon stylesheet."""
        return """
            /* Main Window */
            QMainWindow {
                background: linear-gradient(135deg, #121212, #1a1a1a);
                border: none;
                color: #00ffcc;
                border-radius: 15px;
            }
            QLabel {
                color: #00ffcc;
                font-size: 16px;
                font-family: "Roboto", sans-serif;
                font-weight: 400;
                letter-spacing: 1px;
            }
            QProgressBar {
                text-align: center;
                color: #00cc99;
                border: none;
                border-radius: 15px;
                background: rgba(0, 255, 204, 0.1);
                height: 20px;
                margin: 20px 0;
            }
            QProgressBar::chunk {
                border-radius: 15px;
                background: linear-gradient(135deg, #00ff99, #00cc99);
            }
        """

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None
    
    def update_ping(self, ping_value):
        """Update the ping progress bar and store value."""
        self.ping_value = ping_value
        self.temp_bar.findChild(QProgressBar).setValue(ping_value)


    def create_system_monitor_display(self):
        from PyQt6.QtGui import QFont
        """Creates a system monitoring display."""
        frame = QFrame()
        layout = QVBoxLayout(frame)

        self.monitor_label = QLabel("Loading system stats...")
        self.monitor_label.setFont(QFont("Roboto", 18))
        self.monitor_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.monitor_label.setStyleSheet("color: #ff6600;")
        layout.addWidget(self.monitor_label)

        return frame

    def create_limit_spinbox(self, default_value):
        """Create a QSpinBox with range 0-100 and a default value."""
        spinbox = QSpinBox()
        spinbox.setRange(0, 100)
        spinbox.setValue(default_value)
        return spinbox

    def create_system_stats_section(self):
        """Creates the center section for system stats with a grid layout."""
        frame = QFrame()
        layout = QGridLayout(frame)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.cpu_bar = self.create_progress_bar("CPU")
        self.ram_bar = self.create_progress_bar("RAM")
        self.disk_bar = self.create_progress_bar("Disk")
        self.temp_bar = self.create_progress_bar("Ping")

        layout.addWidget(self.cpu_bar, 0, 0)
        layout.addWidget(self.ram_bar, 0, 1)
        layout.addWidget(self.disk_bar, 1, 0)
        layout.addWidget(self.temp_bar, 1, 1)

        return frame

    def create_progress_bar(self, title):
        from PyQt6.QtGui import QFont
        """Creates a compact progress bar with a title."""
        frame = QFrame()
        layout = QVBoxLayout(frame)
        label = QLabel(title)
        label.setFont(QFont("Roboto", 14, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)
        progress_bar.setValue(0)
        progress_bar.setFixedHeight(20)

        layout.addWidget(label)
        layout.addWidget(progress_bar)

        return frame

    def create_additional_monitoring_section(self):
        from PyQt6.QtWidgets import QListWidget
        """Creates the bottom section for additional monitoring (network, battery, processes)."""
        frame = QFrame()
        layout = QVBoxLayout(frame)
        self.network_label = QLabel("Network: 0 KB/s")
        self.battery_label = QLabel("Battery: N/A")
        self.process_list = QListWidget()

        layout.addWidget(self.network_label)
        layout.addWidget(self.battery_label)
        layout.addWidget(self.process_list)

        return frame

    def update_system_stats(self):
        import psutil
        """Update the system stats displayed on the dashboard."""
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        # Network speed calculation
        curr_bytes_received = psutil.net_io_counters().bytes_recv
        curr_bytes_sent = psutil.net_io_counters().bytes_sent

        download_speed = (curr_bytes_received - self.prev_bytes_received) / 1024  # KB/s
        upload_speed = (curr_bytes_sent - self.prev_bytes_sent) / 1024  # KB/s

        self.prev_bytes_received = curr_bytes_received
        self.prev_bytes_sent = curr_bytes_sent

        # Check if psutil can fetch temperature data
        try:
            temperature = psutil.sensors_temperatures().get('coretemp', [])[0].current if psutil.sensors_temperatures() else 0
        except AttributeError:
            temperature = 0

        # Update progress bars (ensure values are integers)
        self.cpu_bar.findChild(QProgressBar).setValue(int(cpu_usage))
        self.ram_bar.findChild(QProgressBar).setValue(int(ram_usage))
        self.disk_bar.findChild(QProgressBar).setValue(int(disk_usage))
        self.temp_bar.findChild(QProgressBar).setValue(self.ping_value)  # Update ping bar

        # Update network speed display
        self.network_label.setText(f"Download: {download_speed:.2f} KB/s | Upload: {upload_speed:.2f} KB/s")

        # Update system monitor label
        self.monitor_label.setText(f"CPU: {int(cpu_usage)}% | RAM: {int(ram_usage)}% | Disk: {int(disk_usage)}% | Ping: {self.ping_value}ms")

        # Restart ping thread periodically
        if not self.ping_thread.isRunning():
            self.ping_thread.start()

class DisplayImage(QWidget):
    def __init__(self):
        from PyQt6.QtGui import QIcon, QPixmap
        super().__init__()
        layout = QVBoxLayout()
        set_dark_theme(self)
        # Load and display the image
        image_label = QLabel(self)

        # Try to find the image using `find_icon`
        icon_path = self.find_icon('background/icon.png')  # Try to find the image

        if icon_path:
            pixmap = QPixmap(icon_path)  # Load the found image
        else:
            pixmap = QPixmap()  # Load an empty pixmap as a fallback

        # Scale the pixmap properly
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # Set the scaled pixmap to the QLabel
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        self.setLayout(layout)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

class Home(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)
        
        button_names = ["Settings", "System Monitor", "Password Manager", "Anonymous Search", "Command Menu", "License Agreement", "Version Info", "Usage Policy", "Restart", "Anti Virus", "AIWS"] #Alpha Interface for Windows Security
        
        # Creating and adding stacked buttons with consistent size
        for i, name in enumerate(button_names, start=1):
            button = QPushButton(name)
            button.setFixedHeight(50)  # Uniform height for better UI
            button.setStyleSheet("""
                QPushButton {
                    background-color: #252526;
                    color: white;
                    font-size: 16px;
                    border: none;
                    padding: 10px;
                    text-align: center;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #007ACC;
                }
                QPushButton:pressed {
                    background-color: #005F9E;
                }
            """)
            button.clicked.connect(getattr(self, f"button_{i}_clicked"))
            layout.addWidget(button)
    
    def button_1_clicked(self):
        sett.show()
    
    def button_2_clicked(self):
        dash.show()

    def button_3_clicked(self):
        app_path = self.find_utils4("utils\\PassGuardX.exe")
        try:
            subprocess.Popen([app_path])
        except Exception as e:
            logging.error(f"Error opening application: {e}")

    def button_4_clicked(self):
        app_path = self.find_utils4("utils\\AnonySearch.exe")
        try:
            subprocess.Popen([app_path])
        except Exception as e:
            logging.error(f"Error opening application: {e}")
    
    def button_5_clicked(self):
        app_path = self.find_utils4("utils\\HELP.exe")
        try:
            subprocess.Popen([app_path])
        except Exception as e:
            logging.error(f"Error opening application: {e}")

    def button_9_clicked(self):
        self.restart_alpha_x(tts_engine)
        
    def button_10_clicked(self):
        app_path = self.find_utils4("utils\\PYAS.exe")
        try:
            subprocess.Popen([app_path])
        except Exception as e:
            logging.error(f"Error opening application: {e}")

    def button_11_clicked(self):
        app_path = self.find_utils4("utils\\WSM.exe")
        try:
            subprocess.Popen([app_path])
        except Exception as e:
            logging.error(f"Error opening application: {e}")

    def button_6_clicked(self):
        """Open the license file and display it in a message box."""
        # Open a file dialog to let the user select the license file
        file_path = self.find_icon("dependencies/licence")

        if (file_path):
            try:
                # Read the content of the license file
                with open(file_path, 'r') as file:
                    license_content = file.read()

                # Create a custom dialog for displaying the license
                dialog = QDialog(self)
                dialog.setWindowTitle("License Information")
                dialog.setFixedSize(QSize(600, 400))  # Set the dialog size

                # Create a QTextEdit widget to display the license content
                text_edit = QTextEdit(dialog)
                text_edit.setPlainText(license_content)
                text_edit.setReadOnly(True)  # Make the text read-only

                # Create a QScrollArea to make the QTextEdit scrollable
                from PyQt6.QtWidgets import QScrollArea
                scroll_area = QScrollArea(dialog)
                scroll_area.setWidgetResizable(True)
                scroll_area.setWidget(text_edit)

                # Set the layout of the dialog
                layout = QVBoxLayout(dialog)
                layout.addWidget(scroll_area)

                # Show the dialog
                dialog.exec()

            except Exception as e:
                # Handle file reading errors
                error_box = QMessageBox(self)
                error_box.setWindowTitle("Error")
                error_box.setText(f"Error reading file: {e}")
                error_box.exec()
        else:
            # Handle the case where the file does not exist
            error_box = QMessageBox(self)
            error_box.setWindowTitle("File Not Found")
            error_box.setText(f"License file not found at path: {file_path}")
            error_box.exec()

    def button_7_clicked(self):
        """Open and display the license file in a scrollable dialog."""
        
        file_path = self.find_icon("dependencies/licence.key")

        if not (file_path):
            # Handle the case where the file does not exist
            QMessageBox.critical(self, "File Not Found", f"License file not found at: {file_path}")
            return

        try:
            # Read the content of the license file
            with open(file_path, 'r', encoding='utf-8') as file:
                license_content = file.read()

            # Create a modal dialog
            dialog = QDialog(self)
            dialog.setWindowTitle("Version Info")
            dialog.setFixedSize(QSize(600, 400))  # Set the dialog size

            # Create a QTextEdit widget to display the license content
            text_edit = QTextEdit()
            text_edit.setPlainText(license_content)
            text_edit.setReadOnly(True)  # Make the text read-only

            # Create a QScrollArea to make the QTextEdit scrollable
            from PyQt6.QtWidgets import QScrollArea
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(text_edit)

            # Set the layout of the dialog
            layout = QVBoxLayout()
            layout.addWidget(scroll_area)
            dialog.setLayout(layout)

            # Show the dialog
            dialog.exec()

        except Exception as e:
            # Handle file reading errors
            QMessageBox.critical(self, "Error", f"Error reading file: {e}")

    def button_8_clicked(self):
        """Open the license HTML file and display it in a message box."""
        # Define the path to the license file (HTML file)
        file_path = self.find_icon("dependencies/Usage.html")

        if file_path:
            try:
                # Ensure the file exists
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
                
                # Read the content of the HTML license file
                with open(file_path, 'r') as file:
                    license_content = file.read()

                # Create a custom dialog for displaying the license
                dialog = QDialog(self)
                dialog.setWindowTitle("Usage")
                dialog.setFixedSize(QSize(600, 400))  # Set the dialog size

                # Create a QTextEdit widget to display the license content
                text_edit = QTextEdit(dialog)
                text_edit.setHtml(license_content)  # Use setHtml() to render HTML content
                text_edit.setReadOnly(True)  # Make the text read-only

                # Create a QScrollArea to make the QTextEdit scrollable
                from PyQt6.QtWidgets import QScrollArea
                scroll_area = QScrollArea(dialog)
                scroll_area.setWidgetResizable(True)
                scroll_area.setWidget(text_edit)

                # Set the layout of the dialog
                layout = QVBoxLayout(dialog)
                layout.addWidget(scroll_area)

                # Show the dialog
                dialog.exec()

            except Exception as e:
                # Handle any file reading errors or other issues
                error_box = QMessageBox(self)
                error_box.setWindowTitle("Error")
                error_box.setText(f"Error reading file: {str(e)}")
                error_box.exec()
        else:
            # Handle the case where the file does not exist
            error_box = QMessageBox(self)
            error_box.setWindowTitle("File Not Found")
            error_box.setText(f"Usage file not found at path: {file_path}")
            error_box.exec()

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'dependencies', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def find_utils4(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'utils', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path

    def restart_alpha_x(self, tts_engine):
        import time
        """Stops all non-main threads, stops the TTS engine, and restarts Alpha-X."""
        # Stop all non-main threads
        for thread in threading.enumerate():
            if thread is not threading.main_thread():
                try:
                    logging.info(f"Attempting to stop thread: {thread.name}")
                    thread.join(timeout=1)
                except Exception as e:
                    logging.error(f"Error stopping thread {thread.name}: {e}")

        # Stop the TTS engine gracefully if it's running
        if tts_engine:
            try:
                logging.info("Stopping TTS engine before restart.")
                tts_engine.stop()
                tts_engine = None
            except Exception as e:
                logging.error(f"Error stopping TTS engine: {e}")

        time.sleep(1)  # Wait briefly before shutting down

        # Dynamically get the user's profile path
        user_profile = os.getenv("USERPROFILE")
        if user_profile:
            app_exe_path = os.path.join("C:\\", "Users", os.path.basename(user_profile), "AppData", "Local", "Programs", "Alpha-X", "Alpha-X.exe")
            logging.info(f"Alpha-X executable path: {app_exe_path}")

            if os.path.exists(app_exe_path):
                try:
                    subprocess.Popen([app_exe_path], close_fds=True)
                    QMessageBox.information(self, "Restarting", "Alpha-X.exe will restart.")
                except Exception as e:
                    logging.error(f"Error launching Alpha-X.exe: {e}")

        os._exit(0)  # Force exit after launching the new instance
        return None

def set_dark_theme(self):
    """Set dark theme for the application."""
    dark_stylesheet = """
    QWidget {
        background-color: #898181;
    }
    """
    self.setStyleSheet(dark_stylesheet)

class DisplayImage(QWidget):
    from PyQt6.QtGui import QPixmap
    def __init__(self):
        from PyQt6.QtGui import QPixmap
        super().__init__()
        layout = QVBoxLayout()
        set_dark_theme(self)
        # Load and display the image
        image_label = QLabel(self)

        # Try to find the image using `find_icon`
        icon_path = self.find_icon('background/icon.png')  # Try to find the image

        if icon_path:
            pixmap = QPixmap(icon_path)  # Load the found image
        else:
            pixmap = QPixmap()  # Load an empty pixmap as a fallback

        # Scale the pixmap properly
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # Set the scaled pixmap to the QLabel
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        self.setLayout(layout)

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None
from PyQt6.QtGui import QSyntaxHighlighter
class PythonSyntaxHighlighter(QSyntaxHighlighter):
    """Modernized Python Syntax Highlighter with improved styles."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlight_rules = []
        
        def create_format(color, bold=False):
            from PyQt6.QtGui import QFont, QTextCharFormat, QColor
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(color))
            if bold:
                fmt.setFontWeight(QFont.Weight.Bold)
            return fmt
        
        # Define styles using modern colors (Dracula theme)
        self.keyword_format = create_format("#ff79c6", True)
        self.class_format = create_format("#8be9fd", True)
        self.function_format = create_format("#50fa7b")
        self.comment_format = create_format("#6272a4")
        self.string_format = create_format("#f1fa8c")
        self.number_format = create_format("#bd93f9")
        
        # Keywords
        keywords = [
            "def", "class", "return", "import", "from", "as", "if", "elif", "else", "while",
            "for", "try", "except", "with", "self", "True", "False", "None", "and", "or", "not",
            "is", "in", "lambda", "raise", "finally", "del", "global", "nonlocal"
        ]
        self.highlight_rules += [(QRegularExpression(rf'\b{kw}\b'), self.keyword_format) for kw in keywords]
        
        # Class and Function Definitions
        self.highlight_rules.append((QRegularExpression(r'\bclass\s+([A-Za-z_][A-Za-z0-9_]*)'), self.class_format))
        self.highlight_rules.append((QRegularExpression(r'\bdef\s+([A-Za-z_][A-Za-z0-9_]*)'), self.function_format))
        
        # Strings, Comments, and Numbers
        self.highlight_rules.append((QRegularExpression(r'"[^"]*"|\'[^\']*\'|"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''), self.string_format))
        self.highlight_rules.append((QRegularExpression(r"#.*"), self.comment_format))
        self.highlight_rules.append((QRegularExpression(r'\b\d+\b'), self.number_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.highlight_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)

class OutputWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Make the window frameless but still have a custom title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)  
        self.setWindowTitle("Termux")
        
        # Set window border and background
        self.setStyleSheet("background: transparent; border: 2px solid #f8f8f2; border-radius: 8px;")
        
        # Create the frame to contain output area and buttons (with a border)
        frame = QFrame(self)
        frame.setStyleSheet("background: transparent; border: 2px solid #f8f8f2; border-radius: 8px;")

        # Create output area
        self.output_area = QPlainTextEdit(frame)
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("background-color: #1e1e1e; color: #f8f8f2; padding: 8px; border-radius: 8px;")
        self.output_area.setFixedHeight(150)

        # Create Close Button
        self.close_button = QPushButton("❌", frame)
        self.close_button.setStyleSheet("color: white; border: none; border-radius: 10px; padding: 5px;")
        self.close_button.clicked.connect(self.close_window)
        self.close_button.setFixedSize(30, 30)

        # Create Clear Button
        self.clear_button = QPushButton("Clear", frame)
        self.clear_button.setStyleSheet("color: white; background-color: #ffb86c; border: none; border-radius: 10px; padding: 5px;")
        self.clear_button.clicked.connect(self.clear_output)
        self.clear_button.setFixedSize(50, 30)

        # Create a horizontal layout for buttons (Close and Clear)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.close_button)
        button_layout.setSpacing(10)  # Add some space between the buttons

        # Layout Setup for the frame
        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(self.output_area)
        frame_layout.addLayout(button_layout)  # Add the button layout here
        frame.setLayout(frame_layout)

        # Main layout of the window, add the frame to the window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

        # For dragging functionality
        self._drag_position = None

    def update_output(self, output):
        self.output_area.appendPlainText(output)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self._drag_position:
            delta = event.globalPosition().toPoint() - self._drag_position
            self.move(self.pos() + delta)
            self._drag_position = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self._drag_position = None

    def close_window(self):
        self.close()

    def clear_output(self):
        """Clears the output area."""
        self.output_area.clear()

    def paintEvent(self, event):
        from PyQt6.QtGui import QPainter, QColor
        # Paint the window with complete transparency
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Completely transparent background, keeping only the UI elements visible
        painter.fillRect(self.rect(), QColor(0, 0, 0, 0))  # Ensuring no background is visible
        super().paintEvent(event)

class CodeEditor(QWidget):
    from PyQt6.QtGui import QDragEnterEvent, QDropEvent
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.process = None
        self.setAcceptDrops(True)  # Enable drag-and-drop
        self.init_ui()

    def init_ui(self):
        from PyQt6.QtGui import QFont
        layout = QVBoxLayout()
        splitter = QSplitter(Qt.Orientation.Horizontal)  # Split horizontally for side panels and editor

        # Primary Side Panel (Fixed width)
        self.primary_panel = QWidget()
        self.primary_panel.setFixedWidth(80)
        self.primary_panel.setStyleSheet("background-color: #1f1e1e; border-radius: 8px; padding: 8px;")

        self.primary_panel_layout = QVBoxLayout()
        self.primary_panel_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Secondary Panel (Right - File Explorer)
        self.secondary_panel = QWidget()
        self.secondary_panel.setStyleSheet("background-color: #484848; color: #f8f8f2; border-radius: 8px; padding: 8px;")
        self._add_file_explorer(self.secondary_panel)
        self.secondary_panel.setMinimumWidth(50)
        self.secondary_panel.setMaximumWidth(300)
        self.secondary_panel.hide()

        # Common button style
        button_style = """
            QPushButton {
                background-color: #6272a4;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #7a1818;
                color: black;
            }
        """

        # Buttons for the primary panel with images
        from PyQt6.QtGui import QIcon
        self.open_fol = QPushButton()
        icon_path1 = self.find_icon(r'ICON\menu\folder.png') 
        self.open_fol.setIcon(QIcon(icon_path1))  # Path to image
        self.open_fol.setIconSize(QSize(24, 24))  # Adjust icon size

        self.open_file_btn = QPushButton()
        icon_path2 = self.find_icon(r'ICON\menu\file.png') 
        self.open_file_btn.setIcon(QIcon(icon_path2))
        self.open_file_btn.setIconSize(QSize(24, 24))

        self.new_file_btn = QPushButton()
        icon_path3 = self.find_icon(r'ICON\menu\new-file.png') 
        self.new_file_btn.setIcon(QIcon(icon_path3))
        self.new_file_btn.setIconSize(QSize(24, 24))

        self.settings_btn = QPushButton()
        icon_path4 = self.find_icon('ICON\menu\settings.png') 
        self.settings_btn.setIcon(QIcon(icon_path4))
        self.settings_btn.setIconSize(QSize(24, 24))

        self.find_btn = QPushButton()
        icon_path5 = self.find_icon('ICON\menu\search.png') 
        self.find_btn.setIcon(QIcon(icon_path5))
        self.find_btn.setIconSize(QSize(24, 24))

        self.terminal_btn = QPushButton()
        icon_path6 = self.find_icon(r'ICON\menu\terminal.png') 
        self.terminal_btn.setIcon(QIcon(icon_path6))
        self.terminal_btn.setIconSize(QSize(24, 24))

        self.run_btn = QPushButton()
        icon_path7 = self.find_icon(r'ICON\menu\run.png') 
        self.run_btn.setIcon(QIcon(icon_path7))
        self.run_btn.setIconSize(QSize(24, 24))

        self.toggle_fileview_btn = QPushButton()
        icon_path8 = self.find_icon(r'ICON\menu\toggle.png') 
        self.toggle_fileview_btn.setIcon(QIcon(icon_path8))
        self.toggle_fileview_btn.setIconSize(QSize(24, 24))

        # Apply style and connect signals
        for btn in [self.open_fol,self.open_file_btn, self.new_file_btn, self.settings_btn, self.find_btn, self.terminal_btn, self.run_btn, self.toggle_fileview_btn]:
            btn.setStyleSheet(button_style)
            self.primary_panel_layout.addWidget(btn)

        # Connect buttons to actions
        self.open_fol.clicked.connect(self.open_folder)
        self.new_file_btn.clicked.connect(self.new_file)
        self.settings_btn.clicked.connect(self.open_settings)
        self.find_btn.clicked.connect(self.find_text)
        self.terminal_btn.clicked.connect(self.open_terminal)
        self.run_btn.clicked.connect(self.run_code)
        self.open_file_btn.clicked.connect(self.open_file)
        self.toggle_fileview_btn.clicked.connect(self.secondary_panel.show)

        self.primary_panel.setLayout(self.primary_panel_layout)

        # Editor Area (Center)
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Write your Python code here 🟢🔵🟠")
        self.editor.setFont(QFont("Courier", 12))
        self.editor.setStyleSheet("""
            background-color: #484848 ;
            color: #f8f8f2;
            border-radius: 8px;
            padding: 8px;
        """)
        self.highlighter = PythonSyntaxHighlighter(self.editor.document())
        self.output_window = OutputWindow()
        self.output_window.hide()  # Keep it hidden initially

        # Set up buttons and file actions
        #button_layout = QHBoxLayout()
        #self._add_action_buttons(button_layout)

        # Add widgets to the splitter
        splitter.addWidget(self.primary_panel)
        splitter.addWidget(self.secondary_panel)
        splitter.addWidget(self.editor)

        layout.addWidget(splitter)
        #layout.addLayout(button_layout)
        self.setLayout(layout)

        # Initial window size
        self.setMinimumSize(800, 600)

        # Keyboard Shortcuts
        self.setup_shortcuts()

    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def _add_primary_buttons(self, layout):
        # Group file operation buttons
        buttons = [
            ("📂", self.open_folder),
            ("📝", self.open_file),
            ("🆕", self.new_file),
            ("⚙️", self.open_settings),
            ("🔍", self.find_text),
            ("</>", self.open_terminal),
            ("▶️", self.run_code)
        ]
        for text, action in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(action)
            layout.addWidget(btn)

    def _add_file_explorer(self, panel):
        from PyQt6.QtGui import QFileSystemModel
        from PyQt6.QtCore import QDir
        from PyQt6.QtWidgets import QTreeView
        # Setup the file explorer panel
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(QDir.rootPath())

        self.explorer = QTreeView()
        self.explorer.setModel(self.file_system_model)
        self.explorer.setRootIndex(self.file_system_model.index(QDir.rootPath()))
        self.explorer.setStyleSheet("background-color: #484848; color: #f8f8f2;")
        self.explorer.setIconSize(QSize(32, 32))
        self.explorer.setColumnHidden(1, True)  # Hide Size column
        self.explorer.setColumnHidden(2, True)  # Hide Type column
        self.explorer.setColumnHidden(3, True)  # Hide Date Modified column
        self.explorer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        from PyQt6.QtWidgets import QSizePolicy
        self.explorer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        explorer_layout = QVBoxLayout()
        explorer_layout.addWidget(self.explorer)
        panel.setLayout(explorer_layout)

    #def _add_action_buttons(self, layout):

        #self.open_button = QPushButton("📝 Open")
        #self.open_button.clicked.connect(self.open_file)

        #self.save_button = QPushButton("💾 Save")
        #self.save_button.clicked.connect(self.save_file)

        #for btn in [self.open_button, self.save_button, self.run_button]:
            #layout.addWidget(btn)

    def setup_shortcuts(self):
        from PyQt6.QtGui import QKeySequence, QShortcut
        # Setup keyboard shortcuts for common actions
        QShortcut(QKeySequence("Ctrl+S"), self).activated.connect(self.save_file)
        QShortcut(QKeySequence("Ctrl+O"), self).activated.connect(self.open_file)
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(self.run_code)
        QShortcut(QKeySequence("Ctrl+Z"), self).activated.connect(self.editor.undo)
        QShortcut(QKeySequence("Ctrl+Y"), self).activated.connect(self.editor.redo)

    def open_folder(self):
        """Fix the issue with setting root index"""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        
        if file_dialog.exec() == QFileDialog.Accepted:
            selected_folder = file_dialog.selectedFiles()[0]
            self.explorer.setRootIndex(self.file_system_model.index(selected_folder))  # Now it works correctly
            
    def open_file(self):
        # Open file dialog to select a file
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setFilter("Python Files (*.py)")
        if file_dialog.exec() == QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            with open(selected_file, "r", encoding="utf-8") as file:
                self.editor.setPlainText(file.read())
            self.current_file = selected_file

    def save_file(self):
        if not self.current_file:
            self.current_file, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py)")
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(self.editor.toPlainText())

    def run_code(self):
        # Run the Python code in the editor
        import subprocess
        code = self.editor.toPlainText()
        if not code.strip():
            QMessageBox.warning(self, "Run Code", "No code to run!")
            return

        process = subprocess.Popen(
            ["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        stdout, stderr = process.communicate()

        if stderr:
            self.output_window.update_output(f"Error: {stderr}")
        else:
            self.output_window.update_output(stdout)

    def open_settings(self):
        # Placeholder for settings
        QMessageBox.information(self, "Settings", "Settings panel is under development!")

    def find_text(self):
        # Find text in editor
        text, ok = QInputDialog.getText(self, "Find Text", "Enter text to find:")
        if ok and text:
            cursor = self.editor.document().find(text)
            if cursor.isNull():
                QMessageBox.information(self, "Find", "Text not found!")
            else:
                self.editor.setTextCursor(cursor)

    def new_file(self):
        self.editor.clear()
        self.current_file = None

    def find_text(self):
        text, ok = QInputDialog.getText(self, "Find Text", "Enter text to find:")
        if ok and text:
            cursor = self.editor.document().find(text)
            if cursor.isNull():
                QMessageBox.information(self, "Find", "Text not found!")
            else:
                self.editor.setTextCursor(cursor)

    def open_terminal(self):
        os.system("start cmd")  # Opens the Windows command prompt

    def toggle_editor(self):
        # Toggle the visibility of the editor
        if self.editor.isVisible():
            self.editor.hide()
        else:
            self.editor.show()

    def setup_shortcuts(self):
        from PyQt6.QtGui import QKeySequence
        from PyQt6.QtGui import QShortcut
        QShortcut(QKeySequence("Ctrl+S"), self).activated.connect(self.save_file)
        QShortcut(QKeySequence("Ctrl+O"), self).activated.connect(self.open_file)
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(self.run_code)
        QShortcut(QKeySequence("Ctrl+Z"), self).activated.connect(self.editor.undo)  # Undo with Ctrl+Z
        QShortcut(QKeySequence("Ctrl+Y"), self).activated.connect(self.editor.redo)  # Redo with Ctrl+Y

    def check_and_install_python(self, installer_path):
        import shutil
        """
        Checks if Python is installed. If not, runs the Python installer.
        :param installer_path: Path to the Python installer executable.
        """
        try:
            # Check if Python is installed
            python_path = shutil.which("python") or shutil.which("python3")
            if python_path:
                print(f"Python is installed at: {python_path}")
            else:
                print("Python is not installed. Running the installer...")
                if os.path.exists(installer_path):
                    subprocess.run([installer_path], check=True)
                else:
                    print("Installer not found at the specified path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def find_depends(self, icon_name):
            """Attempts to find the icon in and out of the script's directory."""
            script_dir = os.path.dirname(os.path.realpath(__file__))

            possible_paths = [
                os.path.join(script_dir, icon_name),
                os.path.join(script_dir, 'dependencies', icon_name),
                os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
            ]

            for path in possible_paths:
                if os.path.exists(path):
                    return path

            return None

    def run_code(self):
        import shutil
        code = self.editor.toPlainText()
        if not code.strip():
            self.output_window.update_output("No code to execute!")
            return

        # Define the installer path (update this to the actual path)
        installer_path = self.find_depends("dependencies/python-3.9.7-amd64.exe")

        # Check if Python is installed, and install it if necessary
        python_path = shutil.which("python") or shutil.which("python3")
        if not python_path:
            self.output_window.update_output("Python not found. Installing...")
            self.check_and_install_python(installer_path)

        # Proceed with execution after installation
        if self.process and self.process.state() == QProcess.ProcessState.Running:
            self.process.terminate()

        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.process.readyRead.connect(self.update_output)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w', encoding="utf-8") as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        self.process.start("python", [temp_file_path])

        # Show the output window when the run button is clicked
        self.output_window.show()

    def update_output(self):
        if self.process:
            output = self.process.readAll().data().decode()
            self.output_window.update_output(output)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Allow drag if file URL is detected"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        """Handle file drop and open its contents"""
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()  # Get the first dropped file path
            if os.path.isfile(file_path):  # Ensure it's a file
                self.open_file_dragged(file_path)

    def save_file(self):
        if not hasattr(self, "current_file"):
            self.current_file = None  # Ensure attribute exists

        options = QFileDialog.Options()
        options |= QFileDialog.Option.DontUseNativeDialog  # Avoid native dialogs if problematic

        if not self.current_file:
            self.current_file, _ = QFileDialog.getSaveFileName(self, "Save File", os.path.expanduser("~/Documents"), "Python Files (*.py)", options=options)

        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(self.editor.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")

    def open_file(self):
        # Open the file dialog to select files or folders
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)  # Allow file selection
        file_dialog.setOption(QFileDialog.Option.ShowDirsOnly, False)  # Allow showing files and directories
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        
        # Open file or open folder options
        result = file_dialog.exec()
        selected_files = file_dialog.selectedFiles()
        
        if result == QFileDialog.Accepted:
            selected_path = selected_files[0]
            
            # Check if selected path is a directory or a file
            if os.path.isdir(selected_path):  # If folder is selected
                # Ask user if they want to open the folder
                reply = QMessageBox.question(self, "Open Folder", 
                                            f"Do you want to open the folder: {selected_path}?", 
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    self.explorer.setRootIndex(self.file_system_model.index(selected_path))
                    self.secondary_panel.show()
            else:  # If file is selected
                # Ask user if they want to open the file
                reply = QMessageBox.question(self, "Open File", 
                                            f"Do you want to open the file: {selected_path}?", 
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    with open(selected_path, "r", encoding="utf-8") as file:
                        self.editor.setPlainText(file.read())
                    self.current_file = selected_path

    def open_file_dragged(self, file_path):
        """Read and display the file contents in the editor"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.editor.setPlainText(content)  # Display file contents in the editor
        except Exception as e:
            self.editor.setPlainText(f"Error opening file: {e}")  # Handle errors gracefully

    def open_folder(self):
        # Open file dialog to select a folder
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)  # Set mode to select directories only
        file_dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)  # Only show directories
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        
        # Open dialog and get selected folder
        if file_dialog.exec() == QFileDialog.Accepted:
            selected_folder = file_dialog.selectedFiles()[0]  # Get the selected folder path
            
            # Ask user if they want to open the selected folder
            reply = QMessageBox.question(self, "Open Folder", 
                                        f"Do you want to open the folder: {selected_folder}?", 
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.explorer.setRootIndex(self.file_system_model.index(selected_folder))

class PowerUsageWorker(QRunnable):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def run(self):
        import psutil
        battery = psutil.sensors_battery()
        power_usage = battery.percent if battery else 0
        self.callback(power_usage)

class PowerUsageWorker(QRunnable):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def run(self):
        import psutil
        battery = psutil.sensors_battery()
        power_usage = battery.percent if battery else 0
        self.callback(power_usage)

class SystemMonitor(QWidget):
    power_updated = pyqtSignal(int)
    def __init__(self):
        import psutil
        super().__init__()
        self.setStyleSheet(self.get_stylesheet())
        
        self.network_data = {"sent": [], "received": []}
        self.last_net_io = psutil.net_io_counters()
        
        self.threadpool = QThreadPool.globalInstance()
        self.power_updated.connect(self.update_power_usage)

        self.init_ui()
        self.init_timer()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.cpu_label, self.cpu_progress = self.create_stat_widget("CPU Usage")
        self.memory_label, self.memory_progress = self.create_stat_widget("Memory Usage")
        self.disk_label, self.disk_progress = self.create_stat_widget("Disk Usage")
        self.power_label, self.power_progress = self.create_stat_widget("Battery")
        
        plot_layout = QHBoxLayout()
        self.network_canvas, self.network_ax = self.create_plot("Network Speed (MB/s)")
        
        plot_layout.addWidget(self.network_canvas)
        
        self.process_table = self.create_process_table()
        
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_progress)
        layout.addWidget(self.memory_label)
        layout.addWidget(self.memory_progress)
        layout.addWidget(self.disk_label)
        layout.addWidget(self.disk_progress)
        layout.addWidget(self.power_label)
        layout.addWidget(self.power_progress)
        layout.addLayout(plot_layout)
        layout.addWidget(QLabel("Top Processes:", self))
        layout.addWidget(self.process_table)
        
        self.setLayout(layout)
    
    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)
    
    def create_stat_widget(self, label_text):
        label = QLabel(label_text, self)
        progress_bar = QProgressBar(self)
        progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label, progress_bar
    
    def create_plot(self, title):
        from matplotlib.figure import Figure
        figure = Figure(figsize=(4, 3))
        ax = figure.add_subplot(111)
        figure.patch.set_facecolor('#121212')
        ax.set_facecolor('#1e1e1e')
        ax.set_title(title, color='white')
        ax.set_ylabel("Usage", color='white')
        ax.grid(color='#444', linestyle='--', linewidth=0.5)
        canvas = FigureCanvas(figure)
        return canvas, ax
    
    def create_process_table(self):
        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["PID", "Process Name", "CPU %"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        return table
    
    def update_stats(self):
        import psutil
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        self.update_progress_bar(self.cpu_progress, cpu_usage)
        self.update_progress_bar(self.memory_progress, memory_usage)
        self.update_progress_bar(self.disk_progress, disk_usage)

        # Run power usage check in a separate thread
        self.threadpool.start(PowerUsageWorker(self.power_updated.emit))

        self.update_network_usage()
        self.update_process_table()

    def update_power_usage(self, power_usage):
        self.update_progress_bar(self.power_progress, power_usage)
    
    def update_progress_bar(self, bar, value):
        bar.setValue(int(value))
        color = "#50fa7b" if value < 50 else "#ffb86c" if value < 80 else "#ff5555"
        bar.setStyleSheet(f"QProgressBar::chunk {{ background-color: {color}; }}")
    
    def update_network_usage(self):
        import psutil
        current_net_io = psutil.net_io_counters()
        sent_speed = (current_net_io.bytes_sent - self.last_net_io.bytes_sent) / (1024 ** 2)
        recv_speed = (current_net_io.bytes_recv - self.last_net_io.bytes_recv) / (1024 ** 2)
        self.last_net_io = current_net_io
        
        self.network_data["sent"].append(sent_speed)
        self.network_data["received"].append(recv_speed)
        
        if len(self.network_data["sent"]) > 60:
            self.network_data["sent"].pop(0)
            self.network_data["received"].pop(0)
        
        self.network_ax.clear()
        self.network_ax.plot(self.network_data["sent"], label='Sent (MB/s)', color='red')
        self.network_ax.plot(self.network_data["received"], label='Received (MB/s)', color='orange')
        self.network_ax.set_title("Network Speed Over Time", color='white')
        self.network_ax.set_xlabel("Time (s)", color='white')
        self.network_ax.set_ylabel("Speed (MB/s)", color='white')
        self.network_ax.legend()
        self.network_canvas.draw()
    
    def update_process_table(self):
        import psutil
        self.process_table.setRowCount(0)
        processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:5]
        
        for index, process in enumerate(processes):
            self.process_table.insertRow(index)
            self.process_table.setItem(index, 0, QTableWidgetItem(str(process.info['pid'])))
            self.process_table.setItem(index, 1, QTableWidgetItem(process.info['name']))
            self.process_table.setItem(index, 2, QTableWidgetItem(f"{process.info['cpu_percent']:.1f}%"))
    
    def get_stylesheet(self):
        return """
            QWidget {
                color: #ffffff;
                font-family: Arial;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            QProgressBar {
                border: 2px solid #333;
                border-radius: 5px;
                background-color: #222;
                text-align: center;
                height: 20px;
            }
            QProgressBar::chunk {
                border-radius: 5px;
            }
            QTableWidget {
                background-color: #1e1e1e;
                border: 1px solid #333;
                gridline-color: #333;
            }
            QTableWidget::item {
                padding: 8px;
            }
        """

class PacketSniffer(QThread):
    packet_captured = pyqtSignal(str)
    
    def __init__(self):
        import threading
        super().__init__()
        self.stop_event = threading.Event()  # Event to stop the sniffer

    def run(self):
        import scapy.all as scapy
        """Starts the packet sniffer."""
        self.stop_event.clear()  # Ensure the stop event is clear when starting the sniffing
        scapy.sniff(prn=self.process_packet, store=False, stop_filter=self.should_stop)

    def process_packet(self, packet):
        """Processes and emits packet details."""
        self.packet_captured.emit(packet.summary())

    def should_stop(self, packet):
        """Check if the sniffing should stop."""
        return self.stop_event.is_set()

    def stop(self):
        """Stops the sniffer gracefully."""
        self.stop_event.set()  # Set the stop event to stop sniffing

class NetworkAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        #self.setWindowTitle("Network Analyzer")
        self.setStyleSheet("color: #ffffff;") #background-color: #1e1e1e; 
        
        layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.scan_button = QPushButton("🔍 Scan Network")
        #self.scan_button.setStyleSheet(self.get_button_style())
        self.scan_button.setStyleSheet("QPushButton { padding: 12px; background-color: #484848; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        self.scan_button.clicked.connect(self.scan_network)

        self.network_table = QTableWidget()
        self.network_table.setColumnCount(3)
        self.network_table.setHorizontalHeaderLabels(["IP Address", "MAC Address", "Vendor"])
        self.network_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.network_table.setStyleSheet("background-color: #2b2b2b; color: #ffffff; font-size: 12px;")

        self.packet_output = QTextEdit()
        self.packet_output.setReadOnly(True)
        self.packet_output.setStyleSheet("background-color: black; color: lime; font-family: Consolas; font-size: 12px;")

        self.start_sniffing_button = QPushButton("▶️ Start Packet Capture")
        self.start_sniffing_button.setStyleSheet("QPushButton { padding: 12px; background-color: #484848; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        #.start_sniffing_button.setStyleSheet(self.get_button_style())
        self.start_sniffing_button.clicked.connect(self.start_sniffing)

        self.stop_sniffing_button = QPushButton("⏹ Stop Packet Capture")
        self.stop_sniffing_button.setStyleSheet("QPushButton { padding: 12px; background-color: #484848; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        #self.stop_sniffing_button.setStyleSheet(self.get_button_style())
        self.stop_sniffing_button.clicked.connect(self.stop_sniffing)
        self.stop_sniffing_button.setEnabled(False)

        layout.addWidget(self.label)
        layout.addWidget(self.scan_button)
        layout.addWidget(self.network_table)
        layout.addWidget(self.start_sniffing_button)
        layout.addWidget(self.stop_sniffing_button)
        layout.addWidget(self.packet_output)
        self.setLayout(layout)

    def get_button_style(self):
        """Returns modern button styling."""
        return (
            "background-color: #0078D7; color: white; border-radius: 5px; padding: 8px;"
            "font-weight: bold; font-size: 14px;"
        )

    def get_local_ip_range(self):
        import netifaces
        """Dynamically fetches the local IP address and subnet mask to generate the correct IP range."""
        try:
            interface = netifaces.gateways()["default"][netifaces.AF_INET][1]  # Get the default network interface
            addresses = netifaces.ifaddresses(interface)
            ip_info = addresses[netifaces.AF_INET][0]
            
            ip_address = ip_info["addr"]
            netmask = ip_info["netmask"]
            
            # Convert netmask to CIDR notation (e.g., 255.255.255.0 -> /24)
            cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
            return f"{ip_address}/{cidr}"
        except Exception as e:
            print(f"Error getting local IP range: {e}")
            return "192.168.1.1/24"  # Fallback range

    def scan_network(self):
        import scapy.all as scapy
        """Scans the local network dynamically."""
        self.network_table.setRowCount(0)
        ip_range = self.get_local_ip_range()  # Get dynamic IP range
        print(f"Scanning network: {ip_range}")  # Debug print

        try:
            arp_request = scapy.ARP(pdst=ip_range)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

            print(f"Devices found: {len(answered_list)}")  # Debug print

            for index, element in enumerate(answered_list):
                ip = element[1].psrc
                mac = element[1].hwsrc
                vendor = self.get_mac_vendor(mac)

                print(f"Device: {ip} - {mac} - {vendor}")  # Debug print

                self.network_table.insertRow(index)
                self.network_table.setItem(index, 0, QTableWidgetItem(ip))
                self.network_table.setItem(index, 1, QTableWidgetItem(mac))
                self.network_table.setItem(index, 2, QTableWidgetItem(vendor))
        except Exception as e:
            print(f"Error: {e}")  # Debug print
            QMessageBox.critical(self, "Error", f"Failed to scan network: {str(e)}")

    def get_mac_vendor(self, mac_address):
        import requests
        """Fetches the MAC address vendor."""
        try:
            response = requests.get(f"https://api.macvendors.com/{mac_address}")
            return response.text if response.status_code == 200 else "Unknown"
        except:
            return "Unknown"

    def start_sniffing(self):
        """Starts packet capturing."""
        self.sniffer_thread = PacketSniffer()
        self.sniffer_thread.packet_captured.connect(self.display_packet)
        self.sniffer_thread.start()
        self.start_sniffing_button.setEnabled(False)
        self.stop_sniffing_button.setEnabled(True)

    def stop_sniffing(self):
        """Stops packet capturing."""
        if hasattr(self, "sniffer_thread"):
            self.sniffer_thread.stop()
            self.sniffer_thread.quit()
            self.sniffer_thread.wait()

        self.start_sniffing_button.setEnabled(True)
        self.stop_sniffing_button.setEnabled(False)


    def display_packet(self, packet):
        """Displays captured packets."""
        self.packet_output.append(f"<font color='lightgray'>{packet}</font>")

class Terminal(QWidget):
    def __init__(self):
        super().__init__()

        self.shell = "powershell.exe"  # Default to PowerShell
        self.process = QProcess(self)  # QProcess for real-time execution
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)  # Merge stdout and stderr
        self.process.readyRead.connect(self.read_output)  # Read output when available

        # Main layout
        main_layout = QVBoxLayout()

        # QTextEdit widget to display terminal output
        self.output_display = QTextEdit(self)
        self.output_display.setReadOnly(True)  # Make it read-only so user can't type in it
        self.output_display.setStyleSheet("""
            background-color: black;
            color: lightgreen;
            font-family: Consolas, 'Courier New', monospace;
            font-size: 14px;
            padding: 5px;
        """)  # Style for terminal output
        main_layout.addWidget(self.output_display)

        # QLineEdit widget for user input
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter command here...")
        self.input_field.setStyleSheet("""
            background-color: black;
            color: lightgreen;
            font-family: Consolas, 'Courier New', monospace;
            font-size: 14px;
            padding: 5px;
        """)  # Style for user input
        self.input_field.returnPressed.connect(self.send_command)  # Send command on Enter
        main_layout.addWidget(self.input_field)

        # Start PowerShell
        self.start_shell()

        # Set layout
        self.setLayout(main_layout)

        # Set window properties
        self.setWindowTitle("Terminal")
        self.setGeometry(100, 100, 800, 600)

    def start_shell(self):
        """Starts the PowerShell shell in the background."""
        if self.process.state() == QProcess.ProcessState.Running:
            self.process.kill()  # Kill the previous process if already running
        self.process.start(self.shell)  # Start the PowerShell process

    def read_output(self):
        """Reads output from the PowerShell shell and displays it in the QTextEdit."""
        output = self.process.readAll().data().decode("utf-8").strip()
        if output:
            self.output_display.append(output)  # Append output to the QTextEdit widget

    def send_command(self):
        """Handles the user input command and sends it to the PowerShell process."""
        command = self.input_field.text().strip()
        if command:
            self.process.write((command + "\n").encode("utf-8"))
            self.process.waitForBytesWritten()  # Ensure the command is sent
            self.input_field.clear()  # Clear the input field

    def closeEvent(self, event):
        """Override close event to kill the process before exiting."""
        self.process.kill()  # Kill the process before closing
        event.accept()  # Accept the event to close the window

    def __del__(self):
        """Destructor to ensure the process is killed if not already."""
        if self.process.state() == QProcess.ProcessState.Running:
            self.process.kill()

class FileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.current_path = os.path.expanduser("~")
        self.init_ui()
        self.load_directory()

    def init_ui(self):
        """Initializes the UI with a modern design."""
        main_layout = QVBoxLayout()
        
        # Navigation Bar
        nav_layout = QHBoxLayout()
        self.back_button = QPushButton(qta.icon("mdi.arrow-left"), " Back")
        self.back_button.clicked.connect(self.go_back)
        self.path_label = QLabel(self.current_path)
        self.path_label.setStyleSheet("font-weight: bold; font-size: 16px;")  # Increased font size
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.path_label)
        
        # File Tree View
        self.file_tree = QTreeWidget()
        self.file_tree.setColumnCount(3)
        self.file_tree.setHeaderLabels(["Name", "Size", "Last Modified"])
        self.file_tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.file_tree.itemDoubleClicked.connect(self.open_item)
        self.file_tree.customContextMenuRequested.connect(self.show_context_menu)

        # Make file items larger
        self.file_tree.setIconSize(QSize(32, 32))  # Bigger icons
        self.file_tree.setColumnWidth(0, 300)  # Name column
        self.file_tree.setColumnWidth(1, 120)  # Size column
        self.file_tree.setColumnWidth(2, 180)  # Last Modified column
        self.file_tree.setStyleSheet("""
            QTreeWidget::item { height: 40px; }
        """)

        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.file_tree)
        self.setLayout(main_layout)
        
        # Apply Styles
        self.setStyleSheet("""
            QPushButton { 
                padding: 12px; background-color: #f50000; color: white; border-radius: 5px;
            } 
            QPushButton:hover { 
                background-color: #242424; color: #ffffff;
            }
            QLabel {
                font-size: 14px;
            }
            QTreeWidget {
                border: 1px solid #ccc;
            }
        """)

    def load_directory(self):
        """Loads directory contents into the tree view."""
        self.file_tree.clear()
        self.path_label.setText(self.current_path)
        
        try:
            items = sorted(os.listdir(self.current_path),
                           key=lambda x: (not os.path.isdir(os.path.join(self.current_path, x)), x.lower()))
            
            for item in items:
                item_path = os.path.join(self.current_path, item)
                size = self.get_size(item_path)
                mod_time = self.get_mod_time(item_path)
                tree_item = QTreeWidgetItem([item, size, mod_time])
                tree_item.setIcon(0, self.get_icon(item_path))
                self.file_tree.addTopLevelItem(tree_item)
        except PermissionError:
            QMessageBox.warning(self, "Access Denied", "You don't have permission to access this directory.")

    def get_size(self, path):
        """Returns formatted file/folder size."""
        if os.path.isdir(path):
            return "Folder"
        size = os.path.getsize(path)
        return f"{size / 1024:.2f} KB" if size > 1024 else f"{size} B"

    def get_mod_time(self, path):
        """Returns the last modified time."""
        return datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")

    def get_icon(self, path):
        from PyQt6.QtGui import QIcon
        """Returns an appropriate icon based on file type."""
        if os.path.isdir(path):
            icon_path1 = self.find_icon('ICON/folder.png') 
            return QIcon(icon_path1)
        mime_type, _ = mimetypes.guess_type(path)
        if mime_type and "image" in mime_type:
            icon_path3 = self.find_icon('ICON/image.png')
            return QIcon(icon_path3)
        icon_path2 = self.find_icon('ICON/file.png') 
        return QIcon(icon_path2)
    
    def find_icon(self, icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

    def open_item(self, item):
        from PyQt6.QtGui import QDesktopServices
        """Opens a file or navigates to a folder."""
        new_path = os.path.join(self.current_path, item.text(0))
        if os.path.isdir(new_path):
            self.current_path = new_path
            self.load_directory()
        else:
            QDesktopServices.openUrl(QUrl.fromLocalFile(new_path))

    def go_back(self):
        """Navigates back to the parent directory."""
        if os.path.dirname(self.current_path):
            self.current_path = os.path.dirname(self.current_path)
            self.load_directory()

    def show_context_menu(self, position):
        """Displays a right-click context menu."""
        menu = QMenu()
        actions = {
            "Open": self.open_selected,
            "Delete": self.delete_selected,
            "Rename": self.rename_selected,
            "New Folder": self.create_new_folder
        }
        
        for name, method in actions.items():
            from PyQt6.QtGui import QAction
            action = QAction(name, self)
            action.triggered.connect(method)
            menu.addAction(action)
        
        menu.exec(self.file_tree.viewport().mapToGlobal(position))

    def open_selected(self):
        selected_item = self.file_tree.currentItem()
        if selected_item:
            self.open_item(selected_item)

    def delete_selected(self):
        import shutil
        selected_item = self.file_tree.currentItem()
        if selected_item:
            path = os.path.join(self.current_path, selected_item.text(0))
            reply = QMessageBox.question(self, "Confirm Delete", f"Delete '{selected_item.text(0)}'?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
                    self.load_directory()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Could not delete: {e}")

    def rename_selected(self):
        selected_item = self.file_tree.currentItem()
        if selected_item:
            old_path = os.path.join(self.current_path, selected_item.text(0))
            new_name, ok = QInputDialog.getText(self, "Rename", "Enter new name:")
            if ok and new_name:
                try:
                    os.rename(old_path, os.path.join(self.current_path, new_name))
                    self.load_directory()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Could not rename: {e}")

    def create_new_folder(self):
        folder_name, ok = QInputDialog.getText(self, "New Folder", "Enter folder name:")
        if ok and folder_name:
            try:
                os.makedirs(os.path.join(self.current_path, folder_name), exist_ok=True)
                self.load_directory()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not create folder: {e}")

class GitWorker(QThread):
    """ Background thread for running Git operations """
    finished = pyqtSignal(str, str)  # status message, color

    def __init__(self, operation, repo_path=None, repo_url=None, files=None):
        super().__init__()
        self.operation = operation
        self.repo_path = repo_path
        self.repo_url = repo_url
        self.files = files

    def run(self):
        import git
        try:
            if self.operation == "clone":
                git.Repo.clone_from(self.repo_url, self.repo_path)
                self.finished.emit("Repository cloned successfully", "green")
            elif self.operation == "commit":
                repo = git.Repo(self.repo_path)
                repo.index.add(self.files)
                repo.index.commit("Auto-commit from GitHub Manager")
                self.finished.emit("Changes committed successfully", "green")
            elif self.operation == "push":
                repo = git.Repo(self.repo_path)
                repo.remotes.origin.push()
                self.finished.emit("Changes pushed to GitHub", "green")
            elif self.operation == "pull":
                repo = git.Repo(self.repo_path)
                repo.remotes.origin.pull()
                self.finished.emit("Changes pulled from GitHub", "green")
        except Exception as e:
            self.finished.emit(f"Error: {str(e)}", "red")

class GitHub(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.selected_files = []

    def init_ui(self):
        from PyQt6.QtGui import QFont, QTextCharFormat, QMouseEvent
        """ Setup the modern UI """
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 14px;
            }
            QLineEdit, QPushButton {
                border-radius: 6px;
                padding: 6px;
            }
            QLineEdit {
                border: 1px solid #444;
                background-color: #2a2a2a;
            }
            QPushButton {
                background-color: #0078D7;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
            QLabel {
                font-size: 16px;
            }
        """)

        layout = QVBoxLayout()

        # Input Fields
        self.repo_url_input = self.create_input_field("Enter GitHub Repository URL", qta.icon("mdi.github"))
        self.repo_path_input = self.create_input_field("Enter Local Repository Path", qta.icon("mdi.folder-open"))
        
        layout.addWidget(self.repo_url_input)
        layout.addWidget(self.repo_path_input)

        # Status Label
        self.status_label = QLabel("Status: Ready")
        self.status_label.setFont(QFont("Arial", 12))
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        # Buttons Layout
        button_layout = QHBoxLayout()
        self.clone_button = self.create_button("Clone", qta.icon("mdi.download"), self.clone_repository)
        self.create_repo_button = self.create_button("Init Repo", qta.icon("mdi.database"), self.create_local_repository)
        self.commit_button = self.create_button("Commit", qta.icon("mdi.check"), self.commit_changes)
        self.push_button = self.create_button("Push", qta.icon("mdi.upload"), self.push_changes)
        self.pull_button = self.create_button("Pull", qta.icon("mdi.refresh"), self.pull_changes)

        button_layout.addWidget(self.clone_button)
        button_layout.addWidget(self.create_repo_button)
        button_layout.addWidget(self.commit_button)
        button_layout.addWidget(self.push_button)
        button_layout.addWidget(self.pull_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def create_input_field(self, placeholder, icon):
        """ Helper to create modern input fields with icons """
        layout = QHBoxLayout()
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setMinimumHeight(30)
        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(24, 24))
        layout.addWidget(icon_label)
        layout.addWidget(input_field)
        frame = QFrame()
        frame.setLayout(layout)
        return frame

    def create_button(self, text, icon, callback):
        """ Helper to create styled buttons with icons """
        button = QPushButton(text)
        button.setStyleSheet("QPushButton { padding: 12px; background-color: #f50000; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        button.setIcon(icon)
        button.setMinimumHeight(35)
        button.clicked.connect(callback)
        return button

    def _set_status(self, message, color="green"):
        """ Update status message dynamically """
        self.status_label.setText(f"Status: {message}")
        self.status_label.setStyleSheet(f"color: {color};")

    def start_git_operation(self, operation, repo_path=None, repo_url=None, files=None):
        """ Starts a background Git operation """
        self.progress_bar.setVisible(True)
        self.thread = GitWorker(operation, repo_path, repo_url, files)
        self.thread.finished.connect(self.on_git_operation_done)
        self.thread.start()

    def on_git_operation_done(self, message, color):
        """ Handles Git operation completion """
        self.progress_bar.setVisible(False)
        self._set_status(message, color)

    def clone_repository(self):
        repo_url = self.repo_url_input.layout().itemAt(1).widget().text().strip()
        repo_path = self.repo_path_input.layout().itemAt(1).widget().text().strip()

        if not repo_url or not repo_path or not self.is_valid_url(repo_url):
            self._set_status("Invalid repository URL or path", "red")
            return

        self._set_status("Cloning repository...", "blue")
        self.start_git_operation("clone", repo_path=repo_path, repo_url=repo_url)

    def create_local_repository(self):
        import git
        repo_path = self.repo_path_input.layout().itemAt(1).widget().text().strip()
        if not repo_path:
            self._set_status("Provide a local path", "red")
            return

        os.makedirs(repo_path, exist_ok=True)
        git.Repo.init(repo_path)
        self._set_status("Repository initialized", "green")

    def commit_changes(self):
        repo_path = self.repo_path_input.layout().itemAt(1).widget().text().strip()
        if not repo_path or not self.selected_files:
            self._set_status("No files selected for commit", "red")
            return

        self._set_status("Committing changes...", "blue")
        self.start_git_operation("commit", repo_path=repo_path, files=self.selected_files)

    def push_changes(self):
        repo_path = self.repo_path_input.layout().itemAt(1).widget().text().strip()
        self.start_git_operation("push", repo_path=repo_path)

    def pull_changes(self):
        repo_path = self.repo_path_input.layout().itemAt(1).widget().text().strip()
        self.start_git_operation("pull", repo_path=repo_path)

    def is_valid_url(self, url):
        """ Validate GitHub repository URL """
        return bool(re.match(r"^(https://|git@)github.com[:/][\w-]+/[\w-]+(\.git)?$", url))

    def get_or_init_repo(self, repo_path):
        import git
        """Helper function to get or initialize a Git repository"""
        try:
            if os.path.exists(repo_path) and os.path.isdir(os.path.join(repo_path, ".git")):
                return git.Repo(repo_path)
            else:
                os.makedirs(repo_path, exist_ok=True)
                return git.Repo.init(repo_path)
        except git.exc.InvalidGitRepositoryError:
            self._set_status("Invalid Git repository! Initializing new repository.", "orange")
            return git.Repo.init(repo_path)

class OutputWin(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create a text output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        self.setLayout(layout)

    def update_output(self, message):
        """Update the output window with a new message."""
        self.output_area.append(message)  # Append new messages
        self.output_area.ensureCursorVisible()  # Scroll to the latest message

class Web_Engine(QWidget):
    def __init__(self):
        super().__init__()

        self.search_history = []  # Store search history

        # Main Layout
        main_layout = QVBoxLayout()

        # Create Persistent Profile
        profile_path = os.path.expanduser("~/.web_browser_profile")  # Change to suitable path
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentStoragePath(profile_path)
        profile.setCachePath(profile_path)
        profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies)

        # Use the provided QWebEngineView instance
        self.webview = webview
        self.webview.setUrl(QUrl("https://www.qwant.com/?theme=1"))

        # Enable downloads
        profile = self.webview.page().profile()
        profile.downloadRequested.connect(self.handle_download)

        # Floating Search Bar (inside WebView)
        self.search_bar = QWidget(self.webview)
        self.search_bar.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 150);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.search_bar.setFixedSize(400, 40)

        search_layout = QHBoxLayout(self.search_bar)
        search_layout.setContentsMargins(5, 5, 5, 5)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search or enter URL...")
        self.search_input.setStyleSheet("color: white; background-color: rgba(50, 50, 50, 200); border: none;")
        self.search_input.returnPressed.connect(self.load_url)

        self.search_button = QPushButton("Go")
        self.search_button.clicked.connect(self.load_url)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # Auto-completion for search history
        self.completer = QCompleter(self.search_history)
        self.search_input.setCompleter(self.completer)

        # Add WebView to main layout
        main_layout.addWidget(self.webview)
        self.setLayout(main_layout)

        # Position search bar (Overlay)
        self.search_bar.move(50, 20)
        self.search_bar.hide()

        # Show search bar on hover
        self.webview.installEventFilter(self)

    def eventFilter(self, obj, event):
        """Show search bar when mouse hovers over WebView."""
        if obj == self.webview and event.type() == event.Type.HoverEnter:
            self.search_bar.show()
        elif obj == self.webview and event.type() == event.Type.HoverLeave:
            self.search_bar.hide()
        return super().eventFilter(obj, event)

    def check_internet_connection(self):
        import requests
        """Check if the internet is available."""
        try:
            requests.get("https://www.google.com", timeout=3)  # Ping Google
            return True
        except requests.ConnectionError:
            return False

    def wait_for_internet(self):
        """Continuously check for internet connection until restored."""
        webview.hide()
        QMessageBox.information(self, "No Internet", "No internet connection. Waiting for connection...")
        timer = QTimer(self)
        timer.setInterval(5000)  # Check every 5 seconds
        timer.timeout.connect(lambda: self.retry_loading(timer))
        timer.start()

    def retry_loading(self, timer):
        """Retry loading the page when the internet comes back."""
        if self.check_internet_connection():
            QMessageBox.information(self, "Internet Restored", "Internet connection has been restored!")
            webview.show()
            timer.stop()
            self.load_url()

    def load_url(self):
        """Load URL from the search bar, checking internet connection first."""
        text = self.search_input.text().strip()

        if not self.check_internet_connection():
            QMessageBox.warning(self, "No Internet", "No internet connection. Waiting to reconnect...")
            self.wait_for_internet()
            return

        if text:
            if " " in text:
                url = f"https://www.qwant.com/?q={text.replace(' ', '+')}&theme=1"
            elif not text.startswith("http"):
                url = f"https://{text}"
            else:
                url = text

            self.webview.setUrl(QUrl(url))

            if text not in self.search_history:
                self.search_history.append(text)
                self.completer.setModel(QStringListModel(self.search_history))

    def handle_download(self, download: QWebEngineDownloadRequest):
        """Handle file downloads with an internet check."""
        if not self.check_internet_connection():
            QMessageBox.warning(self, "No Internet", "Download failed due to no internet. Waiting to retry...")
            self.wait_for_internet()
            return

        suggested_filename = download.suggestedFileName()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", suggested_filename)

        if file_path:
            directory = "/".join(file_path.split("/")[:-1])
            filename = file_path.split("/")[-1]

            download.setDownloadDirectory(directory)
            download.setDownloadFileName(filename)
            download.accept()

            progress_dialog = QProgressDialog("Downloading...", "Cancel", 0, 100, self)
            progress_dialog.setWindowTitle("Download Progress")
            progress_dialog.setMinimumWidth(300)
            progress_dialog.setAutoClose(False)
            progress_dialog.setAutoReset(False)

            timer = QTimer(self)
            timer.setInterval(500)
            timer.timeout.connect(lambda: self.check_download_progress(download, progress_dialog, timer, filename))
            timer.start()

            QMessageBox.information(self, "Download Started", f"Downloading {filename} to {directory}...")
        else:
            QMessageBox.warning(self, "Download Canceled", "The download was canceled.")

    def check_download_progress(self, download, progress_dialog, timer, filename):
        """Manually check and update download progress."""
        received_bytes = download.receivedBytes()
        total_bytes = download.totalBytes()

        if total_bytes > 0:
            percent = int((received_bytes / total_bytes) * 100)
            progress_dialog.setValue(percent)
            progress_dialog.setLabelText(f"Downloading {filename}... {percent}%")

        # Stop the timer and close progress dialog when download completes
        if download.isFinished():
            timer.stop()
            progress_dialog.setValue(100)
            progress_dialog.close()
            QMessageBox.information(self, "Download Complete", f"{filename} has been downloaded successfully!")

class Chat(QWidget):
    def __init__(self):
        super().__init__()

        self.config_file = "config.json"
        self.sessions_file = "chat_sessions.json"
        self.API_KEY = None
        self.API_URL = "https://openrouter.ai/api/v1/chat/completions"
        self.MODEL = "meta-llama/llama-3-8b-instruct:free"
        self.chat_sessions = {}
        self.current_session = None
        self.checking_api_key = True

        # Start API key check in a separate thread
        self.api_check_thread = threading.Thread(target=self.check_api_key, daemon=True)
        self.api_check_thread.start()

        self.load_api_key()
        self.load_sessions()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget { background-color: #1c1c28; color: white; font-size: 14px; border-radius: 8px; padding: 10px;}
            QLineEdit { background-color: #2a2a3a; color: #ffffff; border-radius: 6px; padding: 10px; border: 1px solid #444; }
            QPushButton { background-color: #3d3d4d; color: white; border-radius: 6px; padding: 8px; border: none; }
            QPushButton:hover { background-color: #525268; }
            QLabel { color: #e0e0e0; }
            QFrame { background-color: #282838; border-radius: 8px; padding: 10px; }
        """)

        main_layout = QHBoxLayout()
        chat_layout = QVBoxLayout()

        # Scrollable chat area
        from PyQt6.QtWidgets import QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;")

        self.chat_display = QVBoxLayout()
        self.chat_container = QWidget()
        self.chat_container.setLayout(self.chat_display)
        self.scroll_area.setWidget(self.chat_container)

        # Watermark (brand name)
        self.watermark = QLabel("Alpha-X", self)
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watermark.setStyleSheet("color: rgba(255, 255, 255, 0.07); font-size: 50px; font-weight: bold;")
        self.chat_display.addWidget(self.watermark)

        # Chat input area
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message...")
        self.input_field.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("Send")
        from PyQt6.QtWidgets import QSizePolicy
        self.send_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.send_button.clicked.connect(self.send_message)

        self.clear_button = QPushButton("Clear Chat")
        self.clear_button.clicked.connect(self.clear_screen)

        # Loader and progress indicator
        self.loader_label = QLabel("Processing...")
        self.loader_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loader_label.hide()

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)
        input_layout.addWidget(self.clear_button)

        chat_layout.addWidget(self.scroll_area)
        chat_layout.addWidget(self.loader_label)
        chat_layout.addWidget(self.progress_bar)
        chat_layout.addLayout(input_layout)

        # Sidebar (Chat History)
        self.history_panel_widget = QWidget()
        self.history_panel_widget.setFixedWidth(220)  # Keeps sidebar fixed
        self.history_panel_widget.setStyleSheet("border-radius: 8px; padding: 5px;")
        self.history_panel = QVBoxLayout(self.history_panel_widget)

        self.history_title = QLabel("Chat History")
        self.history_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.history_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #dddddd; padding: 5px;")

        from PyQt6.QtWidgets import QListWidget
        self.history_list = QListWidget()
        self.history_list.setStyleSheet("""
            QListWidget { background-color: #23232e; border-radius: 6px; padding: 5px; }
            QListWidget::item { padding: 8px; color: white; }
            QListWidget::item:selected { background-color: #3b3b5c; }
        """)
        self.history_list.itemClicked.connect(self.load_session)

        self.history_panel.addWidget(self.history_title)
        self.history_panel.addWidget(self.history_list)

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(self.history_panel)

        main_layout.addWidget(sidebar_widget)
        main_layout.addLayout(chat_layout)

        self.setLayout(main_layout)
        self.update_history()

    def check_api_key(self):
        import time
        while self.checking_api_key:
            self.load_api_key()
            time.sleep(5)

    def load_api_key(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    data = json.load(file)
                    self.API_KEY = data.get("API_KEY", None)

                    if self.API_KEY:
                        logging.info("API Key loaded successfully.")
                        self.checking_api_key = False
                    else:
                        logging.info("API Key missing. Retrying...")
                        QMessageBox.information(self, "API Key", "API Key not found. Retrying...")
            except Exception as e:
                logging.error(f"Error loading API Key: {e}")

    def load_sessions(self):
        if os.path.exists(self.sessions_file):
            try:
                with open(self.sessions_file, "r") as file:
                    self.chat_sessions = json.load(file)
            except Exception as e:
                logging.error(f"Error loading chat sessions: {e}")

    def save_sessions(self):
        try:
            with open(self.sessions_file, "w") as file:
                json.dump(self.chat_sessions, file, indent=4)
        except Exception as e:
            logging.error(f"Error saving chat sessions: {e}")

    def send_message(self):
        user_text = self.input_field.text().strip()
        if not user_text:
            return

        if self.current_session is None:
            self.current_session = user_text[:20]
            self.chat_sessions[self.current_session] = []

        self.chat_sessions[self.current_session].append(f"You: {user_text}")
        self.display_message(user_text, "user")
        self.input_field.clear()

        self.loader_label.show()
        self.progress_bar.show()

        # Create ChatWorker and connect signals
        self.worker = ChatWorker(user_text, self.API_KEY, self.API_URL, self.MODEL)
        self.worker.finished.connect(self.handle_ai_response)
        self.worker.start()

        self.update_history()
        self.save_sessions()

    def display_message(self, text, sender):
        bubble = QFrame()
        bubble_layout = QVBoxLayout()
        message_label = QLabel(text)
        message_label.setWordWrap(True)

        if sender == "user":
            bubble.setStyleSheet("background-color: #444; color: white; padding: 10px; border-radius: 6px;")
            message_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        elif sender == "ai":
            bubble.setStyleSheet("background-color: #333; color: white; padding: 10px; border-radius: 6px;")
            message_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        elif sender == "error":
            bubble.setStyleSheet("background-color: #ff5555; color: white; padding: 10px; border-radius: 6px;")
            message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bubble_layout.addWidget(message_label)
        bubble.setLayout(bubble_layout)
        self.chat_display.addWidget(bubble)

        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def handle_ai_response(self, response_text):
        self.chat_sessions[self.current_session].append(f"AI: {response_text}")
        self.display_message(response_text, "ai")
        
        self.loader_label.hide()
        self.progress_bar.hide()

        self.save_sessions()

    def update_history(self):
        self.history_list.clear()
        for session in self.chat_sessions:
            self.history_list.addItem(session)

    def load_session(self, session_item):
        session_name = session_item.text()
        self.current_session = session_name
        self.clear_screen()
        for message in self.chat_sessions.get(session_name, []):
            sender, text = message.split(": ", 1) if ": " in message else ("error", message)
            self.display_message(text, sender)

    def clear_screen(self):
        for i in reversed(range(self.chat_display.count())):
            self.chat_display.itemAt(i).widget().deleteLater()

class ChatWorker(QThread):
    finished = pyqtSignal(str)
    
    def __init__(self, user_command, api_key, api_url, model):
        super().__init__()
        self.user_command = user_command
        self.api_key = api_key
        self.api_url = api_url
        self.model = model
    
    def run(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": self.user_command}]
        }
        
        try:
            import requests
            response = requests.post(self.api_url, headers=headers, json=payload)
            response_json = response.json()
            if "choices" in response_json and response_json["choices"]:
                result = response_json["choices"][0]["message"]["content"].strip()
            else:
                result = "Failed to generate a response."
        except Exception as e:
            logging.error(f"Error parsing API response: {e}")
            result = "Error processing request."
        
        self.finished.emit(result)

def find_icon(icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path

        return None

class AppScanner(QThread):
    apps_found = pyqtSignal(list)

    def run(self):
        import winreg
        apps = []
        uninstall_keys = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]

        exclude_keywords = ["uninstaller", "runtime", "driver", "openssl"]

        for key_path in uninstall_keys:
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            with winreg.OpenKey(key, subkey_name) as subkey:
                                name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                                exe_path = self.find_executable(subkey)
                                if exe_path and not any(keyword.lower() in name.lower() for keyword in exclude_keywords):
                                    apps.append((name, exe_path))
                        except Exception:
                            pass
            except Exception:
                pass

        self.apps_found.emit(sorted(apps, key=lambda x: x[0].lower()))

    def find_executable(self, subkey):
        import winreg
        from pathlib import Path
        try:
            install_path, _ = winreg.QueryValueEx(subkey, "InstallLocation")
            if install_path and os.path.exists(install_path):
                exe_files = list(Path(install_path).rglob("*.exe"))
                return str(exe_files[0]) if exe_files else None
        except FileNotFoundError:
            pass
        return None

class AppLauncher(QRunnable):
    """Runs application launching in a separate thread to prevent UI freezing."""

    def __init__(self, app_path):
        super().__init__()
        self.app_path = app_path

    def run(self):
        try:
            print(f"Launching application: {self.app_path}")  # Debugging output
            subprocess.Popen([self.app_path], shell=True)  # Launch app in new thread
        except Exception as e:
            print(f"Failed to launch {self.app_path}: {e}")

class AppMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1E1E1E; color: white;")

        self.default_icon_path = "ICON/hub-64.png"
        self.threadpool = QThreadPool.globalInstance()  # Thread pool for launching apps

        main_layout = QVBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search applications...")
        self.search_bar.setStyleSheet(
            "padding: 12px; font-size: 16px; border-radius: 10px; background-color: #2C2C2C; color: white;")
        self.search_bar.textChanged.connect(self.filter_apps)

        from PyQt6.QtWidgets import QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;")

        self.container_widget = QWidget()
        self.grid_layout = QGridLayout(self.container_widget)
        self.scroll_area.setWidget(self.container_widget)

        main_layout.addWidget(self.search_bar)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        self.apps = []
        self.filtered_apps = []
        self.scanner = AppScanner()
        self.scanner.apps_found.connect(self.populate_apps)
        self.scanner.start()

    def populate_apps(self, apps):
        self.apps = apps
        self.filtered_apps = apps
        self.update_grid()

    def update_grid(self):
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        row, col = 0, 0
        for app_name, app_path in self.filtered_apps:
            if not app_path:
                continue

            button = QPushButton()
            from PyQt6.QtGui import QIcon
            button.setIcon(QIcon(self.default_icon_path))
            button.setIconSize(QSize(72, 72))
            button.setToolTip(app_name)
            button.setStyleSheet(
                "QPushButton { border: none; background-color: #292929; border-radius: 10px; padding: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
            button.clicked.connect(lambda checked, path=app_path: self.launch_app(path))

            label = QLabel(app_name)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("font-size: 14px; padding: 5px;")

            self.grid_layout.addWidget(button, row, col)
            self.grid_layout.addWidget(label, row + 1, col)

            col += 1
            if col >= 3:
                col = 0
                row += 2

    def filter_apps(self):
        query = self.search_bar.text().strip().lower()
        self.filtered_apps = [app for app in self.apps if query in app[0].lower()]
        self.update_grid()

    def launch_app(self, path):
        """Launch app in a separate thread to keep UI responsive."""
        self.threadpool.start(AppLauncher(path))

class SecurityVault(QWidget):
    buffer_size = 64 * 1024
    
    def __init__(self):
        from PyQt6.QtGui import QIcon
        from PyQt6.QtGui import QColor, QFont
        super().__init__()
        #self.setWindowTitle("Secret Vault")
        #self.setGeometry(400, 200, 500, 350)
        self.setStyleSheet("""
            background-color: #2b2b2b;
            color: #f1f1f1;
            font-family: 'Segoe UI', sans-serif;
        """)
        icon_path = self.find_icon('background/icon.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))
        
        self.vault_dir = os.path.expanduser("~/.vault")
        self.config_path = os.path.expanduser("~/.vaultcfg")

        # Main Layout
        main_layout = QVBoxLayout()

        # File List
        from PyQt6.QtWidgets import QListWidget
        self.file_list = QListWidget()
        self.file_list.setStyleSheet("background-color: #3a3a3a; color: #ffffff; border-radius: 5px;")
        self.load_files()

        # Buttons with modern style
        btn_add = QPushButton("Add File")
        btn_add.setStyleSheet("QPushButton { padding: 12px; background-color: #484848; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        btn_add.clicked.connect(self.add_file)

        btn_unhide = QPushButton("Unhide File")
        btn_unhide.setStyleSheet("QPushButton { padding: 12px; background-color: #484848; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        btn_unhide.clicked.connect(self.unhide_file)

        btn_reset = QPushButton("Reset Vault")
        btn_reset.setStyleSheet("QPushButton { padding: 12px; background-color: #484848; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}")
        btn_reset.clicked.connect(self.reset_vault)

        # Add widgets to layout
        main_layout.addWidget(self.file_list)
        main_layout.addWidget(btn_add)
        main_layout.addWidget(btn_unhide)
        main_layout.addWidget(btn_reset)

        # Set the main layout
        self.setLayout(main_layout)
        self.authenticate()

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def authenticate(self):
        if os.path.exists(self.config_path):
            password, ok = QInputDialog.getText(self, "Vault Password", "Enter your Vault Password:")
            if not ok or not password:
                exit()
            self.master_password = password
            self.generate_key()
            with open(self.config_path, 'rb') as f:
                encrypted_pwd = f.read()
                try:
                    fernet = Fernet(self.key)
                    fernet.decrypt(encrypted_pwd)
                except:
                    QMessageBox.warning(self, "Error", "Wrong Vault Password!")
                    exit()
        else:
            password, ok = QInputDialog.getText(self, "Create Password", "Create a Vault Password:")
            if not ok or not password:
                exit()
            self.master_password = password
            self.generate_key()
            fernet = Fernet(self.key)
            enc_pwd = fernet.encrypt(password.encode())
            with open(self.config_path, 'wb') as f:
                f.write(enc_pwd)
            os.makedirs(self.vault_dir, exist_ok=True)

    def generate_key(self):
        salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"
        password = self.master_password.encode()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        self.key = base64.urlsafe_b64encode(kdf.derive(password))

    def load_files(self):
        self.file_list.clear()
        
        if os.path.exists(self.vault_dir):
            files = os.listdir(self.vault_dir)
            
            for file_name in files:
                file_path = os.path.join(self.vault_dir, file_name)
                
                # Determine icon based on file type (customize with actual icons)
                if file_name.endswith(('.txt', '.log', '.md', '.aes')):
                    icon_path = r"ICON\menu\file.png"
                elif file_name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    icon_path = "ICON\menu\image-file.png"
                elif file_name.endswith(('.mp4', '.avi', '.mkv')):
                    icon_path = r"ICON\menu\video-file.png"
                elif file_name.endswith(('.exe', '.bat')):
                    icon_path = "ICON\menu\exe-file.png"
                else:
                    icon_path = "ICON/hub-64.png"  # Default icon for unknown files

                # Create an item with the icon
                from PyQt6.QtWidgets import QListWidgetItem
                from PyQt6.QtGui import QIcon
                item = QListWidgetItem(QIcon(icon_path), file_name)
                self.file_list.addItem(item)

    def add_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if not file_path:
            return
        
        # Ask user if they want to encrypt the file before storing
        enc_choice = QMessageBox.question(self, "Encryption", "Encrypt the file before storing?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        # Get the filename to use it in the vault
        filename = os.path.basename(file_path)
        dest_path = os.path.join(self.vault_dir, filename + ".aes" if enc_choice == QMessageBox.StandardButton.Yes else filename)
        
        try:
            # If user chooses encryption
            if enc_choice == QMessageBox.StandardButton.Yes:
                pyAesCrypt.encryptFile(file_path, dest_path, self.key.decode(), self.buffer_size)
            else:
                # If no encryption, just copy the file
                import shutil
                shutil.copy(file_path, dest_path)
            
            # Delete the original file after adding it to the vault
            os.remove(file_path)
            
            # Reload the file list to reflect the new contents of the vault
            self.load_files()
            QMessageBox.information(self, "Success", "File successfully added to the vault and original file deleted.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred while processing the file: {e}")

    def unhide_file(self):
        selected_item = self.file_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Error", "No file selected!")
            return
        file_name = selected_item.text()
        vault_path = os.path.join(self.vault_dir, file_name)
        dest_path = os.path.join(os.getcwd(), file_name[:-4] if file_name.endswith('.aes') else file_name)
        if file_name.endswith('.aes'):
            pyAesCrypt.decryptFile(vault_path, dest_path, self.key.decode(), self.buffer_size)
        else:
            import shutil
            shutil.copy(vault_path, dest_path)
        os.remove(vault_path)
        self.load_files()
        QMessageBox.information(self, "Success", f"File restored to {dest_path}")

    def reset_vault(self):
        confirm = QMessageBox.question(self, "Reset Vault", "Are you sure you want to delete all Vault Data?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            import shutil
            shutil.rmtree(self.vault_dir, ignore_errors=True)
            os.remove(self.config_path)
            QMessageBox.information(self, "Success", "Vault reset successfully!")
            exit()

class MainMenu(QMainWindow):
    def __init__(self):
        from PyQt6.QtGui import QIcon
        super().__init__()
        self.setWindowTitle("Menu-X")
        self.setGeometry(100, 100, 900, 500)
        self.setStyleSheet(self.get_styles())

        icon_path = self.find_icon('background/icon.png')
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QHBoxLayout()
        self.central_widget.setLayout(main_layout)

        # Sidebar and its layout
        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(0)
        self.sidebar.setStyleSheet("background-color: #1E1E1E; border-right: 2px solid #333;")
        sidebar_layout = QVBoxLayout()

        # Menu buttons
        self.buttons = {
            "Home": QPushButton("\uf015 Home"),
            "Chat": QPushButton("\uf086 Chat"),
            "Web-Engine": QPushButton("\uf0ac  Web-Engine"),
            "Code-Run": QPushButton("\uf303  Code-Run"),
            "System Monitor": QPushButton("\uf2db  System Monitor"),
            "Network Analyzer": QPushButton("\uf1eb  Network Analyzer"),
            "Terminal": QPushButton("\uf120  Terminal"),
            "File Manager": QPushButton("\uf07b  File Manager"),
            "GitHub": QPushButton("\uf09b GitHub"),
            "Apps": QPushButton("\uf1b2 Apps"),
            "Vault": QPushButton("\uf023 Vault")
        }

        for btn in self.buttons.values():
            btn.setFixedHeight(50)
            btn.setStyleSheet("QPushButton { padding: 12px; background-color: #1b1b1b; color: white; border-radius: 5px;} QPushButton:hover { background-color: #242424; color: #ffffff;}") #898181
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()
        self.sidebar.setLayout(sidebar_layout)

        # Sidebar Toggle Button
        self.toggle_button = QPushButton("\uf0c9")  # Hamburger icon
        self.toggle_button.setFixedSize(50, 50)
        self.toggle_button.setStyleSheet("background-color: #1E1E1E; color: white; border: none; font-size: 24px;")
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Content Area
        self.content_area = QStackedWidget()
        self.content_area.setStyleSheet("background-color: #2D2D30;")
        self.pages = {
            "": DisplayImage(),  # Default page when inactive
            "Home": Home(),
            "Chat": Chat(),
            "Web-Engine": Web_Engine(),
            "Code-Run": CodeEditor(),
            "System Monitor": SystemMonitor(),
            "Network Analyzer": NetworkAnalyzer(),
            "Terminal": Terminal(),
            "File Manager": FileManager(),
            "GitHub": GitHub(),
            "Apps": AppMenu(),
            "Vault": SecurityVault()
        }

        for name, widget in self.pages.items():
            self.content_area.addWidget(widget)

        # Handle button clicks to load respective pages
        for name, btn in self.buttons.items():
            btn.clicked.connect(lambda _, n=name: self.load_tool(n))

        # Main layout for the window
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content_area)

        # Position the toggle button outside of sidebar area
        main_layout.addWidget(self.toggle_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Set up inactivity time
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.timeout.connect(self.show_inactivity_screen)
        self.inactivity_timer.start(3600000)  # 1 hour (3,600,000 ms)

        # Reset inactivity timer on user interaction
        self.setMouseTracking(True)
        self.installEventFilter(self)

    def find_icon(self, icon_name):
        script_dir = os.path.dirname(os.path.realpath(__file__))

        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'ICON', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]

        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def load_tool(self, tool_name):
        self.content_area.setCurrentWidget(self.pages[tool_name])

    def show_inactivity_screen(self):
        # Switch to the DisplayImage() page after 1 hour of inactivity
        self.content_area.setCurrentWidget(self.pages[""])

    def get_styles(self):
        return """
        QPushButton:hover {
            background-color: #007ACC;
        }
        QPushButton:pressed {
            background-color: #005F9E;
        }
        """

    def eventFilter(self, source, event):
        from PyQt6.QtCore import QEvent
        if event.type() in [QEvent.Type.KeyPress, QEvent.Type.MouseMove]:
            # Reset inactivity timer if user interaction occurs
            self.inactivity_timer.start(3600000)  # Restart timer (1 hour)
        return super().eventFilter(source, event)

    def toggle_sidebar(self):
        # Toggle the sidebar width between 0 and 180
        current_width = self.sidebar.width()
        new_width = 180 if current_width == 0 else 0
        self.sidebar.setFixedWidth(new_width)

# Define global variables
cli_window = None
window = None

def show_main_window():
    global cli_window, window  # Ensure these are global variables
    
    # Create CLI window and main window
    cli_window = CLIWindow()
    window = Window(cli_window)
    #com_window = CommandListWindow()
    
    if window is None:
        logging.error("Error: window is None before accessing loader!")
    elif not hasattr(window, "loader"):
        logging.error("Error: window has no attribute 'loader'!")
    else:
        window.loader.setVisible(True)

    # Show the main window and hide the CLI window
    window.show()
    #com_window.show()
    cli_window.hide()

if __name__ == '__main__':
    is_admin()

    import base64
    import json
    import xml.etree.ElementTree as ET

    def decode_license(encoded_license):
        """
        Decodes the license details from the encoded string.
        """
        decoded_json = base64.urlsafe_b64decode(encoded_license.encode()).decode()
        return json.loads(decoded_json)

    def save_license_to_xml(encoded_license, filename="license.xml"):
        """
        Decodes the license details and saves them into an XML file.
        """
        license_data = decode_license(encoded_license)
        
        root = ET.Element("License")
        for key, value in license_data.items():
            child = ET.SubElement(root, key)
            child.text = value
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print(f"License details saved to {filename}")

    # Example usage
    encoded_details = Encoded_License_Details
    save_license_to_xml(encoded_details)

    import sys
    def load_license_from_xml(file_path="license.xml"):
        import sys 
        import xml.etree.ElementTree as ET
        """Loads license details from an XML file."""
        if not os.path.exists(file_path):
            show_message("License Error", "License file not found!", QMessageBox.Icon.Critical)
            sys.exit(1)
        
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            return {
                "Licensor": root.find("licensor").text,
                "License Key": root.find("license_key").text,
                "Expiration Date": root.find("expiration_date").text,
            }
        except Exception as e:
            show_message("License Error", f"Failed to read license file: {e}", QMessageBox.Icon.Critical)
            sys.exit(1)

    def show_message(title, message, icon):
        import sys
        from PyQt6.QtGui import QIcon
        """Displays a message box with the given title, message, and icon."""
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        icon_path = find_icon('background/icon.png')
        app.setWindowIcon(QIcon(icon_path))

        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.setWindowIcon(QIcon(icon_path))
        msg_box.exec()

    def find_icon(icon_name):
        """Attempts to find the icon in and out of the script's directory."""
        script_dir = os.path.dirname(os.path.realpath(__file__))
        possible_paths = [
            os.path.join(script_dir, icon_name),
            os.path.join(script_dir, 'background', icon_name),
            os.path.abspath(os.path.join(script_dir, os.pardir, icon_name)),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def is_license_valid(license_info):
        import datetime
        """Checks if the license is still valid."""
        try:
            expiration_date = datetime.datetime.strptime(license_info["Expiration Date"], "%Y-%m-%d")
            if datetime.datetime.now() > expiration_date:
                show_message("License Expired", "Your license has expired!\nUpdate to a newer version.", QMessageBox.Icon.Critical)
                return False
            return True
        except Exception as e:
            show_message("License Error", f"Invalid license date format: {e}", QMessageBox.Icon.Critical)
            return False

    # Load license and validate
    LICENSE = load_license_from_xml()
    if is_license_valid(LICENSE):
        show_message("License Valid", f"Software is licensed by licensor {LICENSE['Licensor']}.\nLicense key: {LICENSE['License Key']}\nYour access code is 00000", QMessageBox.Icon.Information)
        import sys
        app = QApplication(sys.argv)

        webview = QWebEngineView()

        UpdatePrompt.check_for_update()

        # Create splash screen object
        splash = SplashScreen()

        # Show splash screen initially
        splash.show_splash()

        Logining = LoginPage()
        QTimer.singleShot(10000, Logining.show)

        quest = QuestionnaireApp()
        
        sett = SettingsWindow()

        dash = DashboardWindow()

        menu = MainMenu()
        # Main program logic here
    else:
        sys.exit(1)

    # Start the application event loop
    sys.exit(app.exec())