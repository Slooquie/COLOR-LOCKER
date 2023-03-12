from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QColor, QImage, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import cv2
import numpy as np

class ColorSelector(QWidget):
    color_changed = pyqtSignal(QColor)

    def __init__(self):
        super().__init__()

        # List of available colors
        self.colors = [
            QColor(Qt.red),
            QColor(Qt.green),
            QColor(Qt.blue),
            QColor(Qt.yellow),
            QColor(Qt.magenta),
            QColor(Qt.cyan),
            QColor(255, 128, 0),  # Orange
            QColor(128, 128, 128),  # Gray
            QColor(255, 255, 255),  # White
            QColor(0, 0, 0),  # Black
            QColor(255, 255, 0),  # Light yellow
            QColor(0, 255, 0),  # Lime green
            QColor(0, 128, 0),  # Forest green
            QColor(0, 0, 255),  # Dark blue
            QColor(0, 255, 255),  # Turquoise
            QColor(128, 0, 128),  # Purple
        ]

        self.initUI()

    def initUI(self):
        # Set up color buttons
        layout = QHBoxLayout()
        for color in self.colors:
            button = QPushButton('')
            button.setStyleSheet(f"background-color: {color.name()}")
            button.clicked.connect(lambda _, c=color: self.color_changed.emit(c))
            layout.addWidget(button)
        self.setLayout(layout)


class ColorDetector(QWidget):
    color_detected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # List of available colors
        self.colors = [
            ("Red", (0, 0, 255)),
            ("Green", (0, 255, 0)),
            ("Blue", (255, 0, 0)),
            ("Yellow", (0, 255, 255)),
            ("Magenta", (255, 0, 255)),
            ("Cyan", (255, 255, 0)),
            ("White", (255, 255, 255)),
            ("Black", (0, 0, 0)),
            ("Gray", (128, 128, 128)),
            ("Orange", (255, 128, 0)),
            ("Light yellow", (255, 255, 0)),
            ("Lime green", (0, 255, 0)),
            ("Forest green", (0, 128, 0)),
            ("Dark blue", (0, 0, 255)),
            ("Turquoise", (0, 255, 255)),
            ("Purple", (128, 0, 128)),
        ]

        # Default color detection settings
        self.detect_color = False
        self.lower_color = np.array([0, 0, 0])
        self.upper_color = np.array([0, 0, 0])

        self.initUI()

    def initUI(self):
        # Set up color selector
        self.color_selector = ColorSelector()
        self.color_selector.color_changed.connect(self.on_color_change)

        # Set up image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # Set up color detection checkbox
        self.color_detection_checkbox = QCheckBox('Color Detection')
        self.color_detection_checkbox.setChecked

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QColor, QImage, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import cv2
import numpy as np

class ColorSelector(QWidget):
    color_changed = pyqtSignal(QColor)

    def __init__(self):
        super().__init__()

        # List of available colors
        self.colors = [
            QColor(Qt.red),
            QColor(Qt.green),
            QColor(Qt.blue),
            QColor(Qt.yellow),
            QColor(Qt.magenta),
            QColor(Qt.cyan),
            QColor(255, 128, 0),  # Orange
            QColor(128, 128, 128),  # Gray
            QColor(255, 255, 255),  # White
            QColor(0, 0, 0),  # Black
            QColor(255, 255, 0),  # Light yellow
            QColor(0, 255, 0),  # Lime green
            QColor(0, 128, 0),  # Forest green
            QColor(0, 0, 255),  # Dark blue
            QColor(0, 255, 255),  # Turquoise
            QColor(128, 0, 128),  # Purple
        ]

        self.initUI()

    def initUI(self):
        # Set up color buttons
        layout = QHBoxLayout()
        for color in self.colors:
            button = QPushButton('')
            button.setStyleSheet(f"background-color: {color.name()}")
            button.clicked.connect(lambda _, c=color: self.color_changed.emit(c))
            layout.addWidget(button)
        self.setLayout(layout)


class ColorDetector(QWidget):
    color_detected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # List of available colors
        self.colors = [
            ("Red", (0, 0, 255)),
            ("Green", (0, 255, 0)),
            ("Blue", (255, 0, 0)),
            ("Yellow", (0, 255, 255)),
            ("Magenta", (255, 0, 255)),
            ("Cyan", (255, 255, 0)),
            ("White", (255, 255, 255)),
            ("Black", (0, 0, 0)),
            ("Gray", (128, 128, 128)),
            ("Orange", (255, 128, 0)),
            ("Light yellow", (255, 255, 0)),
            ("Lime green", (0, 255, 0)),
            ("Forest green", (0, 128, 0)),
            ("Dark blue", (0, 0, 255)),
            ("Turquoise", (0, 255, 255)),
            ("Purple", (128, 0, 128)),
        ]

        # Default color detection settings
        self.detect_color = False
        self.lower_color = np.array([0, 0, 0])
        self.upper_color = np.array([0, 0, 0])

        self.initUI()

    def initUI(self):
        # Set up color selector
        self.color_selector = ColorSelector()
        self.color_selector.color_changed.connect(self.on_color_change)

        # Set up image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # Set up color detection
