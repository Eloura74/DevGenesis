"""History tab widget"""

import shutil

from PySide6.QtCore import Qt
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
from devgenesis.logger import LOG_FILE


class HistoryTab(QWidget):
    """Project history tab"""
    
    def __init__(self, db: DatabaseService, parent=None):
        super().__init__(parent)
        self.db = db
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the history tab UI"""
        layout = QVBoxLayout(self)

        label = QLabel("Historique des projets générés")
        label.setObjectName("sectionLabel")
        layout.addWidget(label)

        # History list
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)

        # Buttons
        btn_layout = QHBoxLayout()
        refresh_btn = QPushButton("🔄 Actualiser")
        refresh_btn.setObjectName("secondaryButton")
        refresh_btn.clicked.connect(self.load_history)
        btn_layout.addWidget(refresh_btn)

        export_btn = QPushButton("💾 Exporter les logs")
        export_btn.setObjectName("secondaryButton")
        export_btn.clicked.connect(self.export_logs)
        btn_layout.addWidget(export_btn)

        clear_btn = QPushButton("🗑️ Effacer l'historique")
        clear_btn.setObjectName("dangerButton")
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
