@echo off
echo ========================================
echo Nettoyage du projet DevGenesis
echo ========================================
echo.

echo Suppression des fichiers de documentation redondants...
del /F /Q "AMELIORATIONS_v1.1.md" 2>nul
del /F /Q "ARCHITECTURE.md" 2>nul
del /F /Q "CHANGELOG.md" 2>nul
del /F /Q "COMPARAISON_VISUELLE.md" 2>nul
del /F /Q "CONTRIBUTING.md" 2>nul
del /F /Q "EXAMPLES.md" 2>nul
del /F /Q "GUIDE_UTILISATION.md" 2>nul
del /F /Q "INDEX_DOCUMENTATION.md" 2>nul
del /F /Q "INSTALLATION_COMPLETE.md" 2>nul
del /F /Q "LANCEMENT.md" 2>nul
del /F /Q "NOUVELLES_FONCTIONNALITES.md" 2>nul
del /F /Q "PROJECT_SUMMARY.md" 2>nul
del /F /Q "PROJET_TERMINE.md" 2>nul
del /F /Q "QUICKSTART.md" 2>nul
del /F /Q "RESUME_FINAL.md" 2>nul
del /F /Q "START_HERE.md" 2>nul
del /F /Q "STRUCTURE.md" 2>nul
del /F /Q "SYNTHESE_COMPLETE.md" 2>nul
del /F /Q "TEST_RAPIDE.md" 2>nul
del /F /Q "test_installation.py" 2>nul

echo.
echo Suppression du fichier de code inutilise...
del /F /Q "devgenesis\ui\main_window_refactored.py" 2>nul

echo.
echo ========================================
echo Nettoyage termine!
echo ========================================
echo.
echo Fichiers conserves:
echo - README.md (documentation principale)
echo - LICENSE (licence)
echo - requirements.txt (dependances)
echo - pyproject.toml (configuration)
echo - devgenesis/ (code source)
echo - run.py (lanceur)
echo - start.bat / start.sh (scripts de lancement)
echo - install.bat / install.sh (scripts d'installation)
echo.
pause
