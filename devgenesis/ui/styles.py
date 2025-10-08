"""Stylesheet definitions for DevGenesis UI."""

DARK_THEME = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #0b0e12, stop:1 #111418);
    color: #f7f9fc;
}

QWidget {
    background-color: transparent;
    color: #f7f9fc;
    font-family: 'Inter', 'SF Pro Display', 'Segoe UI', sans-serif;
    font-size: 10pt;
    letter-spacing: 0.3px;
}

QWidget#headerWidget {
    background: transparent;
    border: none;
}

QWidget#bannerWidget {
    border-bottom: 2px solid #d4af37;
}

QWidget#headerOverlay {
    background: transparent;
}

QWidget#headerContent {
    background: rgba(23, 26, 31, 0.72);
    border: 1px solid rgba(212, 175, 55, 0.45);
    border-radius: 24px;
}

QWidget#projectTypePanel {
    background: rgba(14, 16, 19, 0.88);
    border: 1px solid rgba(212, 175, 55, 0.2);
    border-radius: 24px;
    padding: 12px;
}

QScrollArea#configurationScroll {
    border: none;
    background: transparent;
}

QLabel#logoLabel {
    background: transparent;
}

QLabel#titleLabel {
    font-size: 26pt;
    font-weight: 700;
    letter-spacing: 0.4px;
    color: #f2c94c;
}

QLabel#subtitleLabel {
    font-size: 11pt;
    color: #c9d6eb;
    font-weight: 500;
    padding: 8px 24px;
    border-radius: 20px;
    background: rgba(17, 20, 24, 0.78);
    border: 1px solid rgba(212, 175, 55, 0.35);
}

QLabel#sectionLabel {
    font-size: 13pt;
    font-weight: 600;
    color: #d4af37;
    margin-top: 8px;
    margin-bottom: 12px;
    letter-spacing: 0.4px;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #d4af37, stop:1 #c79f2d);
    color: #111418;
    border: 1px solid rgba(17, 20, 24, 0.15);
    border-radius: 18px;
    padding: 12px 28px;
    font-weight: 600;
    font-size: 10.5pt;
    letter-spacing: 0.4px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #ffdf7e, stop:1 #f2c94c);
    color: #111418;
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #c79f2d, stop:1 #a6791f);
}

QPushButton:disabled {
    background: rgba(32, 36, 43, 0.8);
    color: rgba(247, 249, 252, 0.35);
    border: 1px solid rgba(79, 83, 94, 0.4);
}

QPushButton#secondaryButton {
    background: rgba(17, 20, 24, 0.2);
    color: #d4af37;
    border: 1px solid rgba(212, 175, 55, 0.55);
    padding: 10px 22px;
}

QPushButton#secondaryButton:hover {
    background: rgba(244, 212, 121, 0.12);
    color: #111418;
}

QPushButton#secondaryIconButton {
    background: rgba(17, 20, 24, 0.45);
    color: #d4af37;
    border: 1px solid rgba(212, 175, 55, 0.45);
    border-radius: 16px;
    padding: 8px;
}

QPushButton#secondaryIconButton:hover {
    background: rgba(244, 212, 121, 0.2);
    color: #111418;
}

QPushButton#dangerButton {
    background: rgba(255, 107, 107, 0.16);
    color: #ff6b6b;
    border: 1px solid rgba(255, 107, 107, 0.55);
}

QPushButton#dangerButton:hover {
    background: rgba(255, 107, 107, 0.28);
    color: #111418;
}

QPushButton#themeToggleButton {
    background: rgba(17, 20, 24, 0.75);
    color: #d4af37;
    border: 1px solid rgba(212, 175, 55, 0.5);
    border-radius: 20px;
    padding: 6px 20px;
}

QPushButton#themeToggleButton:hover,
QPushButton#themeToggleButton:checked {
    background: rgba(244, 212, 121, 0.18);
    color: #f2c94c;
}

QLineEdit,
QTextEdit,
QPlainTextEdit {
    background-color: #1a1e23;
    border: 1px solid #2a2f38;
    border-radius: 16px;
    padding: 10px 14px;
    color: #f7f9fc;
    selection-background-color: #d4af37;
    selection-color: #111418;
}

QLineEdit:focus,
QTextEdit:focus,
QPlainTextEdit:focus {
    border: 1px solid #d4af37;
    box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.25);
    background-color: #1f232a;
}

QLineEdit::placeholder,
QTextEdit::placeholder,
QPlainTextEdit::placeholder {
    color: rgba(201, 214, 235, 0.45);
}

QComboBox {
    background-color: #1a1e23;
    border: 1px solid #2a2f38;
    border-radius: 16px;
    padding: 10px 14px;
    color: #f7f9fc;
}

QComboBox:hover {
    border: 1px solid #d4af37;
}

QComboBox::drop-down {
    width: 28px;
    border: none;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
    image: none;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid #d4af37;
    margin-right: 6px;
}

QComboBox QAbstractItemView {
    background-color: #171a1f;
    border: 1px solid rgba(212, 175, 55, 0.35);
    border-radius: 14px;
    selection-background-color: rgba(212, 175, 55, 0.25);
    selection-color: #f7f9fc;
    color: #f7f9fc;
}

QListWidget,
QTreeWidget,
QTableWidget {
    background-color: rgba(23, 26, 31, 0.82);
    border: 1px solid rgba(212, 175, 55, 0.22);
    border-radius: 18px;
    color: #f7f9fc;
    outline: none;
}

QListWidget::item,
QTreeWidget::item,
QTableWidget::item {
    padding: 12px;
    margin: 4px 6px;
    border-radius: 16px;
    color: #f7f9fc;
}

QListWidget#projectTypeList::item {
    min-height: 48px;
    border-left: 4px solid transparent;
}

QListWidget::item:selected,
QTreeWidget::item:selected,
QTableWidget::item:selected {
    background: rgba(212, 175, 55, 0.16);
    color: #f2c94c;
}

QListWidget#projectTypeList::item:selected {
    border-left: 4px solid #d4af37;
}

QListWidget::item:hover,
QTreeWidget::item:hover,
QTableWidget::item:hover {
    background: rgba(32, 36, 43, 0.75);
}

QListWidget#projectTypeList::item:hover {
    background: rgba(38, 43, 53, 0.85);
}

QGroupBox {
    background-color: rgba(23, 26, 31, 0.88);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 20px;
    margin-top: 24px;
    padding: 28px 24px 20px 24px;
    font-weight: 600;
    color: #f2c94c;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 14px;
    margin-left: 18px;
    background-color: #111418;
    border-radius: 16px;
    border: 1px solid rgba(212, 175, 55, 0.45);
    color: #d4af37;
    height: 28px;
    line-height: 28px;
}

QTabWidget::pane {
    border: 1px solid rgba(212, 175, 55, 0.18);
    border-radius: 20px;
    background: rgba(23, 26, 31, 0.86);
    margin-top: 12px;
}

QTabBar::tab {
    background: rgba(17, 20, 24, 0.6);
    color: rgba(199, 206, 221, 0.85);
    border: 1px solid transparent;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    padding: 10px 20px;
    margin-right: 4px;
}

QTabBar::tab:selected {
    background: rgba(244, 212, 121, 0.15);
    color: #f2c94c;
    border: 1px solid rgba(212, 175, 55, 0.45);
}

QTabBar::tab:hover:!selected {
    color: #ffdf7e;
}

QProgressBar {
    background: rgba(17, 20, 24, 0.8);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 18px;
    text-align: center;
    color: #f7f9fc;
    height: 26px;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #ffdf7e, stop:1 #d4af37);
    border-radius: 16px;
}

QCheckBox {
    spacing: 12px;
    color: #f7f9fc;
    font-weight: 500;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border-radius: 6px;
    border: 1px solid #2a2f38;
    background: #111418;
}

QCheckBox::indicator:hover {
    border: 1px solid #d4af37;
}

QCheckBox::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #f2c94c, stop:1 #d4af37);
    border: 1px solid #d4af37;
}

QRadioButton {
    color: #f7f9fc;
    font-weight: 500;
}

QRadioButton::indicator {
    width: 22px;
    height: 22px;
    border: 1px solid #2a2f38;
    border-radius: 11px;
    background: #111418;
}

QRadioButton::indicator:checked {
    border: 6px solid #d4af37;
}

QScrollBar:vertical {
    background: rgba(17, 20, 24, 0.75);
    width: 12px;
    margin: 6px 2px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: rgba(58, 63, 74, 0.85);
    border-radius: 6px;
    min-height: 40px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(212, 175, 55, 0.45);
}

QScrollBar:horizontal {
    background: rgba(17, 20, 24, 0.75);
    height: 12px;
    margin: 2px 6px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: rgba(58, 63, 74, 0.85);
    border-radius: 6px;
    min-width: 40px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(212, 175, 55, 0.45);
}

QScrollBar::add-line,
QScrollBar::sub-line {
    background: none;
    border: none;
}

QListView::item:selected:!active {
    background: rgba(212, 175, 55, 0.18);
}

QTreeWidget::item:selected:active {
    background: rgba(212, 175, 55, 0.18);
}

QToolTip {
    background: rgba(23, 26, 31, 0.92);
    color: #f7f9fc;
    border: 1px solid rgba(212, 175, 55, 0.45);
    border-radius: 12px;
    padding: 6px 10px;
}

QDialog {
    background: rgba(17, 20, 24, 0.96);
    border: 1px solid rgba(212, 175, 55, 0.35);
    border-radius: 20px;
}

QMenu {
    background: rgba(17, 20, 24, 0.94);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 16px;
}

QMenu::item {
    padding: 8px 16px;
    border-radius: 12px;
}

QMenu::item:selected {
    background: rgba(212, 175, 55, 0.18);
    color: #f2c94c;
}
"""

LIGHT_THEME = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #f1f3f7, stop:1 #e2e6ee);
    color: #1b1e24;
}

QWidget {
    background-color: transparent;
    color: #1b1e24;
    font-family: 'Inter', 'SF Pro Display', 'Segoe UI', sans-serif;
    font-size: 10pt;
    letter-spacing: 0.2px;
}

QWidget#headerWidget {
    background: transparent;
    border: none;
}

QWidget#bannerWidget {
    border-bottom: 2px solid #c09924;
}

QWidget#headerOverlay {
    background: transparent;
}

QWidget#headerContent {
    background: rgba(255, 255, 255, 0.82);
    border: 1px solid rgba(192, 153, 36, 0.45);
    border-radius: 24px;
}

QWidget#projectTypePanel {
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid rgba(192, 153, 36, 0.28);
    border-radius: 24px;
    padding: 12px;
}

QScrollArea#configurationScroll {
    border: none;
    background: transparent;
}

QLabel#titleLabel {
    font-size: 26pt;
    font-weight: 700;
    color: #c09924;
}

QLabel#subtitleLabel {
    font-size: 11pt;
    color: #4b4f58;
    font-weight: 500;
    padding: 8px 24px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.72);
    border: 1px solid rgba(192, 153, 36, 0.28);
}

QLabel#sectionLabel {
    font-size: 13pt;
    font-weight: 600;
    color: #c09924;
    margin-top: 8px;
    margin-bottom: 12px;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #f2c94c, stop:1 #d4af37);
    color: #1b1e24;
    border: 1px solid rgba(27, 30, 36, 0.08);
    border-radius: 18px;
    padding: 12px 28px;
    font-weight: 600;
    font-size: 10.5pt;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #ffdf7e, stop:1 #f8d96a);
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #d4af37, stop:1 #b98c1f);
}

QPushButton:disabled {
    background: #e0e3eb;
    color: rgba(27, 30, 36, 0.35);
    border: 1px solid rgba(27, 30, 36, 0.1);
}

QPushButton#secondaryButton {
    background: rgba(255, 255, 255, 0.7);
    color: #b0861f;
    border: 1px solid rgba(192, 153, 36, 0.5);
}

QPushButton#secondaryButton:hover {
    background: rgba(255, 223, 126, 0.22);
}

QPushButton#secondaryIconButton {
    background: rgba(255, 255, 255, 0.75);
    color: #b0861f;
    border: 1px solid rgba(192, 153, 36, 0.45);
    border-radius: 16px;
    padding: 8px;
}

QPushButton#secondaryIconButton:hover {
    background: rgba(255, 223, 126, 0.28);
}

QPushButton#dangerButton {
    background: rgba(255, 107, 107, 0.14);
    color: #c03535;
    border: 1px solid rgba(255, 107, 107, 0.45);
}

QPushButton#themeToggleButton {
    background: rgba(255, 255, 255, 0.78);
    color: #b0861f;
    border: 1px solid rgba(192, 153, 36, 0.5);
    border-radius: 20px;
    padding: 6px 20px;
}

QPushButton#themeToggleButton:hover,
QPushButton#themeToggleButton:checked {
    background: rgba(255, 223, 126, 0.24);
    color: #f2c94c;
}

QLineEdit,
QTextEdit,
QPlainTextEdit {
    background-color: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(176, 181, 196, 0.8);
    border-radius: 16px;
    padding: 10px 14px;
    color: #1b1e24;
    selection-background-color: #d4af37;
    selection-color: #111418;
}

QLineEdit:focus,
QTextEdit:focus,
QPlainTextEdit:focus {
    border: 1px solid #d4af37;
    background-color: rgba(255, 255, 255, 1.0);
}

QComboBox {
    background-color: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(176, 181, 196, 0.8);
    border-radius: 16px;
    padding: 10px 14px;
    color: #1b1e24;
}

QComboBox:hover {
    border: 1px solid #d4af37;
}

QComboBox::drop-down {
    width: 28px;
    border: none;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
    image: none;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid #c09924;
    margin-right: 6px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid rgba(192, 153, 36, 0.35);
    border-radius: 14px;
    selection-background-color: rgba(212, 175, 55, 0.22);
    selection-color: #1b1e24;
    color: #1b1e24;
}

QListWidget,
QTreeWidget,
QTableWidget {
    background-color: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(192, 153, 36, 0.25);
    border-radius: 18px;
    color: #1b1e24;
}

QListWidget::item,
QTreeWidget::item,
QTableWidget::item {
    padding: 12px;
    margin: 4px 6px;
    border-radius: 16px;
}

QListWidget::item:selected,
QTreeWidget::item:selected,
QTableWidget::item:selected {
    background: rgba(212, 175, 55, 0.18);
    color: #b0861f;
}

QListWidget#projectTypeList::item {
    min-height: 48px;
    border-left: 4px solid transparent;
}

QListWidget#projectTypeList::item:selected {
    border-left: 4px solid #d4af37;
}

QListWidget::item:hover,
QTreeWidget::item:hover,
QTableWidget::item:hover {
    background: rgba(212, 175, 55, 0.12);
}

QListWidget#projectTypeList::item:hover {
    background: rgba(255, 223, 126, 0.2);
}

QGroupBox {
    background-color: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(192, 153, 36, 0.35);
    border-radius: 20px;
    margin-top: 24px;
    padding: 28px 24px 20px 24px;
    font-weight: 600;
    color: #b0861f;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 14px;
    margin-left: 18px;
    background-color: rgba(255, 255, 255, 0.92);
    border-radius: 16px;
    border: 1px solid rgba(192, 153, 36, 0.45);
    color: #b0861f;
}

QTabWidget::pane {
    border: 1px solid rgba(192, 153, 36, 0.28);
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.9);
    margin-top: 12px;
}

QTabBar::tab {
    background: rgba(255, 255, 255, 0.7);
    color: #5a5f6d;
    border: 1px solid transparent;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    padding: 10px 20px;
    margin-right: 4px;
}

QTabBar::tab:selected {
    background: rgba(255, 223, 126, 0.3);
    color: #b0861f;
    border: 1px solid rgba(192, 153, 36, 0.45);
}

QTabBar::tab:hover:!selected {
    color: #c09924;
}

QProgressBar {
    background: rgba(255, 255, 255, 0.85);
    border: 1px solid rgba(192, 153, 36, 0.3);
    border-radius: 18px;
    text-align: center;
    color: #1b1e24;
    height: 26px;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #ffdf7e, stop:1 #d4af37);
    border-radius: 16px;
}

QCheckBox {
    spacing: 12px;
    color: #1b1e24;
    font-weight: 500;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border-radius: 6px;
    border: 1px solid rgba(176, 181, 196, 0.8);
    background: rgba(255, 255, 255, 0.9);
}

QCheckBox::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #f2c94c, stop:1 #d4af37);
    border: 1px solid #d4af37;
}

QRadioButton {
    color: #1b1e24;
    font-weight: 500;
}

QRadioButton::indicator {
    width: 22px;
    height: 22px;
    border-radius: 11px;
    border: 1px solid rgba(176, 181, 196, 0.8);
    background: rgba(255, 255, 255, 0.9);
}

QRadioButton::indicator:checked {
    border: 6px solid #d4af37;
}

QScrollBar:vertical {
    background: rgba(230, 233, 240, 0.85);
    width: 12px;
    margin: 6px 2px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: rgba(192, 153, 36, 0.35);
    border-radius: 6px;
    min-height: 40px;
}

QScrollBar:horizontal {
    background: rgba(230, 233, 240, 0.85);
    height: 12px;
    margin: 2px 6px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: rgba(192, 153, 36, 0.35);
    border-radius: 6px;
    min-width: 40px;
}

QScrollBar::add-line,
QScrollBar::sub-line {
    background: none;
    border: none;
}

QToolTip {
    background: rgba(255, 255, 255, 0.95);
    color: #1b1e24;
    border: 1px solid rgba(192, 153, 36, 0.4);
    border-radius: 12px;
    padding: 6px 10px;
}

QDialog {
    background: rgba(255, 255, 255, 0.94);
    border: 1px solid rgba(192, 153, 36, 0.3);
    border-radius: 20px;
}

QMenu {
    background: rgba(255, 255, 255, 0.94);
    border: 1px solid rgba(192, 153, 36, 0.3);
    border-radius: 16px;
}

QMenu::item {
    padding: 8px 16px;
    border-radius: 12px;
}

QMenu::item:selected {
    background: rgba(212, 175, 55, 0.2);
    color: #b0861f;
}
"""


def get_theme(theme_name: str) -> str:
    """Return the corresponding theme stylesheet."""
    return DARK_THEME if theme_name == "dark" else LIGHT_THEME
