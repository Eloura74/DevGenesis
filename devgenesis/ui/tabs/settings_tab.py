"""Settings tab widget"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox
from devgenesis.database import DatabaseService


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
