#!/bin/bash

echo "========================================"
echo "  DevGenesis - Démarrage"
echo "========================================"
echo ""

if [ ! -d "venv" ]; then
    echo "ERREUR: Environnement virtuel non trouvé"
    echo "Exécutez d'abord ./install.sh"
    exit 1
fi

echo "Activation de l'environnement virtuel..."
source venv/bin/activate

echo "Lancement de DevGenesis..."
python run.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERREUR: Impossible de lancer l'application"
    exit 1
fi
