"""History tab widget"""

import shutil

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from devgenesis.database import DatabaseService
from devgenesis.generator import preview_project_from_template
from devgenesis.logger import LOG_FILE
from devgenesis.ui.dialogs.preview_dialog import PreviewDialog
from devgenesis.ui.icons import load_icon


class HistoryTab(QWidget):
    """Project history tab"""
    
    def __init__(self, db: DatabaseService, parent=None):
        super().__init__(parent)
        self.db = db
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the history tab UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        label = QLabel("Historique des projets générés")
        label.setObjectName("sectionLabel")
        layout.addWidget(label)

        # History list
        self.history_list = QListWidget()
        self.history_list.setObjectName("historyList")
        layout.addWidget(self.history_list)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        icon_size = QSize(22, 22)

        refresh_btn = QPushButton("Actualiser")
        refresh_btn.setObjectName("secondaryButton")
        refresh_btn.setIcon(load_icon("refresh"))
        refresh_btn.setIconSize(icon_size)
        refresh_btn.clicked.connect(self.load_history)
        btn_layout.addWidget(refresh_btn)

        preview_btn = QPushButton("Aperçu")
        preview_btn.setObjectName("secondaryButton")
        preview_btn.setIcon(load_icon("preview"))
        preview_btn.setIconSize(icon_size)
        preview_btn.clicked.connect(self.preview_selection)
        btn_layout.addWidget(preview_btn)

        export_btn = QPushButton("Exporter les logs")
        export_btn.setObjectName("secondaryButton")
        export_btn.setIcon(load_icon("export"))
        export_btn.setIconSize(icon_size)
        export_btn.clicked.connect(self.export_logs)
        btn_layout.addWidget(export_btn)

        clear_btn = QPushButton("Effacer l'historique")
        clear_btn.setObjectName("dangerButton")
        clear_btn.setIcon(load_icon("delete"))
        clear_btn.setIconSize(icon_size)
        clear_btn.clicked.connect(self.clear_history)
        btn_layout.addWidget(clear_btn)

        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # Load initial history
        self.load_history()
    
    def load_history(self):
        """Load project history"""
        self.history_list.clear()
        history = self.db.get_project_history()

        for item in history:
            item_text = f"{item['project_name']} - {item['template_name']} ({item['created_at'][:10]})"
            list_item = QListWidgetItem(item_text)
            list_item.setData(Qt.ItemDataRole.UserRole, item)
            self.history_list.addItem(list_item)
    
    def clear_history(self):
        """Clear project history"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir effacer tout l'historique?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db.clear_history()
            self.load_history()
            QMessageBox.information(self, "Succès", "L'historique a été effacé")

    def export_logs(self) -> None:
        """Export the persistent application logs."""
        if not LOG_FILE.exists():
            QMessageBox.information(self, "Aucun log", "Aucun fichier de log n'a encore été généré.")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Exporter les logs",
            str(LOG_FILE.parent / "devgenesis.log"),
            "Fichier log (*.log);;Tous les fichiers (*)",
        )

        if not filename:
            return

        try:
            shutil.copy2(LOG_FILE, filename)
        except OSError as exc:
            QMessageBox.critical(self, "Export impossible", str(exc))
        else:
            QMessageBox.information(self, "Succès", f"Logs exportés vers {filename}")

    def preview_selection(self) -> None:
        """Open a dry-run preview based on the selected history entry."""
        item = self.history_list.currentItem()
        if not item:
            QMessageBox.information(self, "Aucun élément", "Sélectionnez un projet dans l'historique pour l'aperçu.")
            return

        data = item.data(Qt.ItemDataRole.UserRole)
        if not data or not data.get("template_name"):
            QMessageBox.warning(self, "Template manquant", "Impossible de retrouver le template associé.")
            return

        template = self.db.get_template_by_name(data["template_name"])
        if not template:
            QMessageBox.critical(self, "Introuvable", "Le template référencé n'est plus disponible.")
            return

        try:
            preview = preview_project_from_template(
                template=template,
                project_name=data["project_name"],
                project_path=data["project_path"],
            )
        except Exception as exc:  # pragma: no cover - UI feedback
            QMessageBox.critical(self, "Aperçu impossible", str(exc))
            return

        dialog = PreviewDialog(data["project_name"], preview, self)
        dialog.exec()
