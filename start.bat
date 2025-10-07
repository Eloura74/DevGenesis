@echo off
setlocal EnableExtensions

rem ---- anti-BOM + chemin projet ----
set "ROOT=%~dp0"
pushd "%ROOT%"

echo ========================================
echo   DevGenesis - Demarrage
echo ========================================

rem ---- venv requis ----
if not exist ".venv\Scripts\python.exe" (
  echo ERREUR: Environnement virtuel non trouve. Lancez d'abord install.bat
  pause
  popd
  exit /b 1
)

set "PY=.venv\Scripts\python.exe"

rem ---- detection entrypoint ----
set "ENTRY=run.py"
if exist "main.py" set "ENTRY=main.py"
if exist "src\app.py"  set "ENTRY=src\app.py"
if exist "src\main.py" set "ENTRY=src\main.py"

rem ---- module package (si present) ----
if exist "devgenesis\__main__.py" (
  "%PY%" -m devgenesis || (echo ERREUR: execution module echouee & popd & exit /b 1)
  popd
  exit /b 0
)

rem ---- script direct ----
if not exist "%ENTRY%" (
  echo ERREUR: Entry introuvable.
  echo Placez votre point d'entree dans ^"run.py^", ^"main.py^" ou ^"src\app.py^"/^"src\main.py^",
  echo ou fournissez le package ^"devgenesis^" avec __main__.py.
  pause
  popd
  exit /b 1
)

"%PY%" "%ENTRY%" || (echo ERREUR: execution echouee & popd & exit /b 1)

popd
exit /b 0
