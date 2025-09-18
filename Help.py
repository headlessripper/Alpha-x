import sys
import json
import os
import requests
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QScrollArea, QLineEdit, QFrame, QPushButton, QDialog
)

COMMANDS_JSON_URL = "https://github.com/headlessripper/AlphaX1/releases/download/V0.0.1.0/commands.json"

def load_commands():
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

class CommandListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle('Alpha Commands')

        icon_path = self.find_icon('ICON/help.png')  # Try to find the icon

        # Set the icon if it's found, otherwise use a fallback
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.setWindowIcon(QIcon('background/icon.png'))

        self.commands = load_commands()
        self.setStyleSheet(self.get_qss_style())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search commands...")
        self.search_bar.textChanged.connect(self.update_display)
        layout.addWidget(self.search_bar)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.command_container = QWidget()
        self.command_layout = QVBoxLayout(self.command_container)
        self.scroll_area.setWidget(self.command_container)
        layout.addWidget(self.scroll_area)

        # GitHub Link
        self.github_label = QLabel("For More Information Visit: "'<a href="https://github.com/headlessripper/Alpha-x" style="color:#ff0000;">Alpha-X</a>', self)
        self.github_label.setStyleSheet("font-size: 14px; padding: 5px;")
        self.github_label.setOpenExternalLinks(True)  # Allows opening links in a browser
        layout.addWidget(self.github_label)

        self.populate_commands()
        central_widget.setLayout(layout)
    
    def get_qss_style(self):
        return """
        QWidget {
            background-color: #222831;
            color: #eeeeee;
            font-family: Arial, sans-serif;
        }
        QLabel {
            font-size: 14px;
            padding: 5px;
        }
        QPushButton {
            background-color: #030000;
            color: #ffffff;
            border-radius: 5px;
            padding: 5px;
        }
        QLineEdit {
            background-color: #2c2c2c ;
            color: #ffffff;
            border: 2px solid #ffffff;
            border-radius: 15px;
            padding: 8px;
            font-size: 14px;
        }
        QPushButton:hover {
        background-color: #242424;
        }
        QPushButton:pressed {
            background-color: #FFFFFF;
        }
        QScrollArea {
            border: none;
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 5px;
        }
        QScrollBar:vertical {
            border: none;
            background: none;
            width: 10px;
            margin: 2px 2px 2px 2px;
            border-radius: 5px;
        }
        QScrollBar::handle:vertical {
            background: none;
            min-height: 20px;
            border-radius: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
        }
        QScrollBar::handle:vertical:hover {
            background: none;
        }
        QScrollBar::handle:vertical:pressed {
            background: #000000;
        }
        QScrollBar::track:vertical {
            background: none;
            border-radius: 5px;
        }
        """

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

    def populate_commands(self):
        for category, commands in self.commands.items():
            category_label = QLabel(f"<h3>{category}</h3>")
            self.command_layout.addWidget(category_label)
            
            for cmd in commands:
                if isinstance(cmd, dict) and "command" in cmd and "description" in cmd:
                    command_button = QPushButton(cmd['command'])
                    command_button.clicked.connect(lambda checked, c=cmd: self.show_command_popup(c))
                    self.command_layout.addWidget(command_button)
    
    def show_command_popup(self, cmd):
        popup = CommandPopup(cmd['command'], cmd['description'])
        popup.exec()

    def update_display(self):
        query = self.search_bar.text().strip().lower()
        for i in reversed(range(self.command_layout.count())):
            self.command_layout.itemAt(i).widget().setParent(None)
        for category, commands in self.commands.items():
            matching_commands = [cmd for cmd in commands if query in cmd["command"].lower() or query in cmd["description"].lower()]
            if matching_commands:
                category_label = QLabel(f"<h3>{category}</h3>")
                self.command_layout.addWidget(category_label)
                for cmd in matching_commands:
                    command_button = QPushButton(cmd['command'])
                    command_button.clicked.connect(lambda checked, c=cmd: self.show_command_popup(c))
                    self.command_layout.addWidget(command_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommandListWindow()
    window.show()
    sys.exit(app.exec())
