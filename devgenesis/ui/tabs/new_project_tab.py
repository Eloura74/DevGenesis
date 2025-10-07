"""New project tab widget - Main project generation interface"""

from pathlib import Path
from typing import Optional, Dict, Any
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QTextEdit, QComboBox, QListWidget, QListWidgetItem,
    QFileDialog, QMessageBox, QProgressBar, QGroupBox, QScrollArea,
    QCheckBox, QSplitter
)
from PySide6.QtCore import Qt, Signal
from devgenesis.config import PROJECT_TYPES
from devgenesis.database import DatabaseService
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QTextEdit, QComboBox, QListWidget, QListWidgetItem,
    QFileDialog, QMessageBox, QProgressBar, QGroupBox, QScrollArea,
    QCheckBox, QSplitter,
    QFormLayout, QGridLayout, QSizePolicy   # <- ajouter ceci
)


class NewProjectTab(QWidget):
    """New project creation tab"""
    
    generate_requested = Signal(dict)  # Signal with project configuration
    
    def __init__(self, db: DatabaseService, parent=None):
        super().__init__(parent)
        self.db = db
        self.current_template: Optional[Dict[str, Any]] = None
        self._init_ui()
    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(10, 10, 10, 10)

        subtitle = QLabel("Générateur universel de projets et environnements de développement")
        subtitle.setObjectName("subtitleLabel")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(15)

        # Gauche
        left_panel = self._create_project_types_panel()
        left_panel.setFixedWidth(280)  # largeur stable
        content_layout.addWidget(left_panel)

        # Droite avec scroll
        right_scroll = QScrollArea()
        right_scroll.setWidgetResizable(True)
        right_panel = self._create_project_config_panel()
        right_scroll.setWidget(right_panel)
        content_layout.addWidget(right_scroll, 1)

        layout.addLayout(content_layout)
          
    def _create_project_types_panel(self) -> QWidget:
        """Create project types selection panel"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        # Section label with background
        label = QLabel("Type de projet")
        label.setObjectName("sectionLabel")
        label.setStyleSheet("""
            QLabel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #2a2a2a, stop:0.5 #3a3a3a, stop:1 #2a2a2a);
                border: 1px solid #b89850;
                border-radius: 8px;
                padding: 10px;
                font-size: 12pt;
                font-weight: 700;
                color: #d4af37;
            }
        """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Project types list
        self.project_types_list = QListWidget()
        self.project_types_list.setSpacing(5)

        for key, project_type in PROJECT_TYPES.items():
            item = QListWidgetItem(f"{project_type['icon']}  {project_type['name']}")
            item.setData(Qt.ItemDataRole.UserRole, key)
            item.setToolTip(project_type["description"])
            self.project_types_list.addItem(item)

        self.project_types_list.currentItemChanged.connect(self.on_project_type_selected)
        layout.addWidget(self.project_types_list)

        return widget
    
    def _create_project_config_panel(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout(widget)
        root.setSpacing(12)
        root.setContentsMargins(8, 8, 8, 8)

        # ===== Informations du projet =====
        info_group = QGroupBox("Informations du projet")
        info_form = QFormLayout(info_group)
        info_form.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)
        info_form.setFormAlignment(Qt.AlignTop)
        info_form.setHorizontalSpacing(10)
        info_form.setVerticalSpacing(8)
        info_form.setContentsMargins(16, 12, 16, 12)

        # Nom
        self.project_name_input = QLineEdit()
        self.project_name_input.setPlaceholderText("Nom du projet *")
        info_form.addRow(QLabel("Nom :"), self.project_name_input)

        # Emplacement
        path_row = QWidget()
        path_h = QHBoxLayout(path_row)
        path_h.setContentsMargins(0, 0, 0, 0)
        path_h.setSpacing(6)
        self.project_path_input = QLineEdit()
        self.project_path_input.setPlaceholderText("Emplacement *")
        default_path = str(Path.home() / "Documents" / "DevGenesis")
        self.project_path_input.setText(default_path)
        path_browse_btn = QPushButton("📁")
        path_browse_btn.setObjectName("secondaryButton")
        path_browse_btn.setFixedWidth(36)
        path_browse_btn.clicked.connect(self.browse_project_path)
        path_h.addWidget(self.project_path_input, 1)
        path_h.addWidget(path_browse_btn, 0)
        info_form.addRow(QLabel("Chemin :"), path_row)

        # Description
        self.project_desc_input = QTextEdit()
        self.project_desc_input.setPlaceholderText("Description (optionnelle)")
        self.project_desc_input.setFixedHeight(80)
        info_form.addRow(QLabel("Description :"), self.project_desc_input)

        root.addWidget(info_group)

        # ===== Template =====
        template_group = QGroupBox("Template")
        template_form = QFormLayout(template_group)
        template_form.setLabelAlignment(Qt.AlignRight | Qt.AlignVCenter)
        template_form.setHorizontalSpacing(10)
        template_form.setVerticalSpacing(8)
        template_form.setContentsMargins(16, 12, 16, 12)

        self.template_combo = QComboBox()
        self.template_combo.currentIndexChanged.connect(self.on_template_selected)
        template_form.addRow(QLabel("Sélection :"), self.template_combo)

        self.template_desc_label = QLabel("")
        self.template_desc_label.setWordWrap(True)
        self.template_desc_label.setStyleSheet("color:#b8b8b8;font-style:italic;font-size:9pt;")
        self.template_desc_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        template_form.addRow(QLabel("Résumé :"), self.template_desc_label)

        self.tech_label = QLabel("")
        self.tech_label.setWordWrap(True)
        self.tech_label.setStyleSheet("color:#d4af37;font-size:9pt;font-weight:600;")
        template_form.addRow(QLabel("Recommandé :"), self.tech_label)

        root.addWidget(template_group)

        # ===== Options =====
        options_group = QGroupBox("Options")
        options_group.setContentsMargins(0, 0, 0, 0)
        options_grid = QGridLayout(options_group)
        options_grid.setContentsMargins(16, 12, 16, 12)
        options_grid.setHorizontalSpacing(20)
        options_grid.setVerticalSpacing(6)

        self.git_init_checkbox = QCheckBox("Initialiser Git")
        self.git_init_checkbox.setChecked(True)
        self.venv_checkbox = QCheckBox("Créer environnement virtuel")
        self.venv_checkbox.setChecked(True)
        self.install_deps_checkbox = QCheckBox("Installer dépendances")
        self.install_deps_checkbox.setChecked(True)

        options_grid.addWidget(self.git_init_checkbox, 0, 0)
        options_grid.addWidget(self.venv_checkbox,      0, 1)
        options_grid.addWidget(self.install_deps_checkbox, 1, 0)

        root.addWidget(options_group)

        # ===== Actions & logs =====
        self.generate_btn = QPushButton("Générer le projet")
        self.generate_btn.setMinimumHeight(42)
        self.generate_btn.clicked.connect(self.generate_project)
        root.addWidget(self.generate_btn)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setTextVisible(False)
        root.addWidget(self.progress_bar)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setMinimumHeight(140)
        self.log_output.setPlaceholderText("Les logs de génération apparaîtront ici…")
        root.addWidget(self.log_output)

        root.addStretch(1)
        return widget

    def on_project_type_selected(self, current, previous):
        """Handle project type selection"""
        if not current:
            return

        project_type_key = current.data(Qt.ItemDataRole.UserRole)
        project_type = PROJECT_TYPES[project_type_key]

        # Update template combo box
        self.template_combo.clear()
        templates = self.db.get_templates_by_type(project_type_key)

        if not templates:
            # If no templates for this type, show all templates
            templates = self.db.get_all_templates()

        for template in templates:
            self.template_combo.addItem(template["name"], template)

        # Show recommended technologies
        recommended = ", ".join(project_type["recommended_tech"])
        self.tech_label.setText(f"<b>Technologies recommandées:</b> {recommended}")
    
    def on_template_selected(self, index):
        """Handle template selection"""
        if index < 0:
            return

        template = self.template_combo.itemData(index)
        if template:
            self.current_template = template
            self.template_desc_label.setText(template["description"])
    
    def browse_project_path(self):
        """Browse for project path"""
        path = QFileDialog.getExistingDirectory(
            self,
            "Sélectionner l'emplacement du projet",
            str(Path.home()),
        )
        if path:
            self.project_path_input.setText(path)
    
    def generate_project(self):
        """Validate and emit generate signal"""
        # Validate inputs
        project_name = self.project_name_input.text().strip()
        if not project_name:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom de projet")
            return

        project_path = self.project_path_input.text().strip()
        if not project_path:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un emplacement")
            return

        if not self.current_template:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un template")
            return

        # Get full project path
        full_path = str(Path(project_path) / project_name)

        # Check if directory exists
        if Path(full_path).exists():
            reply = QMessageBox.question(
                self,
                "Confirmation",
                f"Le répertoire {full_path} existe déjà. Continuer?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.No:
                return

        # Get description
        description = self.project_desc_input.toPlainText().strip()

        # Emit signal with configuration
        config = {
            "template": self.current_template,
            "project_name": project_name,
            "project_path": full_path,
            "description": description,
            "git_init": self.git_init_checkbox.isChecked(),
            "create_venv": self.venv_checkbox.isChecked(),
            "install_deps": self.install_deps_checkbox.isChecked(),
        }
        
        self.generate_requested.emit(config)
    
    def log(self, message: str, level: str = "info"):
        """Add message to log output"""
        color_map = {
            "info": "#89b4fa",
            "success": "#a6e3a1",
            "warning": "#f9e2af",
            "error": "#f38ba8",
        }
        color = color_map.get(level, "#cdd6f4")
        self.log_output.append(f'<span style="color: {color};">{message}</span>')
    
    def set_generation_in_progress(self, in_progress: bool):
        """Set UI state for generation in progress"""
        self.generate_btn.setEnabled(not in_progress)
        self.progress_bar.setVisible(in_progress)
        if in_progress:
            self.progress_bar.setRange(0, 0)  # Indeterminate
            self.log_output.clear()
            self.log("🚀 Démarrage de la génération du projet...", "info")
    
    def on_generation_progress(self, message: str, level: str):
        """Handle generation progress updates"""
        self.log(message, level)
    
    def on_generation_finished(self, success: bool):
        """Handle generation completion"""
        self.set_generation_in_progress(False)
        if success:
            self.log("✅ Projet généré avec succès!", "success")
        else:
            self.log("❌ Échec de la génération du projet", "error")
