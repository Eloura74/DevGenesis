# Icônes SVG - DevGenesis

## Installation

Les icônes SVG nécessitent le module `QtSvg` de PySide6.

### Option 1: Installer PySide6-Addons (Recommandé)
```bash
pip install PySide6-Addons
```

### Option 2: Réinstaller PySide6 complet
```bash
pip install --upgrade --force-reinstall PySide6
```

## Fallback

Si QtSvg n'est pas disponible, l'application utilisera automatiquement des icônes de fallback dessinées avec QPainter. Ces icônes sont fonctionnelles mais moins détaillées que les SVG.

## Vérification

Pour vérifier si QtSvg est disponible :
```bash
python -c "from PySide6.QtSvg import QSvgRenderer; print('QtSvg OK')"
```

## Icônes disponibles

- `new_project` - Nouveau projet
- `templates` - Templates (grille 2x2)
- `create_template` - Créer template (document+)
- `history` - Historique (horloge)
- `settings` - Paramètres (engrenage)
- `web` - Application web (globe)
- `api` - API Backend (code)
- `ai` - AI/ML (couches)
- `mobile` - Application mobile (téléphone)
- `desktop` - Application desktop (écran)
- `tool` - CLI Tool (clé)
- `chip` - IoT/Embedded (puce)

## Utilisation

```python
from devgenesis.ui.icons import IconProvider

# Icône simple
icon = IconProvider.get_icon("new_project", "#f2c94c", 24)

# Icônes avec états multiples
icons = IconProvider.get_colored_icons("settings", 24)
# icons['normal'], icons['hover'], icons['selected']
```
