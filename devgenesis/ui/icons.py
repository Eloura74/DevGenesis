"""SVG Icons for DevGenesis UI - Gold Tech Modern Theme

Note: If QtSvg is not available, falls back to using standard Qt icons.
To enable SVG icons, install: pip install PySide6-Addons
"""

from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QPen, QBrush
from PySide6.QtCore import QByteArray, QSize, Qt, QRectF

try:
    from PySide6.QtSvg import QSvgRenderer
    SVG_AVAILABLE = True
except ImportError:
    SVG_AVAILABLE = False
    print("Warning: QtSvg not available. Using fallback icons. Install with: pip install PySide6-Addons")


class IconProvider:
    """Provides SVG icons with dynamic coloring"""
    
    # SVG Icons as strings
    ICONS = {
        "new_project": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13 7H7v6h6V7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M17 7v6M17 17v-4M7 17h6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/>
            </svg>
        """,
        "templates": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="3" width="7" height="7" rx="1" stroke="currentColor" stroke-width="2"/>
                <rect x="14" y="3" width="7" height="7" rx="1" stroke="currentColor" stroke-width="2"/>
                <rect x="3" y="14" width="7" height="7" rx="1" stroke="currentColor" stroke-width="2"/>
                <rect x="14" y="14" width="7" height="7" rx="1" stroke="currentColor" stroke-width="2"/>
            </svg>
        """,
        "create_template": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M14 2v6h6M12 18v-6M9 15h6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        """,
        "history": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/>
                <path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
        """,
        "settings": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/>
                <path d="M12 1v3m0 16v3M4.22 4.22l2.12 2.12m11.32 11.32l2.12 2.12M1 12h3m16 0h3M4.22 19.78l2.12-2.12m11.32-11.32l2.12-2.12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
        """,
        "web": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/>
                <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" stroke="currentColor" stroke-width="2"/>
            </svg>
        """,
        "api": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/>
                <path d="M9 9l-3 3 3 3M15 9l3 3-3 3M13 7l-2 10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        """,
        "ai": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7l10 5 10-5-10-5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 17l10 5 10-5M2 12l10 5 10-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        """,
        "mobile": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="5" y="2" width="14" height="20" rx="2" stroke="currentColor" stroke-width="2"/>
                <path d="M12 18h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
        """,
        "desktop": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="2" y="3" width="20" height="14" rx="2" stroke="currentColor" stroke-width="2"/>
                <path d="M8 21h8M12 17v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
        """,
        "tool": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        """,
        "chip": """
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="4" y="4" width="16" height="16" rx="2" stroke="currentColor" stroke-width="2"/>
                <rect x="9" y="9" width="6" height="6" stroke="currentColor" stroke-width="2"/>
                <path d="M9 2v2M15 2v2M9 20v2M15 20v2M2 9h2M2 15h2M20 9h2M20 15h2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
        """,
    }
    
    @staticmethod
    def _create_fallback_icon(name: str, color: str, size: int) -> QIcon:
        """Create a simple fallback icon using QPainter"""
        pixmap = QPixmap(size, size)
        pixmap.fill(QColor(0, 0, 0, 0))
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        pen = QPen(QColor(color))
        pen.setWidth(2)
        painter.setPen(pen)
        
        margin = size * 0.15
        rect = QRectF(margin, margin, size - 2*margin, size - 2*margin)
        
        # Simple geometric shapes based on icon name
        if name == "new_project":
            painter.drawRect(rect)
            painter.drawLine(int(size/2), int(margin), int(size/2), int(size-margin))
            painter.drawLine(int(margin), int(size/2), int(size-margin), int(size/2))
        elif name == "templates":
            half = size / 2
            painter.drawRect(QRectF(margin, margin, half-margin*1.5, half-margin*1.5))
            painter.drawRect(QRectF(half+margin*0.5, margin, half-margin*1.5, half-margin*1.5))
            painter.drawRect(QRectF(margin, half+margin*0.5, half-margin*1.5, half-margin*1.5))
            painter.drawRect(QRectF(half+margin*0.5, half+margin*0.5, half-margin*1.5, half-margin*1.5))
        elif name == "settings":
            painter.drawEllipse(rect)
            painter.drawEllipse(QRectF(size*0.35, size*0.35, size*0.3, size*0.3))
        elif name == "history":
            painter.drawEllipse(rect)
            painter.drawLine(int(size/2), int(size/2), int(size/2), int(margin))
            painter.drawLine(int(size/2), int(size/2), int(size-margin), int(size/2))
        else:
            # Default: simple circle
            painter.drawEllipse(rect)
        
        painter.end()
        return QIcon(pixmap)
    
    @staticmethod
    def get_icon(name: str, color: str = "#9ca3af", size: int = 24) -> QIcon:
        """
        Get an icon with specified color
        
        Args:
            name: Icon name from ICONS dict
            color: Hex color string (e.g., "#f2c94c")
            size: Icon size in pixels
        """
        if name not in IconProvider.ICONS:
            return QIcon()
        
        if not SVG_AVAILABLE:
            # Fallback to simple drawn icons
            return IconProvider._create_fallback_icon(name, color, size)
        
        try:
            svg_data = IconProvider.ICONS[name].replace("currentColor", color)
            
            # Create QPixmap from SVG
            byte_array = QByteArray(svg_data.encode('utf-8'))
            renderer = QSvgRenderer(byte_array)
            
            if not renderer.isValid():
                return IconProvider._create_fallback_icon(name, color, size)
            
            pixmap = QPixmap(size, size)
            pixmap.fill(QColor(0, 0, 0, 0))  # Transparent background
            
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            renderer.render(painter)
            painter.end()
            
            return QIcon(pixmap)
        except Exception as e:
            print(f"Error creating icon '{name}': {e}")
            return IconProvider._create_fallback_icon(name, color, size)
    
    @staticmethod
    def get_colored_icons(name: str, size: int = 24) -> dict:
        """
        Get icon in multiple states (normal, hover, selected)
        
        Returns:
            dict with 'normal', 'hover', 'selected' QIcon instances
        """
        return {
            "normal": IconProvider.get_icon(name, "#9ca3af", size),
            "hover": IconProvider.get_icon(name, "#ffdf7e", size),
            "selected": IconProvider.get_icon(name, "#f2c94c", size),
        }
