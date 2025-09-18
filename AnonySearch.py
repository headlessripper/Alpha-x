from PyQt6.QtCore import QUrl, Qt, pyqtSignal, QSize
from PyQt6.QtGui import QIcon, QPainter, QRegion
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QInputDialog, QHBoxLayout, QSpacerItem, QSizePolicy, QTabBar, QComboBox, QLabel, QFileDialog
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineDownloadRequest  # Import QWebEngineDownloadRequest instead of QWebEngineDownloadItem
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtNetwork import QNetworkProxy
import sys
import os

def set_dark_theme(self):
    """Set dark theme for the application."""
    dark_stylesheet = """
    QWidget {
        background-color: #ff0000;
        color: #ffffff;
    }
    QPushButton {
        background-color: #000000;
        color: #d3d3d3;
        border: none;
        padding: 15px;
        border-radius: 10px;
    }
    """
    self.setStyleSheet(dark_stylesheet)

class WebViewerTab(QWidget):
    def __init__(self, tab_widget):
        super().__init__()
        self.tab_widget = tab_widget  # Store the reference to the QTabWidget
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        
        # Create browser instance
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
        
        # Connect the download requested signal to handle downloads
        self.browser.page().profile().downloadRequested.connect(self.handle_download)

        # Set the browser to handle its own back, forward, and reload actions
        self.setup_browser_navigation()

        # Create a custom profile for the tab
        self.profile = QWebEngineProfile()
        self.browser.setPage(QWebEnginePage(self.profile, self.browser))

        # Create button panel for loading URL
        self.button_panel = QHBoxLayout()
        self.layout.addLayout(self.button_panel)
        
        # Load URL button
        self.load_button = QPushButton("Load URL")
        self.load_button.clicked.connect(self.load_url)
        self.button_panel.addWidget(self.load_button)
        
        # Add proxy selection dropdown
        self.proxy_combo = QComboBox()
        self.proxy_combo.addItem("Select Proxy")
        self.proxy_combo.addItem("Proxy 1: IND")
        self.proxy_combo.addItem("Proxy 2: USA")
        self.proxy_combo.addItem("Proxy 3: CAN")
        self.proxy_combo.addItem("Proxy 3: TOR")
        self.proxy_combo.currentIndexChanged.connect(self.on_proxy_change)  # Connect signal to update proxy
        self.button_panel.addWidget(self.proxy_combo)

        # Create close button for the tab
        self.close_button = QPushButton("Close Tab")
        self.close_button.clicked.connect(self.close_tab)
        self.button_panel.addWidget(self.close_button)

    def setup_browser_navigation(self):
        """This function enables browser navigation without the explicit buttons."""
        self.browser.setUrl(QUrl("https://www.qwant.com/?theme=1"))  # Set default URL

    def load_url(self):
        url, ok = QInputDialog.getText(self, 'Load URL', 'Enter URL:')
        if ok and url:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
            self.browser.setUrl(QUrl(url))

            # Extract domain from URL and set it as the tab name
            self.update_tab_name(url)

    def update_tab_name(self, url):
        """Extract domain name from the URL and set it as the tab name."""
        parsed_url = QUrl(url)
        host = parsed_url.host()  # Get the host part of the URL (e.g., "www.youtube.com")
        
        # Strip "www." if present
        if host.startswith('www.'):
            host = host[4:]

        # Set the tab name to the domain (e.g., "YouTube" for youtube.com)
        tab_name = host.split('.')[0].capitalize()  # Get the first part of the domain name and capitalize it
        current_index = self.tab_widget.indexOf(self)
        if current_index != -1:
            self.tab_widget.setTabText(current_index, tab_name)

    def set_proxy(self, proxy_name=None):
        """Set proxy to change IP address based on selection."""
        proxies = {
            "Proxy 1 INDIA": {"host": "165.165.111.205", "port": 8080},
            "Proxy 2 USA": {"host": "165.165.111.205", "port": 8888},
            "Proxy 3 CANADA": {"host": "165.165.111.205", "port": 8844},
            "TOR": {"host": "127.0.0.1", "port": 9050},  # Tor SOCKS5 proxy
        }

        if proxy_name is None or proxy_name == "Select Proxy":
            return

        proxy = proxies.get(proxy_name)
        if proxy:
            # Use the correct constant for SOCKS5Proxy in PyQt6
            network_proxy = QNetworkProxy(QNetworkProxy.ProxyType.Socks5Proxy, proxy["host"], proxy["port"])
            QNetworkProxy.setApplicationProxy(network_proxy)  # Apply proxy globally for the application
            print(f"Proxy set to {proxy_name} ({proxy['host']}:{proxy['port']})")

    def on_proxy_change(self):
        """Handle proxy selection change."""
        selected_proxy = self.proxy_combo.currentText()
        if selected_proxy != "Select Proxy":
            self.set_proxy(selected_proxy)

    def close_tab(self):
        """Close the current tab."""
        current_index = self.tab_widget.indexOf(self)
        if current_index != -1:
            self.tab_widget.removeTab(current_index)  # Remove the tab at the current index

    def handle_download(self, download_request):
        """Handles the download and prompts the user to select a location."""
        print("Download requested...")

        # Ask the user where to save the file
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        
        # Get the default suggested file name
        suggested_filename = download_request.url().fileName()
        print(f"Suggested filename: {suggested_filename}")
        file_dialog.selectFile(suggested_filename)

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # Get the user-selected file path
            selected_file_path = file_dialog.selectedFiles()[0]
            print(f"Selected file path: {selected_file_path}")

            # Set the download path
            download_request.setPath(selected_file_path)
            download_request.accept()  # Start the download

            # Optionally, connect to download finished signal to do further actions
            download_request.finished.connect(self.download_finished)

    def download_finished(self):
        """Notify the user that the download has finished."""
        print("Download finished!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AnonySearch')
        set_dark_theme(self)
        self.setGeometry(100, 100, 800, 600)

        icon_path = self.find_icon('ICON/icons8-anonymous-50.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('ICON/icons8-anonymous-50.png'))

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        
        self.tab_widget = QTabWidget()
        central_layout.addWidget(self.tab_widget)
        
        self.add_tab_button = QPushButton("New Tab")
        self.add_tab_button.setStyleSheet("background-color: #000000; color: #d3d3d3; border: none; padding: 15px;")
        self.add_tab_button.clicked.connect(self.add_new_tab)
        central_layout.addWidget(self.add_tab_button)

        self.setCentralWidget(central_widget)
        self.add_new_tab()

    def add_new_tab(self):
        new_tab = WebViewerTab(self.tab_widget)  # Pass the tab_widget reference
        self.tab_widget.addTab(new_tab, f"Tab {self.tab_widget.count() + 1}")
        new_tab.browser.setUrl(QUrl("https://www.qwant.com/?theme=1"))
        self.tab_widget.setCurrentWidget(new_tab)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
