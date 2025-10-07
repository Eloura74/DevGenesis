"""Dialog displaying a dry-run preview of a generation."""

from __future__ import annotations

from typing import Dict, Iterable

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QGroupBox,
    QPushButton,
    QPlainTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QTextEdit,
    QVBoxLayout,
)


class PreviewDialog(QDialog):
    """Simple dialog showing the preview of the generation plan."""

    def __init__(self, project_name: str, preview: Dict[str, Iterable], parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Aperçu – {project_name}")
        self.resize(760, 520)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        layout.addWidget(self._build_structure_group(project_name, preview))
        layout.addWidget(self._build_commands_group(preview))
        layout.addWidget(self._build_readme_group(preview))

        buttons = QDialogButtonBox(QDialogButtonBox.Close)
        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)

    def _build_structure_group(self, project_name: str, preview: Dict[str, Iterable]) -> QGroupBox:
        group = QGroupBox("Arborescence générée")
        tree = QTreeWidget()
        tree.setHeaderLabels(["Élément", "Type"])
        tree.setRootIsDecorated(True)
        tree.setAnimated(True)

        root_item = QTreeWidgetItem([project_name, "dossier"])
        tree.addTopLevelItem(root_item)

        for directory in preview.get("directories", []):
            self._ensure_tree_path(root_item, directory, is_file=False)

        for file_info in preview.get("files", []):
            self._ensure_tree_path(root_item, file_info["path"], is_file=True)

        tree.expandAll()
        layout = QVBoxLayout(group)
        layout.addWidget(tree)
        return group

    def _build_commands_group(self, preview: Dict[str, Iterable]) -> QGroupBox:
        group = QGroupBox("Commandes prévues")
        layout = QGridLayout(group)
        commands = preview.get("commands", []) or ["Aucune"]
        script = "\n".join(commands)

        script_edit = QPlainTextEdit()
        script_edit.setPlainText(script)
        script_edit.setReadOnly(True)
        script_edit.setFont(QFont("Monospace", 10))
        script_edit.setMinimumHeight(110)

        copy_btn = QPushButton("Copier le script")
        copy_btn.clicked.connect(lambda: QApplication.clipboard().setText(script))

        layout.addWidget(script_edit, 0, 0, 1, 2)
        layout.addWidget(copy_btn, 1, 1, alignment=Qt.AlignRight)
        return group

    def _build_readme_group(self, preview: Dict[str, Iterable]) -> QGroupBox:
        group = QGroupBox("README prévisionnel")
        readme = preview.get("readme") or "Aucun contenu README dans le template."
        editor = QTextEdit()
        editor.setReadOnly(True)
        editor.setPlainText(readme)
        editor.setMinimumHeight(150)

        layout = QVBoxLayout(group)
        layout.addWidget(editor)
        return group

    def _ensure_tree_path(self, root: QTreeWidgetItem, path: str, *, is_file: bool) -> None:
        parts = [part for part in path.split("/") if part]
        current = root
        for index, part in enumerate(parts):
            child = self._find_child(current, part)
            if child is None:
                item_type = "fichier" if is_file and index == len(parts) - 1 else "dossier"
                child = QTreeWidgetItem([part, item_type])
                current.addChild(child)
            current = child

    @staticmethod
    def _find_child(parent: QTreeWidgetItem, name: str) -> QTreeWidgetItem | None:
        for idx in range(parent.childCount()):
            if parent.child(idx).text(0) == name:
                return parent.child(idx)
        return None
