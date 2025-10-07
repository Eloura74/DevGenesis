# DevGenesis 🚀

**Générateur universel de projets et environnements de développement**

DevGenesis est une application Python futuriste et ergonomique qui permet à tout développeur de gagner un temps considérable en générant, en quelques clics, des environnements de développement complets et opérationnels.

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Python](https://img.shields.io/badge/python-3.12+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Fonctionnalités principales

### 🎯 Génération automatique de projets
- **Zéro configuration manuelle** - Tout est automatisé
- **Templates prédéfinis** pour les technologies les plus populaires
- **Installation automatique** des dépendances
- **Structure de projet** conforme aux meilleures pratiques

### 🎨 Interface moderne et intuitive
- **Design futuriste** avec thème clair/sombre
- **Navigation par onglets** claire et organisée
- **Feedback visuel** en temps réel
- **Logs de génération** détaillés

### 📦 Templates intégrés

1. **React + Tailwind + Vite** - Application frontend moderne
2. **FastAPI + Docker** - API REST avec PostgreSQL
3. **Flask + Bootstrap** - Application web full-stack
4. **Python CLI + Rich** - Outil en ligne de commande
5. **Next.js + Tailwind** - Application React avec SSR
6. **Django + PostgreSQL** - Framework web complet

### 🔧 Automatisation complète

- ✅ Création de l'arborescence du projet
- ✅ Génération des fichiers de configuration
- ✅ Initialisation Git avec commit initial
- ✅ Création d'environnement virtuel Python
- ✅ Installation des dépendances (npm, pip, etc.)
- ✅ Configuration Docker si nécessaire

## 📋 Prérequis

- **Python 3.12+**
- **Git** (optionnel, pour l'initialisation des dépôts)
- **Node.js** (optionnel, pour les projets JavaScript)
- **Docker** (optionnel, pour les projets conteneurisés)

## 🚀 Installation

### Méthode 1: Installation avec pip

```bash
# Cloner le dépôt
git clone https://github.com/votre-repo/devgenesis.git
cd devgenesis

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Méthode 2: Installation avec Poetry

```bash
# Cloner le dépôt
git clone https://github.com/votre-repo/devgenesis.git
cd devgenesis

# Installer avec Poetry
poetry install

# Activer l'environnement
poetry shell
```

## 🎮 Utilisation

### Lancement de l'application

```bash
# Avec Python
python run.py

# Ou directement
python -m devgenesis.main
```

### Workflow de génération

1. **Sélectionner le type de projet** dans la liste (Web Frontend, API Backend, etc.)
2. **Choisir un template** parmi les options disponibles
3. **Configurer le projet**:
   - Nom du projet
   - Description (optionnelle)
   - Emplacement sur le disque
4. **Sélectionner les options**:
   - Initialisation Git
   - Création d'environnement virtuel
   - Installation automatique des dépendances
5. **Cliquer sur "Générer le Projet"**
6. **Attendre la génération** (logs en temps réel)
7. **Ouvrir le projet** dans votre IDE favori

## 📁 Structure du projet généré

Exemple pour un projet React + Tailwind + Vite:

```
mon-projet/
├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── utils/
│   ├── assets/
│   ├── styles/
│   ├── App.tsx
│   └── main.tsx
├── public/
├── node_modules/
├── .git/
├── .gitignore
├── package.json
├── vite.config.ts
├── tailwind.config.js
├── tsconfig.json
├── index.html
└── README.md
```

## 🎨 Personnalisation

### Créer un template personnalisé

Les templates sont stockés dans la base de données SQLite. Vous pouvez:

1. Utiliser l'interface pour gérer les templates
2. Créer des templates personnalisés via l'onglet "Templates"
3. Importer/exporter des templates au format JSON

### Structure d'un template

```json
{
  "name": "Mon Template",
  "description": "Description du template",
  "project_type": "web_frontend",
  "technologies": [
    {"name": "React", "version": "^18.2.0"}
  ],
  "structure": ["src", "public", "tests"],
  "files": [
    {
      "path": "package.json",
      "content": "...",
      "is_template": true
    }
  ],
  "commands": ["npm install"]
}
```

## 🔧 Configuration

### Fichier de configuration utilisateur

Le fichier `user_config.json` permet de personnaliser:

- Thème par défaut (clair/sombre)
- Emplacement par défaut des projets
- Options de génération par défaut

### Variables d'environnement

Aucune variable d'environnement n'est requise pour le fonctionnement de base.

## 📊 Statistiques

L'onglet "Paramètres" affiche:

- Nombre de templates disponibles
- Nombre de projets générés
- Taux de succès
- Historique des générations

## 🐛 Dépannage

### Erreur: "Git n'est pas installé"

Installez Git depuis [git-scm.com](https://git-scm.com/) ou désactivez l'option "Initialiser Git".

### Erreur: "npm n'est pas trouvé"

Installez Node.js depuis [nodejs.org](https://nodejs.org/) pour les projets JavaScript.

### Erreur: "Permission denied"

Vérifiez que vous avez les droits d'écriture dans le répertoire de destination.

### Les dépendances ne s'installent pas

Vérifiez votre connexion internet et les logs de génération pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues! Pour contribuer:

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Roadmap

- [ ] Support de plus de templates (Vue, Svelte, Go, Rust)
- [ ] Import/export de templates personnalisés
- [ ] Intégration avec GitHub/GitLab pour clonage de templates
- [ ] Support des monorepos
- [ ] CLI pour génération en ligne de commande
- [ ] Plugin VSCode/Windsurf
- [ ] Templates de microservices
- [ ] Support Kubernetes

## 🏆 Valeur ajoutée

- **Gain de temps**: Réduction de 80-90% du temps de setup
- **Simplicité**: Aucune connaissance des commandes requise
- **Universalité**: Compatible Windows, Linux, macOS
- **Standardisation**: Conformité aux bonnes pratiques
- **Évolutivité**: Ajout facile de nouveaux templates

## 📄 License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteurs

- **DevGenesis Team** - *Travail initial*

## 🙏 Remerciements

- Communauté Python
- Équipes PySide6, FastAPI, React
- Tous les contributeurs open-source

## 📞 Support

Pour toute question ou problème:

- Ouvrez une issue sur GitHub
- Consultez la documentation
- Contactez l'équipe de développement

---

**DevGenesis** - *Générez vos projets en quelques clics* 🚀
