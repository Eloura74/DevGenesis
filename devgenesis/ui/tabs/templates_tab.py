"""Templates management tab widget"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QListWidget, QListWidgetItem
)
from PySide6.QtCore import Qt, Signal
from devgenesis.database import DatabaseService


class TemplatesTab(QWidget):
    """Templates management tab"""
    
    refresh_requested = Signal()  # Signal when refresh is requested
    
    def __init__(self, db: DatabaseService, parent=None):
        super().__init__(parent)
        self.db = db
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the templates tab UI"""
        layout = QVBoxLayout(self)

        label = QLabel("Gestion des Templates")
        label.setObjectName("sectionLabel")
        layout.addWidget(label)

        # Templates list
        self.templates_list = QListWidget()
        layout.addWidget(self.templates_list)

        # Buttons
        btn_layout = QHBoxLayout()
        refresh_btn = QPushButton("🔄 Actualiser")
        refresh_btn.setObjectName("secondaryButton")
        refresh_btn.clicked.connect(self._on_refresh)
        btn_layout.addWidget(refresh_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # Load initial templates
        self.load_templates()
    
    def _on_refresh(self):
        """Handle refresh button click"""
        self.load_templates()
        self.refresh_requested.emit()
    
    def load_templates(self):
        """Load templates from database"""
        templates = self.db.get_all_templates()

        # Update templates list
        self.templates_list.clear()
        for template in templates:
            item_text = f"{template['name']} - {template['description']}"
            if template['is_builtin']:
                item_text += " [Intégré]"
            item = QListWidgetItem(item_text)
            item.setData(Qt.ItemDataRole.UserRole, template)
            self.templates_list.addItem(item)
