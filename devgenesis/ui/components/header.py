"""Header component with logo and banner"""

from pathlib import Path
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap


class HeaderWidget(QWidget):
    """Header widget with logo and banner background"""
    
    theme_toggle_requested = Signal()  # Signal when theme toggle is clicked
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the header UI"""
        self.setObjectName("headerWidget")
        self.setMinimumHeight(120)
        self.setMaximumHeight(120)
        
        # Get the project root directory
        project_root = Path(__file__).parent.parent.parent.parent
        banner_path = project_root / "images" / "banniere.png"
        logo_path = project_root / "images" / "logo.png"
        
        # Set banner as background with specific object name selector
        if banner_path.exists():
            banner_url = str(banner_path).replace('\\', '/')
            self.setStyleSheet(f"""
                QWidget#headerWidget {{
                    background-image: url('{banner_url}');
                    background-repeat: no-repeat;
                    background-position: center;
                    background-size: cover;
                    border-radius: 0px;
                }}
            """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(30, 15, 30, 15)

        # Logo
        if logo_path.exists():
            logo_label = QLabel()
            logo_label.setStyleSheet("background: transparent;")
            pixmap = QPixmap(str(logo_path))
            # Scale logo to fit header height while maintaining aspect ratio
            scaled_pixmap = pixmap.scaledToHeight(80, Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
            layout.addWidget(logo_label)
        else:
            # Fallback to text if logo not found
            title = QLabel("DevGenesis")
            title.setObjectName("titleLabel")
            layout.addWidget(title)

        layout.addStretch()

        # Theme toggle button
        self.theme_btn = QPushButton("🌙 Mode Clair")
        self.theme_btn.setObjectName("secondaryButton")
        self.theme_btn.setMaximumWidth(150)
        self.theme_btn.clicked.connect(self.theme_toggle_requested.emit)
        layout.addWidget(self.theme_btn)
    
    def update_theme_button(self, theme: str):
        """Update theme button text based on current theme"""
        self.theme = theme
        if theme == "dark":
            self.theme_btn.setText("🌙 Mode Clair")
        else:
            self.theme_btn.setText("☀️ Mode Sombre")
