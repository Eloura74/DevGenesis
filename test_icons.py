"""Test script for icons"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

try:
    from devgenesis.ui.icons import IconProvider, SVG_AVAILABLE
    print(f"SVG Available: {SVG_AVAILABLE}")
    
    app = QApplication(sys.argv)
    window = QMainWindow()
    widget = QWidget()
    layout = QVBoxLayout(widget)
    
    # Test icons
    for icon_name in ["new_project", "templates", "settings"]:
        icon = IconProvider.get_icon(icon_name, "#f2c94c", 48)
        print(f"Icon '{icon_name}' null: {icon.isNull()}")
        
        label = QLabel(f"Icon: {icon_name}")
        if not icon.isNull():
            pixmap = icon.pixmap(48, 48)
            label.setPixmap(pixmap)
        layout.addWidget(label)
    
    window.setCentralWidget(widget)
    window.show()
    
    print("Window displayed. Close to exit.")
    sys.exit(app.exec())
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
