"""Main window for DevGenesis application - Refactored version."""

from typing import Any, Dict, Optional

from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QStyle,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from devgenesis.config import UI_CONFIG
from devgenesis.database import DatabaseService
from devgenesis.generator import generate_project_from_template
from devgenesis.ui.styles import get_theme

# Import refactored components
from devgenesis.ui.components import HeaderWidget
from devgenesis.ui.tabs import CustomTemplateTab, HistoryTab, NewProjectTab, SettingsTab, TemplatesTab


class GenerationWorker(QObject):
    """Worker object responsible for project generation."""

    progressed = Signal(str, str)
    finished = Signal(bool)

    def __init__(self, config: Dict[str, Any]):
        super().__init__()
        self._config = config

    @Slot()
    def run(self) -> None:
        """Execute the generation process in a worker thread."""
        try:
            success = generate_project_from_template(
                template=self._config["template"],
                project_name=self._config["project_name"],
                project_path=self._config["project_path"],
                description=self._config.get("description"),
                git_init=self._config.get("git_init", True),
                create_venv=self._config.get("create_venv", True),
                install_deps=self._config.get("install_deps", True),
                progress_callback=self._handle_progress,
            )
            self.finished.emit(success)
        except Exception as exc:  # pragma: no cover - defensive
            self.progressed.emit(str(exc), "error")
            self.finished.emit(False)

    def _handle_progress(self, message: str, level: str) -> None:
        self.progressed.emit(message, level)


class MainWindow(QMainWindow):
    """Main application window - Refactored to use component-based architecture"""

    def __init__(self):
        super().__init__()
        self.db = DatabaseService()
        self.generator_thread: Optional[QThread] = None
        self.generation_worker: Optional[GenerationWorker] = None
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
        self._add_tab(self.new_project_tab, QStyle.SP_FileDialogNewFolder, "Nouveau projet")
        self._add_tab(self.templates_tab, QStyle.SP_FileDialogListView, "Templates")
        self._add_tab(self.custom_template_tab, QStyle.SP_FileDialogDetailedView, "Créer template")
        self._add_tab(self.history_tab, QStyle.SP_FileDialogInfoView, "Historique")
        self._add_tab(self.settings_tab, QStyle.SP_FileDialogContentsView, "Paramètres")

        self._register_shortcuts()

    def _add_tab(self, widget: QWidget, icon_name: QStyle.StandardPixmap, label: str) -> None:
        icon = self.style().standardIcon(icon_name)
        self.tabs.addTab(widget, icon, label)

    def _register_shortcuts(self) -> None:
        actions = [
            ("new_project", "Nouveau projet", QKeySequence("Ctrl+N"), lambda: self.tabs.setCurrentWidget(self.new_project_tab)),
            ("generate", "Générer", QKeySequence("Ctrl+G"), self.new_project_tab.generate_project),
            ("focus_logs", "Focus logs", QKeySequence("Ctrl+L"), self.new_project_tab.focus_logs),
        ]

        for name, text, sequence, callback in actions:
            action = QAction(text, self)
            action.setShortcut(sequence)
            action.setObjectName(f"action_{name}")
            action.triggered.connect(callback)
            self.addAction(action)

    def on_generate_project(self, config: Dict[str, Any]):
        """Handle project generation request from NewProjectTab"""
        template = config.get("template")
        project_name = config.get("project_name")
        project_path = config.get("project_path")

        if not template or not project_name or not project_path:
            QMessageBox.warning(self, "Attention", "Veuillez remplir tous les champs requis")
            return

        # Set UI in progress state
        self.new_project_tab.set_generation_in_progress(True)

        # Start generation in thread
        self.generator_thread = QThread(self)
        self.generation_worker = GenerationWorker(config)
        self.generation_worker.moveToThread(self.generator_thread)

        self.generator_thread.started.connect(self.generation_worker.run)
        self.generation_worker.progressed.connect(self.new_project_tab.on_generation_progress)
        self.generation_worker.finished.connect(self._on_generation_complete)
        self.generation_worker.finished.connect(self.generator_thread.quit)
        self.generator_thread.finished.connect(self._cleanup_generation_thread)
        self.generator_thread.start()

    def _on_generation_complete(self, success: bool):
        """Handle generation completion with additional actions"""
        self.new_project_tab.on_generation_finished(success)

        if success:
            # Reload history tab
            self.history_tab.load_history()

    def _cleanup_generation_thread(self) -> None:
        if self.generation_worker:
            self.generation_worker.deleteLater()
            self.generation_worker = None
        if self.generator_thread:
            self.generator_thread.deleteLater()
            self.generator_thread = None

    def toggle_theme(self):
        """Toggle between light and dark theme"""
        self.theme = "light" if self.theme == "dark" else "dark"
        self.setStyleSheet(get_theme(self.theme))
        self.header.update_theme_button(self.theme)
