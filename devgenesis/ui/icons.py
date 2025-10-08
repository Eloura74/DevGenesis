"""Utilities for loading and tinting SVG icons for the DevGenesis UI."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer

ICON_ROOT = Path(__file__).resolve().parent.parent.parent / "images" / "icons"

# Default palette aligned with the "Or Tech" art direction
ICON_COLORS = {
    "normal_off": QColor("#d4af37"),
    "hover_off": QColor("#ffdf7e"),
    "active_off": QColor("#f2c94c"),
    "disabled_off": QColor("#3f434d"),
    "normal_on": QColor("#f2c94c"),
    "hover_on": QColor("#ffdf7e"),
    "active_on": QColor("#f2c94c"),
    "disabled_on": QColor("#3f434d"),
}


def _render_svg(path: Path, color: QColor, size: QSize) -> QPixmap:
    """Render an SVG file to a transparent pixmap tinted with ``color``."""
    if not path.exists():
        pixmap = QPixmap(size)
        pixmap.fill(Qt.GlobalColor.transparent)
        return pixmap

    data = path.read_text(encoding="utf-8").replace("currentColor", color.name())
    renderer = QSvgRenderer(bytearray(data, "utf-8"))
    pixmap = QPixmap(size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    renderer.render(painter)
    painter.end()
    return pixmap


@lru_cache(maxsize=64)
def load_icon(name: str, size: int = 24) -> QIcon:
    """Load an SVG icon and build a themed :class:`QIcon` instance."""
    svg_path = ICON_ROOT / f"{name}.svg"
    icon = QIcon()
    icon_size = QSize(size, size)

    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["normal_off"], icon_size), QIcon.Mode.Normal, QIcon.State.Off)
    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["hover_off"], icon_size), QIcon.Mode.Active, QIcon.State.Off)
    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["active_off"], icon_size), QIcon.Mode.Selected, QIcon.State.Off)
    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["disabled_off"], icon_size), QIcon.Mode.Disabled, QIcon.State.Off)

    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["normal_on"], icon_size), QIcon.Mode.Normal, QIcon.State.On)
    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["hover_on"], icon_size), QIcon.Mode.Active, QIcon.State.On)
    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["active_on"], icon_size), QIcon.Mode.Selected, QIcon.State.On)
    icon.addPixmap(_render_svg(svg_path, ICON_COLORS["disabled_on"], icon_size), QIcon.Mode.Disabled, QIcon.State.On)

    return icon


__all__ = ["load_icon"]
