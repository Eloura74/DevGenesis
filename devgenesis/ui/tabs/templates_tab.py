"""Templates management tab widget"""

from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QInputDialog,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QStyle

from devgenesis.database import DatabaseService
from devgenesis.generator import preview_project_from_template
from devgenesis.ui.dialogs.preview_dialog import PreviewDialog


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
        refresh_btn = QPushButton("Actualiser")
        refresh_btn.setObjectName("secondaryButton")
        refresh_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload))
        refresh_btn.clicked.connect(self._on_refresh)
        btn_layout.addWidget(refresh_btn)

        preview_btn = QPushButton("Aperçu")
        preview_btn.setObjectName("secondaryButton")
        preview_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView))
        preview_btn.clicked.connect(self._on_preview)
        btn_layout.addWidget(preview_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # Load initial templates
        self.load_templates()
    
    def _on_refresh(self):
        """Handle refresh button click"""
        self.load_templates()
        self.refresh_requested.emit()

    def _on_preview(self):
        """Open a dry-run preview for the selected template."""
        item = self.templates_list.currentItem()
        if not item:
            QMessageBox.information(self, "Aucun template", "Veuillez sélectionner un template à prévisualiser.")
            return

        template = item.data(Qt.ItemDataRole.UserRole)
        if not template:
            QMessageBox.warning(self, "Template invalide", "Le template sélectionné est introuvable.")
            return

        project_name, ok = QInputDialog.getText(
            self,
            "Nom du projet",
            "Entrez un nom de projet pour l'aperçu:",
            text=template["name"],
        )
        if not ok or not project_name.strip():
            return

        try:
            preview = preview_project_from_template(
                template=template,
                project_name=project_name.strip(),
                project_path=str(Path.home() / "DevGenesis" / project_name.strip()),
            )
        except Exception as exc:  # pragma: no cover - UI feedback
            QMessageBox.critical(self, "Aperçu impossible", str(exc))
            return

        dialog = PreviewDialog(project_name.strip(), preview, self)
        dialog.exec()

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
