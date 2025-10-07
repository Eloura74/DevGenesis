#!/bin/bash

echo "========================================"
echo "  DevGenesis - Installation"
echo "========================================"
echo ""

echo "[1/3] Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERREUR: Python 3 n'est pas installé"
    echo "Installez Python depuis https://python.org"
    exit 1
fi

python3 --version

echo ""
echo "[2/3] Création de l'environnement virtuel..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERREUR: Impossible de créer l'environnement virtuel"
    exit 1
fi

echo ""
echo "[3/3] Installation des dépendances..."
source venv/bin/activate
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERREUR: Impossible d'installer les dépendances"
    exit 1
fi

echo ""
echo "========================================"
echo "  Installation terminée avec succès!"
echo "========================================"
echo ""
echo "Pour lancer DevGenesis:"
echo "  1. Activez l'environnement: source venv/bin/activate"
echo "  2. Lancez l'application: python run.py"
echo ""
echo "Ou utilisez directement: ./start.sh"
echo ""
