"""Header component with banner background, logo overlay, and theme toggle."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)


class BannerWidget(QWidget):
    """Widget responsible for painting the banner background image."""

    def __init__(self, banner_path: Path, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("bannerWidget")
        self._pixmap: QPixmap | None = None
        if banner_path.exists():
            self._pixmap = QPixmap(str(banner_path))

    def paintEvent(self, event) -> None:  # type: ignore[override]
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
        if self._pixmap:
            scaled = self._pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            painter.drawPixmap(0, 0, scaled)
        else:
            painter.fillRect(self.rect(), Qt.GlobalColor.transparent)
        painter.end()


class HeaderWidget(QWidget):
    """Header widget featuring a full-width banner, logo overlay, and theme toggle."""

    theme_toggle_requested = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.theme = "dark"
        self._project_root = Path(__file__).parent.parent.parent.parent
        self._banner: BannerWidget | None = None
        self._overlay: QWidget | None = None
        self.theme_btn: QPushButton
        self._logo_label: QLabel | None = None
        self._init_ui()

    def _init_ui(self) -> None:
        self.setObjectName("headerWidget")
        self.setMinimumHeight(120)
        self.setMaximumHeight(120)

        banner_path = self._project_root / "images" / "banniere.png"
        logo_path = self._project_root / "images" / "logo.png"

        self._banner = BannerWidget(banner_path, self)
        self._banner.lower()

        self._overlay = QWidget(self)
        self._overlay.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, False)
        self._overlay.setObjectName("headerOverlay")

        overlay_layout = QHBoxLayout(self._overlay)
        overlay_layout.setContentsMargins(24, 10, 24, 10)
        overlay_layout.setSpacing(12)

        if logo_path.exists():
            logo_pixmap = QPixmap(str(logo_path))
            if not logo_pixmap.isNull():
                logo_label = QLabel(self._overlay)
                logo_label.setStyleSheet("background: transparent;")
                scaled = logo_pixmap.scaledToHeight(
                    80, Qt.TransformationMode.SmoothTransformation
                )
                logo_label.setPixmap(scaled)
                self._logo_label = logo_label
                overlay_layout.addWidget(
                    logo_label, alignment=Qt.AlignmentFlag.AlignTop
                )
            else:
                self._add_fallback_title(overlay_layout)
        else:
            self._add_fallback_title(overlay_layout)

        overlay_layout.addStretch()

        self.theme_btn = QPushButton(self._overlay)
        self.theme_btn.setObjectName("themeToggleButton")
        self.theme_btn.setCheckable(True)
        self.theme_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_btn.clicked.connect(self._on_theme_button_clicked)
        overlay_layout.addWidget(
            self.theme_btn, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
        )

        self.update_theme_button(self.theme)

        if self._banner is not None:
            self._banner.setGeometry(self.rect())
        if self._overlay is not None:
            self._overlay.setGeometry(self.rect())

    def resizeEvent(self, event) -> None:  # type: ignore[override]
        super().resizeEvent(event)
        if self._banner is not None:
            self._banner.setGeometry(self.rect())
        if self._overlay is not None:
            self._overlay.setGeometry(self.rect())

    def update_theme_button(self, theme: str) -> None:
        self.theme = theme
        is_light = theme == "light"
        previous_state = self.theme_btn.blockSignals(True)
        self.theme_btn.setChecked(is_light)
        self.theme_btn.blockSignals(previous_state)
        self._refresh_theme_button_label(is_light)

    def _add_fallback_title(self, layout: QHBoxLayout) -> None:
        title = QLabel("DevGenesis", self._overlay)
        title.setObjectName("titleLabel")
        self._logo_label = title
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)

    def _refresh_theme_button_label(self, is_light: bool) -> None:
        if is_light:
            self.theme_btn.setText("☀️ Mode Sombre")
        else:
            self.theme_btn.setText("🌙 Mode Clair")

    def _on_theme_button_clicked(self) -> None:
        is_light = self.theme_btn.isChecked()
        self.theme = "light" if is_light else "dark"
        self._refresh_theme_button_label(is_light)
        self.theme_toggle_requested.emit()
