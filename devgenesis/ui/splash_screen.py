"""Splash screen with video for DevGenesis application"""

import os
from pathlib import Path
from PySide6.QtCore import Qt, QUrl, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget


class VideoOverlay(QWidget):
    """Vidéo plein écran au-dessus de la fenêtre principale.
    Se ferme automatiquement dès la fin réelle de la vidéo.
    """

    finished = Signal()

    def __init__(self, parent, video_path: str):
        super().__init__(parent)

        self.video_path = video_path

        # Fenêtre sans bord, par-dessus le parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setWindowOpacity(1.0)

        # Zone d'affichage vidéo
        self.video_widget = QVideoWidget(self)

        # Lecteur + audio
        self.media_player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.audio_output.setVolume(0.9)  # 0.0 -> 1.0
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_widget)

        # Source vidéo
        video_url = QUrl.fromLocalFile(str(Path(video_path).resolve()))
        self.media_player.setSource(video_url)

        # Signaux
        self.media_player.mediaStatusChanged.connect(self._on_media_status_changed)
        self.media_player.errorOccurred.connect(self._on_error)

        # Animation de fondu (fermeture)
        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(500)  # 500 ms
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)
        self.fade_animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.fade_animation.finished.connect(self._on_fade_finished)

    # Redimensionnement: la vidéo occupe tout l'overlay
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.video_widget.setGeometry(self.rect())

    # Au chargement/lecture/fin du média
    def _on_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            # Lance la lecture dès que c'est prêt
            self.media_player.play()
        elif status == QMediaPlayer.MediaStatus.EndOfMedia:
            # Ferme dès la fin réelle de la vidéo
            self._fade_out()
        elif status in (
            QMediaPlayer.MediaStatus.InvalidMedia,
            QMediaPlayer.MediaStatus.NoMedia,
        ):
            # Si média invalide ou absent: fermer proprement
            self._fade_out()

    def _on_error(self, error, error_string):
        # En cas d'erreur, fermer immédiatement
        print(f"[VideoOverlay] Media error: {error_string}")
        self._fade_out()

    def _fade_out(self):
        # Démarre le fondu de sortie
        if self.fade_animation.state() != QPropertyAnimation.Running:
            self.fade_animation.start()

    def _on_fade_finished(self):
        # Stoppe le lecteur puis notifie et détruit l'overlay
        try:
            self.media_player.stop()
        except Exception:
            pass
        self.finished.emit()
        self.deleteLater()

    # Interaction utilisateur: permet de passer la vidéo
    def mousePressEvent(self, event):
        self._fade_out()

    def keyPressEvent(self, event):
        self._fade_out()

    def showEvent(self, event):
        super().showEvent(event)
        self.video_widget.show()


def get_default_video_path() -> str:
    """Chemin par défaut de la vidéo générique."""
    base_dir = Path(__file__).parent.parent.parent
    return str(base_dir / "images" / "generic.mp4")


def video_exists(video_path: str | None = None) -> bool:
    """Vérifie l'existence du fichier vidéo."""
    if video_path is None:
        video_path = get_default_video_path()
    return os.path.exists(video_path)
