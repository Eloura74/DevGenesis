"""Stylesheet definitions for DevGenesis UI"""

DARK_THEME = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #0a0a0a, stop:1 #1a1a1a);
}

QWidget {
    background-color: transparent;
    color: #f0f0f0;
    font-family: 'Segoe UI', 'SF Pro Display', Arial, sans-serif;
    font-size: 10pt;
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

QPushButton#themeToggleButton {
    background: transparent;
    color: #f0f0f0;
    border: 1px solid rgba(244, 244, 244, 0.35);
    border-radius: 18px;
    padding: 6px 18px;
    font-weight: 600;
}

QPushButton#themeToggleButton:hover,
QPushButton#themeToggleButton:checked {
    border: 1px solid #d4af37;
    color: #ffffff;
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #c9a961, stop:0.3 #b89850, stop:0.7 #a88840, stop:1 #9a7a35);
    color: #1a1a1a;
    border: none;
    border-radius: 12px;
    padding: 14px 28px;
    font-weight: 600;
    font-size: 11pt;
    text-shadow: 0px 1px 2px rgba(255, 255, 255, 0.15);
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #d9b971, stop:0.3 #c9a961, stop:0.7 #b89850, stop:1 #a88840);
    text-shadow: 0px 1px 3px rgba(255, 255, 255, 0.25);
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #9a7a35, stop:0.5 #8a6a30, stop:1 #7a5a25);
}

QPushButton:disabled {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2a2a2a, stop:1 #1a1a1a);
    color: #555555;
}

QPushButton#secondaryButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2a2a2a, stop:1 #1a1a1a);
    color: #e8e8e8;
    border: 1px solid #3a3a3a;
}

QPushButton#secondaryButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #3a3a3a, stop:1 #2a2a2a);
    border: 1px solid #b89850;
}

QPushButton#dangerButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #ff4444, stop:1 #cc0000);
    color: #ffffff;
}

QPushButton#dangerButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #ff6666, stop:1 #ff4444);
}

QLineEdit {
    background-color: #2a2a2a;
    border: 2px solid #4a4a4a;
    border-radius: 8px;
    padding: 10px 12px;
    min-height: 20px;
    color: #ffffff;
    font-size: 11pt;
    selection-background-color: #d4af37;
    selection-color: #000000;
}

QTextEdit, QPlainTextEdit {
    background-color: #2a2a2a;
    border: 2px solid #4a4a4a;
    border-radius: 8px;
    padding: 10px 12px;
    color: #ffffff;
    font-size: 10pt;
    selection-background-color: #d4af37;
    selection-color: #000000;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 2px solid #d4af37;
    background-color: #303030;
    color: #ffffff;
}

QLineEdit::placeholder, QTextEdit::placeholder, QPlainTextEdit::placeholder {
    color: #888888;
}

QComboBox {
    background-color: #2a2a2a;
    border: 2px solid #4a4a4a;
    border-radius: 8px;
    padding: 10px 12px;
    min-height: 20px;
    color: #ffffff;
    font-size: 11pt;
}

QComboBox:hover {
    border: 2px solid #d4af37;
    background-color: #303030;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
    border-radius: 10px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #b89850;
    margin-right: 10px;
}

QComboBox QAbstractItemView {
    background-color: #2a2a2a;
    border: 2px solid #d4af37;
    border-radius: 8px;
    selection-background-color: #d4af37;
    selection-color: #000000;
    color: #ffffff;
    padding: 5px;
    font-size: 10pt;
}

QListWidget, QTreeWidget, QTableWidget {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1a1a1a, stop:1 #0f0f0f);
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    color: #f5f5f5;
    alternate-background-color: #151515;
}

QListWidget::item, QTreeWidget::item, QTableWidget::item {
    padding: 12px;
    border-radius: 8px;
    margin: 2px;
}

QListWidget::item:selected, QTreeWidget::item:selected, QTableWidget::item:selected {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #8a6a30, stop:0.3 #a88840, stop:0.7 #b89850, stop:1 #8a6a30);
    color: #1a1a1a;
    font-weight: 600;
}

QListWidget::item:hover, QTreeWidget::item:hover, QTableWidget::item:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2a2a2a, stop:1 #1a1a1a);
    border: 1px solid #b89850;
}

QScrollBar:vertical {
    background: #0a0a0a;
    width: 10px;
    border-radius: 5px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #3a3a3a, stop:1 #2a2a2a);
    border-radius: 5px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #a88840, stop:0.5 #b89850, stop:1 #a88840);
}

QScrollBar:horizontal {
    background: #0a0a0a;
    height: 10px;
    border-radius: 5px;
    margin: 2px;
}

QScrollBar::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #3a3a3a, stop:1 #2a2a2a);
    border-radius: 5px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #a88840, stop:0.5 #b89850, stop:1 #a88840);
}

QScrollBar::add-line, QScrollBar::sub-line {
    border: none;
    background: none;
}

QLabel {
    color: #f5f5f5;
    background: transparent;
}

QLabel#titleLabel {
    font-size: 28pt;
    font-weight: 700;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #9a7a35, stop:0.3 #b89850, stop:0.5 #d9b971, stop:0.7 #b89850, stop:1 #9a7a35);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    color: #c9a961;
}

QLabel#subtitleLabel {
    font-size: 12pt;
    color: #b8b8b8;
    font-weight: 400;
    padding: 8px 15px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 rgba(42, 42, 42, 0.5), stop:1 rgba(26, 26, 26, 0.5));
    border-radius: 8px;
    margin-bottom: 10px;
}

QLabel#sectionLabel {
    font-size: 13pt;
    font-weight: 600;
    color: #c9a961;
    margin-top: 12px;
    margin-bottom: 8px;
}

QGroupBox {
    background-color: #1f1f1f;
    border: 2px solid #4a4a4a;
    border-radius: 10px;
    margin-top: 12px;
    padding-top: 35px;
    padding-bottom: 15px;
    padding-left: 15px;
    padding-right: 15px;
    font-weight: 600;
    font-size: 11pt;
    color: #d4af37;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 6px 12px;
    left: 10px;
    top: 2px;
    color: #d4af37;
    background-color: #2a2a2a;
    border: 2px solid #d4af37;
    border-radius: 6px;
    font-weight: 700;
    font-size: 10pt;
}

QTabWidget::pane {
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1a1a1a, stop:1 #0f0f0f);
    margin-top: -1px;
}

QTabBar::tab {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2a2a2a, stop:1 #1a1a1a);
    color: #b8b8b8;
    padding: 12px 24px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    margin-right: 4px;
    border: 1px solid #2a2a2a;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #c9a961, stop:0.5 #b89850, stop:1 #a88840);
    color: #1a1a1a;
    font-weight: 600;
    border-bottom: none;
}

QTabBar::tab:hover:!selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #3a3a3a, stop:1 #2a2a2a);
    border: 1px solid #b89850;
}

QProgressBar {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1a1a1a, stop:1 #0f0f0f);
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    text-align: center;
    color: #f5f5f5;
    height: 28px;
    font-weight: 600;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #8a6a30, stop:0.2 #a88840, stop:0.4 #b89850, stop:0.6 #c9a961, stop:0.8 #b89850, stop:1 #8a6a30);
    border-radius: 10px;
}

QCheckBox {
    spacing: 12px;
    color: #f5f5f5;
    font-size: 10pt;
    padding: 5px;
}

QCheckBox::indicator {
    width: 24px;
    height: 24px;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    background-color: #1a1a1a;
}

QCheckBox::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #d4af37, stop:0.5 #c9a961, stop:1 #b89850);
    border: 2px solid #d4af37;
    image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEzLjMzMzMgNEw2IDExLjMzMzNMMi42NjY2NyA4IiBzdHJva2U9IiMxYTFhMWEiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+Cjwvc3ZnPgo=);
}

QCheckBox::indicator:hover {
    border: 2px solid #d4af37;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2a2a2a, stop:1 #1f1f1f);
}

QRadioButton {
    spacing: 10px;
    color: #f5f5f5;
}

QRadioButton::indicator {
    width: 22px;
    height: 22px;
    border: 1px solid #2a2a2a;
    border-radius: 11px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #1a1a1a, stop:1 #0f0f0f);
}

QRadioButton::indicator:checked {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #c9a961, stop:0.5 #b89850, stop:1 #a88840);
    border: 1px solid #b89850;
}

QRadioButton::indicator:hover {
    border: 2px solid #b89850;
}

QToolTip {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2a2a2a, stop:1 #1a1a1a);
    color: #f5f5f5;
    border: 1px solid #b89850;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 10pt;
}

QMessageBox {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #0a0a0a, stop:1 #1a1a1a);
}

QMessageBox QLabel {
    color: #f5f5f5;
}

QMessageBox QPushButton {
    min-width: 100px;
}
"""

LIGHT_THEME = """
QMainWindow {
    background-color: #eff1f5;
}

QWidget {
    background-color: #eff1f5;
    color: #4c4f69;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 10pt;
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

QPushButton#themeToggleButton {
    background: transparent;
    color: #4c4f69;
    border: 1px solid rgba(76, 79, 105, 0.35);
    border-radius: 18px;
    padding: 6px 18px;
    font-weight: 600;
}

QPushButton#themeToggleButton:hover,
QPushButton#themeToggleButton:checked {
    border: 1px solid #1e66f5;
    color: #1e66f5;
}

QPushButton {
    background-color: #1e66f5;
    color: #eff1f5;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: bold;
    font-size: 11pt;
}

QPushButton:hover {
    background-color: #7287fd;
}

QPushButton:pressed {
    background-color: #04a5e5;
}

QPushButton:disabled {
    background-color: #ccd0da;
    color: #9ca0b0;
}

QPushButton#secondaryButton {
    background-color: #ccd0da;
    color: #4c4f69;
}

QPushButton#secondaryButton:hover {
    background-color: #bcc0cc;
}

QPushButton#dangerButton {
    background-color: #d20f39;
    color: #eff1f5;
}

QPushButton#dangerButton:hover {
    background-color: #e64553;
}

QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #e6e9ef;
    border: 2px solid #ccd0da;
    border-radius: 6px;
    padding: 8px;
    color: #4c4f69;
    selection-background-color: #1e66f5;
    selection-color: #eff1f5;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 2px solid #1e66f5;
}

QComboBox {
    background-color: #e6e9ef;
    border: 2px solid #ccd0da;
    border-radius: 6px;
    padding: 8px;
    color: #4c4f69;
}

QComboBox:hover {
    border: 2px solid #1e66f5;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #4c4f69;
    margin-right: 10px;
}

QComboBox QAbstractItemView {
    background-color: #e6e9ef;
    border: 2px solid #ccd0da;
    selection-background-color: #1e66f5;
    selection-color: #eff1f5;
    color: #4c4f69;
}

QListWidget, QTreeWidget, QTableWidget {
    background-color: #e6e9ef;
    border: 2px solid #ccd0da;
    border-radius: 6px;
    color: #4c4f69;
}

QListWidget::item, QTreeWidget::item, QTableWidget::item {
    padding: 8px;
    border-radius: 4px;
}

QListWidget::item:selected, QTreeWidget::item:selected, QTableWidget::item:selected {
    background-color: #1e66f5;
    color: #eff1f5;
}

QListWidget::item:hover, QTreeWidget::item:hover, QTableWidget::item:hover {
    background-color: #ccd0da;
}

QScrollBar:vertical {
    background-color: #e6e9ef;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #bcc0cc;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #acb0be;
}

QScrollBar:horizontal {
    background-color: #e6e9ef;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #bcc0cc;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #acb0be;
}

QScrollBar::add-line, QScrollBar::sub-line {
    border: none;
    background: none;
}

QLabel {
    color: #4c4f69;
    background: transparent;
}

QLabel#titleLabel {
    font-size: 24pt;
    font-weight: bold;
    color: #1e66f5;
}

QLabel#subtitleLabel {
    font-size: 14pt;
    color: #5c5f77;
}

QLabel#sectionLabel {
    font-size: 12pt;
    font-weight: bold;
    color: #1e66f5;
    margin-top: 10px;
}

QGroupBox {
    background-color: #e6e9ef;
    border: 2px solid #ccd0da;
    border-radius: 8px;
    margin-top: 10px;
    padding-top: 20px;
    font-weight: bold;
    color: #1e66f5;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 5px 10px;
    color: #1e66f5;
}

QTabWidget::pane {
    border: 2px solid #ccd0da;
    border-radius: 8px;
    background-color: #e6e9ef;
}

QTabBar::tab {
    background-color: #ccd0da;
    color: #4c4f69;
    padding: 10px 20px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background-color: #1e66f5;
    color: #eff1f5;
}

QTabBar::tab:hover:!selected {
    background-color: #bcc0cc;
}

QProgressBar {
    background-color: #e6e9ef;
    border: 2px solid #ccd0da;
    border-radius: 6px;
    text-align: center;
    color: #4c4f69;
    height: 25px;
}

QProgressBar::chunk {
    background-color: #1e66f5;
    border-radius: 4px;
}

QCheckBox {
    spacing: 8px;
    color: #4c4f69;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #ccd0da;
    border-radius: 4px;
    background-color: #e6e9ef;
}

QCheckBox::indicator:checked {
    background-color: #1e66f5;
    border: 2px solid #1e66f5;
}

QCheckBox::indicator:hover {
    border: 2px solid #1e66f5;
}

QRadioButton {
    spacing: 8px;
    color: #4c4f69;
}

QRadioButton::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #ccd0da;
    border-radius: 10px;
    background-color: #e6e9ef;
}

QRadioButton::indicator:checked {
    background-color: #1e66f5;
    border: 2px solid #1e66f5;
}

QRadioButton::indicator:hover {
    border: 2px solid #1e66f5;
}

QToolTip {
    background-color: #e6e9ef;
    color: #4c4f69;
    border: 2px solid #ccd0da;
    border-radius: 4px;
    padding: 5px;
}

QMessageBox {
    background-color: #eff1f5;
}

QMessageBox QLabel {
    color: #4c4f69;
}

QMessageBox QPushButton {
    min-width: 80px;
}
"""


def get_theme(theme_name: str = "dark") -> str:
    """Get theme stylesheet"""
    return DARK_THEME if theme_name == "dark" else LIGHT_THEME
