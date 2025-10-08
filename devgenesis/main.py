"""Main entry point for DevGenesis application"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from devgenesis.ui.main_window import MainWindow


def main():
    """Main application entry point"""
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("DevGenesis")
    app.setOrganizationName("DevGenesis")
    app.setApplicationVersion("1.0.0")

    # Create and show main window (video overlay will show automatically)
    window = MainWindow()
    window.show()

    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
