"""Custom template creation tab widget"""

from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QListWidget,
    QListWidgetItem,
    QGroupBox,
    QScrollArea,
    QMessageBox,
    QFileDialog,
    QInputDialog,
)
from PySide6.QtCore import Signal, QSize
from devgenesis.custom_config import CustomProjectConfig, get_technology_suggestions
from devgenesis.ui.icons import load_icon


class CustomTemplateTab(QWidget):
    """Custom template creation tab"""
    
    template_saved = Signal()  # Signal when template is saved
    
    def __init__(self, custom_config: CustomProjectConfig, parent=None):
        super().__init__(parent)
        self.custom_config = custom_config
        self._init_ui()
    
    def _init_ui(self):
        """Initialize the custom template tab UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        label = QLabel("Créer un Template Personnalisé")
        label.setObjectName("sectionLabel")
        layout.addWidget(label)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(16)
        scroll_layout.setContentsMargins(8, 8, 8, 8)

        # Template info
        info_group = QGroupBox("Informations du Template")
        info_layout = QVBoxLayout(info_group)
        
        # Template name
        name_label = QLabel("Nom du template *")
        self.custom_template_name = QLineEdit()
        self.custom_template_name.setPlaceholderText("Mon Super Template")
        info_layout.addWidget(name_label)
        info_layout.addWidget(self.custom_template_name)
        
        # Description
        desc_label = QLabel("Description")
        self.custom_template_desc = QTextEdit()
        self.custom_template_desc.setPlaceholderText("Description de votre template...")
        self.custom_template_desc.setMaximumHeight(80)
        info_layout.addWidget(desc_label)
        info_layout.addWidget(self.custom_template_desc)
        
        scroll_layout.addWidget(info_group)
        
        # Technology suggestions
        tech_group = QGroupBox("Technologies Suggérées")
        tech_layout = QVBoxLayout(tech_group)
        
        # Category selector
        cat_label = QLabel("Catégorie")
        self.tech_category_combo = QComboBox()
        self.tech_category_combo.addItems([
            "Frontend", "Backend", "Database", "DevOps", "Testing", "Mobile", "Desktop"
        ])
        self.tech_category_combo.currentTextChanged.connect(self.on_tech_category_changed)
        tech_layout.addWidget(cat_label)
        tech_layout.addWidget(self.tech_category_combo)
        
        # Technology list
        self.tech_suggestions_list = QListWidget()
        self.tech_suggestions_list.setObjectName("techSuggestionsList")
        self.tech_suggestions_list.setMaximumHeight(160)
        tech_layout.addWidget(QLabel("Suggestions:"))
        tech_layout.addWidget(self.tech_suggestions_list)
        
        scroll_layout.addWidget(tech_group)
        
        # Structure patterns
        pattern_group = QGroupBox("Patterns de Structure")
        pattern_layout = QVBoxLayout(pattern_group)
        
        pattern_label = QLabel("Choisir un pattern de base")
        self.pattern_combo = QComboBox()
        self.pattern_combo.addItems([
            "Standard", "Monorepo", "Microservices", "Clean Architecture", "Feature-Based"
        ])
        pattern_layout.addWidget(pattern_label)
        pattern_layout.addWidget(self.pattern_combo)
        
        scroll_layout.addWidget(pattern_group)
        
        # Custom structure
        struct_group = QGroupBox("Structure Personnalisée")
        struct_layout = QVBoxLayout(struct_group)
        
        struct_label = QLabel("Dossiers (un par ligne)")
        self.custom_structure = QTextEdit()
        self.custom_structure.setPlaceholderText("src\nsrc/components\nsrc/utils\ntests\ndocs")
        self.custom_structure.setMaximumHeight(120)
        struct_layout.addWidget(struct_label)
        struct_layout.addWidget(self.custom_structure)
        
        scroll_layout.addWidget(struct_group)
        
        # Commands
        cmd_group = QGroupBox("Commandes d'Installation")
        cmd_layout = QVBoxLayout(cmd_group)
        
        cmd_label = QLabel("Commandes (une par ligne)")
        self.custom_commands = QTextEdit()
        self.custom_commands.setPlaceholderText("npm install\nnpm run build")
        self.custom_commands.setMaximumHeight(80)
        cmd_layout.addWidget(cmd_label)
        cmd_layout.addWidget(self.custom_commands)
        
        scroll_layout.addWidget(cmd_group)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        icon_size = QSize(22, 22)

        save_btn = QPushButton("Sauvegarder le template")
        save_btn.clicked.connect(self.save_custom_template)
        save_btn.setIcon(load_icon("save"))
        save_btn.setIconSize(icon_size)
        btn_layout.addWidget(save_btn)

        import_btn = QPushButton("Importer")
        import_btn.setObjectName("secondaryButton")
        import_btn.setIcon(load_icon("import"))
        import_btn.setIconSize(icon_size)
        import_btn.clicked.connect(self.import_custom_template)
        btn_layout.addWidget(import_btn)

        export_btn = QPushButton("Exporter")
        export_btn.setObjectName("secondaryButton")
        export_btn.setIcon(load_icon("export"))
        export_btn.setIconSize(icon_size)
        export_btn.clicked.connect(self.export_custom_template)
        btn_layout.addWidget(export_btn)
        
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # Initialize suggestions
        self.on_tech_category_changed("Frontend")
    
    def on_tech_category_changed(self, category: str):
        """Handle technology category change"""
        self.tech_suggestions_list.clear()
        
        category_key = category.lower()
        suggestions = get_technology_suggestions(category_key)
        
        for subcategory, techs in suggestions.items():
            for tech in techs:
                item = QListWidgetItem(f"• {tech} ({subcategory})")
                self.tech_suggestions_list.addItem(item)
    
    def save_custom_template(self):
        """Save custom template"""
        name = self.custom_template_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom de template")
            return
        
        description = self.custom_template_desc.toPlainText().strip()
        structure = [line.strip() for line in self.custom_structure.toPlainText().split('\n') if line.strip()]
        commands = [line.strip() for line in self.custom_commands.toPlainText().split('\n') if line.strip()]
        
        # Create template config
        template_config = {
            "name": name,
            "description": description or "Template personnalisé",
            "project_type": "custom",
            "technologies": [],
            "structure": structure or ["src", "tests", "docs"],
            "files": [
                {
                    "path": "README.md",
                    "content": f"# {{{{ project_name }}}}\n\n{description}",
                    "is_template": True
                },
                {
                    "path": ".gitignore",
                    "content": "node_modules/\n__pycache__/\n.venv/\n*.log",
                    "is_template": False
                }
            ],
            "commands": commands,
            "is_builtin": False
        }
        
        # Save to custom config
        if self.custom_config.save_config(name, template_config):
            QMessageBox.information(
                self,
                "Succès",
                f"Template '{name}' sauvegardé avec succès!\n\nVous pouvez maintenant l'utiliser dans l'onglet 'Nouveau Projet'."
            )
            
            # Clear form
            self.custom_template_name.clear()
            self.custom_template_desc.clear()
            self.custom_structure.clear()
            self.custom_commands.clear()
            
            # Emit signal
            self.template_saved.emit()
        else:
            QMessageBox.critical(self, "Erreur", "Impossible de sauvegarder le template")
    
    def import_custom_template(self):
        """Import custom template from file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Importer un template",
            str(Path.home()),
            "JSON Files (*.json);;YAML Files (*.yml *.yaml)"
        )
        
        if file_path:
            if self.custom_config.import_config(file_path):
                QMessageBox.information(self, "Succès", "Template importé avec succès!")
                self.template_saved.emit()
            else:
                QMessageBox.critical(self, "Erreur", "Impossible d'importer le template")
    
    def export_custom_template(self):
        """Export custom template to file"""
        # Get list of custom templates
        custom_templates = self.custom_config.list_configs()
        
        if not custom_templates:
            QMessageBox.information(
                self,
                "Information",
                "Aucun template personnalisé à exporter.\n\nCréez d'abord un template!"
            )
            return
        
        # Let user choose which template to export
        template_name, ok = QInputDialog.getItem(
            self,
            "Exporter un template",
            "Choisissez le template à exporter:",
            custom_templates,
            0,
            False
        )
        
        if ok and template_name:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Exporter le template",
                str(Path.home() / f"{template_name}.json"),
                "JSON Files (*.json)"
            )
            
            if file_path:
                if self.custom_config.export_config(template_name, file_path):
                    QMessageBox.information(self, "Succès", f"Template exporté vers:\n{file_path}")
                else:
                    QMessageBox.critical(self, "Erreur", "Impossible d'exporter le template")
