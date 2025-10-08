"""Settings tab widget"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from devgenesis.database import DatabaseService
from devgenesis.services.environment import check_environment


class SettingsTab(QWidget):
    """Settings and about tab"""
    
    def __init__(self, db: DatabaseService, parent=None):
        super().__init__(parent)
        self.db = db
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the settings tab UI"""
        layout = QVBoxLayout(self)

        label = QLabel("Paramètres")
        label.setObjectName("sectionLabel")
        layout.addWidget(label)

        # Statistics
        stats_group = QGroupBox("Statistiques")
        stats_layout = QVBoxLayout(stats_group)

        self.stats_label = QLabel()
        self.stats_label.setWordWrap(True)
        stats_layout.addWidget(self.stats_label)

        layout.addWidget(stats_group)

        # Environment checks
        env_group = QGroupBox("Environnement système")
        env_layout = QVBoxLayout(env_group)

        self.env_button = QPushButton("Tester l'environnement")
        self.env_button.clicked.connect(self.run_environment_checks)
        env_layout.addWidget(self.env_button, alignment=Qt.AlignLeft)

        self.env_result_table = QTableWidget(0, 4)
        self.env_result_table.setHorizontalHeaderLabels(["Outil", "Statut", "Version", "Suggestion"])
        self.env_result_table.verticalHeader().setVisible(False)
        self.env_result_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.env_result_table.setSelectionMode(QTableWidget.NoSelection)
        self.env_result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.env_result_table.setMinimumHeight(180)
        env_layout.addWidget(self.env_result_table)

        layout.addWidget(env_group)

        # About
        about_group = QGroupBox("À propos")
        about_layout = QVBoxLayout(about_group)

        about_text = """
        <h3>DevGenesis v1.0.0</h3>
        <p>Générateur universel de projets et environnements de développement</p>
        <p><b>Objectif:</b> Supprimer la phase fastidieuse de configuration initiale 
        des projets pour permettre aux développeurs de se concentrer directement 
        sur la logique métier et le code applicatif.</p>
        <p><b>Fonctionnalités:</b></p>
        <ul>
            <li>Génération automatique de projets</li>
            <li>Templates prédéfinis pour React, FastAPI, Django, etc.</li>
            <li>Installation automatique des dépendances</li>
            <li>Configuration Git et environnements virtuels</li>
        </ul>
        """
        about_label = QLabel(about_text)
        about_label.setWordWrap(True)
        about_layout.addWidget(about_label)

        layout.addWidget(about_group)
        layout.addStretch()
        
        # Load initial statistics
        self.refresh_statistics()

    def refresh_statistics(self):
        """Refresh statistics display"""
        stats = self.db.get_statistics()
        stats_text = f"""
        <b>Templates disponibles:</b> {stats['total_templates']}<br>
        <b>Templates intégrés:</b> {stats['builtin_templates']}<br>
        <b>Templates personnalisés:</b> {stats['custom_templates']}<br>
        <b>Projets générés:</b> {stats['total_projects']}<br>
        <b>Projets réussis:</b> {stats['successful_projects']}
        """
        self.stats_label.setText(stats_text)

    def run_environment_checks(self) -> None:
        """Run environment pre-flight checks and populate the table."""
        self.env_button.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            results = check_environment()
        finally:
            QApplication.restoreOverrideCursor()
            self.env_button.setEnabled(True)

        self.env_result_table.setRowCount(len(results))
        for row, result in enumerate(results):
            status_text = "OK" if result.available else "Manquant"
            status_item = QTableWidgetItem(status_text)
            status_item.setTextAlignment(Qt.AlignCenter)
            status_color = QColor("#3fb950") if result.available else QColor("#f85149")
            status_item.setForeground(QBrush(status_color))

            self.env_result_table.setItem(row, 0, QTableWidgetItem(result.tool))
            self.env_result_table.setItem(row, 1, status_item)
            self.env_result_table.setItem(row, 2, QTableWidgetItem(result.version or "-"))
            self.env_result_table.setItem(row, 3, QTableWidgetItem(result.suggestion))
