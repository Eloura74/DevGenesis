@echo off
setlocal enabledelayedexpansion
echo ========================================
echo   DevGenesis - Installation
echo ========================================

REM 1) Detecter Python (py -> python)
where py >nul 2>&1 && (set "PY=py" & goto havepy)
where python >nul 2>&1 && (for /f "delims=" %%P in ('where python') do set "PY=%%P" & goto havepy)
echo ERREUR: Python introuvable. Installe Python 3.13 64-bit.
exit /b 1
:havepy
echo Python detecte: %PY%
"%PY%" --version || (echo ERREUR d'execution de Python & exit /b 1)

REM 2) Creer venv .venv (idempotent)
if not exist ".venv\Scripts\python.exe" (
  echo [1/4] Creation de l'environnement virtuel .venv ...
  "%PY%" -m venv .venv || (echo ERREUR venv & exit /b 1)
)

REM 3) Mettre pip a jour dans le venv
echo [2/4] Upgrade pip ...
".venv\Scripts\python.exe" -m ensurepip --upgrade
".venv\Scripts\python.exe" -m pip install --upgrade pip

REM 4) Installer les dependances projet
echo [3/4] Installation requirements ...
if exist requirements.txt (
  ".venv\Scripts\python.exe" -m pip install -r requirements.txt || (echo ERREUR install deps & exit /b 1)
) else (
  echo Avertissement: requirements.txt introuvable. Suite.
)

REM 5) Marqueur OK
echo ok > ".venv\DEVGENESIS_OK"
echo [4/4] Terminé.
exit /b 0
