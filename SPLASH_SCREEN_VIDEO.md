# Configuration du Splash Screen Vidéo

## Description

Un splash screen vidéo a été ajouté au lancement de l'application DevGenesis. Il affiche la vidéo `A:\Programmation\CreationProjet\images\generic.mp4` pendant 5 secondes avant d'ouvrir la fenêtre principale.

## Fichiers modifiés/créés

### 1. `devgenesis/ui/splash_screen.py` (NOUVEAU)
- Composant `VideoSplashScreen` qui gère l'affichage de la vidéo
- Fonction `show_splash_screen()` pour faciliter l'utilisation
- Gestion automatique de la lecture vidéo et du timing
- Fermeture possible en cliquant ou en appuyant sur une touche

### 2. `devgenesis/main.py` (MODIFIÉ)
- Import du module `splash_screen`
- Affichage du splash screen avant la fenêtre principale
- Timer pour afficher la fenêtre principale après 5 secondes

## Dépendances

PySide6 inclut déjà les modules multimédias nécessaires :
- `PySide6.QtMultimedia` - Lecture audio/vidéo
- `PySide6.QtMultimediaWidgets` - Widget vidéo

**Note importante** : Si vous obtenez une erreur d'import, assurez-vous que PySide6 est installé avec tous ses modules :

```bash
pip install PySide6 --upgrade
```

## Configuration

### Changer la durée du splash screen

Dans `devgenesis/main.py`, ligne 25 :
```python
splash = show_splash_screen(duration_ms=5000)  # 5000 ms = 5 secondes
```

Modifiez la valeur `duration_ms` pour changer la durée (en millisecondes).

### Changer la vidéo

Dans `devgenesis/ui/splash_screen.py`, fonction `show_splash_screen()` :
```python
video_path = base_dir / "images" / "generic.mp4"  # Changez le nom du fichier ici
```

Ou passez directement le chemin lors de l'appel :
```python
splash = show_splash_screen(video_path="chemin/vers/video.mp4", duration_ms=5000)
```

### Désactiver le splash screen

Pour désactiver temporairement le splash screen, commentez les lignes dans `devgenesis/main.py` :

```python
# splash = show_splash_screen(duration_ms=5000)
# 
# # Create main window (but don't show it yet)
# window = MainWindow()
# 
# # Show main window after splash screen closes
# if splash:
#     def show_main_window():
#         splash.close()
#         window.show()
#     
#     QTimer.singleShot(5000, show_main_window)
# else:
#     window.show()

# Remplacer par :
window = MainWindow()
window.show()
```

## Fonctionnalités

- ✅ Lecture automatique de la vidéo au lancement
- ✅ Fermeture automatique après la durée spécifiée
- ✅ Fermeture manuelle en cliquant ou en appuyant sur une touche
- ✅ Fenêtre sans bordure (frameless) centrée à l'écran
- ✅ Gestion des erreurs (si la vidéo n'existe pas, l'application démarre normalement)
- ✅ Toujours au premier plan pendant l'affichage

## Format vidéo supporté

PySide6 supporte les formats suivants (selon les codecs installés sur le système) :
- MP4 (H.264, H.265)
- AVI
- MOV
- WMV
- WebM

**Recommandation** : Utilisez MP4 avec codec H.264 pour une meilleure compatibilité.

## Taille et résolution

Le splash screen est configuré pour une résolution de **800x600 pixels**. Pour changer cette taille, modifiez dans `devgenesis/ui/splash_screen.py` :

```python
super().__init__(QPixmap(800, 600), Qt.WindowStaysOnTopHint)  # Ligne 23
self.video_widget.setGeometry(0, 0, 800, 600)  # Ligne 34
```

## Troubleshooting

### La vidéo ne se lit pas
1. Vérifiez que le fichier existe : `A:\Programmation\CreationProjet\images\generic.mp4`
2. Vérifiez que les codecs vidéo sont installés sur votre système
3. Essayez avec une autre vidéo au format MP4/H.264

### L'application ne démarre pas
- Vérifiez les messages d'erreur dans la console
- Si le problème persiste, désactivez temporairement le splash screen (voir section "Désactiver le splash screen")

### La vidéo est déformée
- Ajustez la taille du splash screen pour correspondre au ratio de votre vidéo
- Ou modifiez votre vidéo pour qu'elle soit en 800x600 (ou 4:3)
