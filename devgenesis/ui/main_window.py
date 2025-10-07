"""Main window for DevGenesis application - Refactored version"""

from typing import Optional, Dict, Any
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QMessageBox
from PySide6.QtCore import QThread, Signal

from devgenesis.config import UI_CONFIG
from devgenesis.database import DatabaseService
from devgenesis.generator import generate_project_from_template
from devgenesis.ui.styles import get_theme

# Import refactored components
from devgenesis.ui.components import HeaderWidget
from devgenesis.ui.tabs import (
    NewProjectTab,
    TemplatesTab,
    CustomTemplateTab,
    HistoryTab,
    SettingsTab,
)


class GeneratorThread(QThread):
    """Thread for running project generation"""

    progress = Signal(str, str)  # message, level
    finished = Signal(bool)  # success

    def __init__(
        self,
        template: Dict[str, Any],
        project_name: str,
        project_path: str,
        description: str,
    ):
        super().__init__()
        self.template = template
        self.project_name = project_name
        self.project_path = project_path
        self.description = description

    def run(self):
        """Run the generation process"""
        try:
            success = generate_project_from_template(
                template=self.template,
                project_name=self.project_name,
                project_path=self.project_path,
                description=self.description,
                progress_callback=self._progress_callback,
            )
            self.finished.emit(success)
        except Exception as e:
            self.progress.emit(f"Erreur: {e}", "error")
            self.finished.emit(False)

    def _progress_callback(self, message: str, level: str):
        """Callback for progress updates"""
        self.progress.emit(message, level)


class MainWindow(QMainWindow):
    """Main application window - Refactored to use component-based architecture"""

    def __init__(self):
        super().__init__()
        self.db = DatabaseService()
        self.generator_thread: Optional[GeneratorThread] = None
        self.theme = "dark"

        self.init_ui()

    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle(UI_CONFIG["window_title"])
        self.setMinimumSize(UI_CONFIG["min_width"], UI_CONFIG["min_height"])
        self.resize(UI_CONFIG["window_width"], UI_CONFIG["window_height"])

        # Apply theme
        self.setStyleSheet(get_theme(self.theme))

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header component
        self.header = HeaderWidget()
        self.header.theme_toggle_requested.connect(self.toggle_theme)
        main_layout.addWidget(self.header)

        # Content container with padding
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 15, 20, 20)
        content_layout.setSpacing(15)

        # Tab widget
        self.tabs = QTabWidget()
        content_layout.addWidget(self.tabs)

        main_layout.addWidget(content_widget)

        # Create tabs using refactored components
        self.new_project_tab = NewProjectTab(self.db)
        self.new_project_tab.generate_requested.connect(self.on_generate_project)
        
        self.templates_tab = TemplatesTab(self.db)
        self.custom_template_tab = CustomTemplateTab(self.db)
        self.history_tab = HistoryTab(self.db)
        self.settings_tab = SettingsTab(self.db)

        # Add tabs to tab widget
        self.tabs.addTab(self.new_project_tab, "🚀 Nouveau Projet")
        self.tabs.addTab(self.templates_tab, "📦 Templates")
        self.tabs.addTab(self.custom_template_tab, "✨ Créer Template")
        self.tabs.addTab(self.history_tab, "📜 Historique")
        self.tabs.addTab(self.settings_tab, "⚙️ Paramètres")

    def on_generate_project(self, config: Dict[str, Any]):
        """Handle project generation request from NewProjectTab"""
        template = config.get("template")
        project_name = config.get("project_name")
        project_path = config.get("project_path")
        description = config.get("description", "")

        if not template or not project_name or not project_path:
            QMessageBox.warning(self, "Attention", "Veuillez remplir tous les champs requis")
            return

        # Set UI in progress state
        self.new_project_tab.set_generation_in_progress(True)

        # Start generation in thread
        self.generator_thread = GeneratorThread(
            template=template,
            project_name=project_name,
            project_path=project_path,
            description=description
        )
        self.generator_thread.progress.connect(self.new_project_tab.on_generation_progress)
        self.generator_thread.finished.connect(self._on_generation_complete)
        self.generator_thread.start()
    
    def _on_generation_complete(self, success: bool):
        """Handle generation completion with additional actions"""
        self.new_project_tab.on_generation_finished(success)
        
        if success:
            # Reload history tab
            self.history_tab.load_history()

    def toggle_theme(self):
        """Toggle between light and dark theme"""
        self.theme = "light" if self.theme == "dark" else "dark"
        self.setStyleSheet(get_theme(self.theme))
        self.header.update_theme_button(self.theme)
