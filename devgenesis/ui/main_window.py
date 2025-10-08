"""Main window for DevGenesis application - Refactored version."""

from typing import Any, Dict, Optional

from PySide6.QtCore import QObject, QThread, Signal, Slot, QTimer
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from devgenesis.config import UI_CONFIG
from devgenesis.database import DatabaseService
from devgenesis.generator import generate_project_from_template
from devgenesis.ui.styles import get_theme
from devgenesis.ui.icons import load_icon
from devgenesis.ui.splash_screen import VideoOverlay, get_default_video_path, video_exists

# Import refactored components
from devgenesis.ui.components import HeaderWidget
from devgenesis.ui.tabs import CustomTemplateTab, HistoryTab, NewProjectTab, SettingsTab, TemplatesTab


# ====================================================================
# Worker pour la génération de projet
# ====================================================================

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
        except Exception as exc:
            self.progressed.emit(str(exc), "error")
            self.finished.emit(False)

    def _handle_progress(self, message: str, level: str) -> None:
        self.progressed.emit(message, level)


# ====================================================================
# Fenêtre principale
# ====================================================================

class MainWindow(QMainWindow):
    """Main application window - Component-based architecture."""

    def __init__(self):
        super().__init__()
        self.db = DatabaseService()
        self.generator_thread: Optional[QThread] = None
        self.generation_worker: Optional[GenerationWorker] = None
        self.theme = "dark"
        self.video_overlay: Optional[VideoOverlay] = None

        self.init_ui()

        # Lancer la vidéo d’intro après affichage de la fenêtre
        QTimer.singleShot(100, self._show_video_overlay)

    # ----------------------------------------------------------------
    # Interface
    # ----------------------------------------------------------------
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle(UI_CONFIG["window_title"])
        self.setMinimumSize(UI_CONFIG["min_width"], UI_CONFIG["min_height"])
        self.resize(UI_CONFIG["window_width"], UI_CONFIG["window_height"])

        # Thème
        self.setStyleSheet(get_theme(self.theme))

        # Conteneur principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header
        self.header = HeaderWidget()
        self.header.theme_toggle_requested.connect(self.toggle_theme)
        main_layout.addWidget(self.header)

        # Contenu
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(24, 24, 24, 24)
        content_layout.setSpacing(16)

        # Tabs
        self.tabs = QTabWidget()
        content_layout.addWidget(self.tabs)
        main_layout.addWidget(content_widget)

        # Création des onglets
        self.new_project_tab = NewProjectTab(self.db)
        self.new_project_tab.generate_requested.connect(self.on_generate_project)
        self.templates_tab = TemplatesTab(self.db)
        self.custom_template_tab = CustomTemplateTab(self.db)
        self.history_tab = HistoryTab(self.db)
        self.settings_tab = SettingsTab(self.db)

        # Ajout des onglets
        self._add_tab(self.new_project_tab, "new_project", "Nouveau projet")
        self._add_tab(self.templates_tab, "templates", "Templates")
        self._add_tab(self.custom_template_tab, "custom_template", "Créer template")
        self._add_tab(self.history_tab, "history", "Historique")
        self._add_tab(self.settings_tab, "settings", "Paramètres")

        self._register_shortcuts()

    # ----------------------------------------------------------------
    # Ajout des onglets
    # ----------------------------------------------------------------
    def _add_tab(self, widget: QWidget, icon_name: str, label: str) -> None:
        icon = load_icon(icon_name)
        self.tabs.addTab(widget, icon, label)

    # ----------------------------------------------------------------
    # Raccourcis clavier
    # ----------------------------------------------------------------
    def _register_shortcuts(self) -> None:
        actions = [
            ("new_project", "Nouveau projet", QKeySequence("Ctrl+N"),
             lambda: self.tabs.setCurrentWidget(self.new_project_tab)),
            ("generate", "Générer", QKeySequence("Ctrl+G"), self.new_project_tab.generate_project),
            ("focus_logs", "Focus logs", QKeySequence("Ctrl+L"), self.new_project_tab.focus_logs),
            ("refresh", "Actualiser", QKeySequence("F5"), self._refresh_current_tab),
        ]

        for name, text, sequence, callback in actions:
            action = QAction(text, self)
            action.setShortcut(sequence)
            action.setObjectName(f"action_{name}")
            action.triggered.connect(callback)
            self.addAction(action)

    # ----------------------------------------------------------------
    # Rafraîchissement onglets
    # ----------------------------------------------------------------
    def _refresh_current_tab(self) -> None:
        current = self.tabs.currentWidget()
        if current is self.templates_tab:
            self.templates_tab.load_templates()
        elif current is self.history_tab:
            self.history_tab.load_history()
        elif current is self.settings_tab:
            self.settings_tab.refresh_statistics()
        elif hasattr(current, "refresh"):
            current.refresh()

    # ----------------------------------------------------------------
    # Génération de projet
    # ----------------------------------------------------------------
    def on_generate_project(self, config: Dict[str, Any]):
        template = config.get("template")
        project_name = config.get("project_name")
        project_path = config.get("project_path")

        if not template or not project_name or not project_path:
            QMessageBox.warning(self, "Attention", "Veuillez remplir tous les champs requis")
            return

        # Blocage UI
        self.new_project_tab.set_generation_in_progress(True)

        # Thread
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
        self.new_project_tab.on_generation_finished(success)
        if success:
            self.history_tab.load_history()

    def _cleanup_generation_thread(self) -> None:
        if self.generation_worker:
            self.generation_worker.deleteLater()
            self.generation_worker = None
        if self.generator_thread:
            self.generator_thread.deleteLater()
            self.generator_thread = None

    # ----------------------------------------------------------------
    # Thème
    # ----------------------------------------------------------------
    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.setStyleSheet(get_theme(self.theme))
        self.header.update_theme_button(self.theme)

    # ----------------------------------------------------------------
    # Splash video
    # ----------------------------------------------------------------
    def _show_video_overlay(self):
        """Affiche la vidéo d’intro si disponible."""
        video_path = get_default_video_path()

        if not video_exists(video_path):
            print(f"[INFO] Vidéo non trouvée : {video_path}, splash ignoré.")
            return

        self.video_overlay = VideoOverlay(self, video_path)
        self.video_overlay.finished.connect(self._on_video_finished)
        self.video_overlay.setGeometry(self.rect())
        self.video_overlay.raise_()
        self.video_overlay.show()

    def _on_video_finished(self):
        """Appelé quand la vidéo se termine."""
        self.video_overlay = None

    # ----------------------------------------------------------------
    # Resize
    # ----------------------------------------------------------------
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.video_overlay:
            self.video_overlay.setGeometry(self.rect())
