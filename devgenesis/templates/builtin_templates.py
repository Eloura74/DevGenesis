"""Built-in project templates for DevGenesis"""

from typing import Dict, List, Any
import json


def get_react_tailwind_vite_template() -> Dict[str, Any]:
    """React + Tailwind CSS + Vite template"""
    return {
        "name": "React + Tailwind + Vite",
        "description": "Application React moderne avec Tailwind CSS et Vite",
        "project_type": "web_frontend",
        "technologies": [
            {"name": "React", "version": "^18.2.0"},
            {"name": "Vite", "version": "^5.0.0"},
            {"name": "Tailwind CSS", "version": "^3.4.0"},
            {"name": "TypeScript", "version": "^5.3.0"},
        ],
        "structure": [
            "src",
            "src/components",
            "src/pages",
            "src/hooks",
            "src/utils",
            "src/assets",
            "src/styles",
            "public",
        ],
        "files": [
            {
                "path": "package.json",
                "content": json.dumps(
                    {
                        "name": "{{ project_name }}",
                        "private": True,
                        "version": "0.1.0",
                        "type": "module",
                        "scripts": {
                            "dev": "vite",
                            "build": "tsc && vite build",
                            "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
                            "preview": "vite preview",
                        },
                        "dependencies": {
                            "react": "^18.2.0",
                            "react-dom": "^18.2.0",
                        },
                        "devDependencies": {
                            "@types/react": "^18.2.43",
                            "@types/react-dom": "^18.2.17",
                            "@typescript-eslint/eslint-plugin": "^6.14.0",
                            "@typescript-eslint/parser": "^6.14.0",
                            "@vitejs/plugin-react": "^4.2.1",
                            "autoprefixer": "^10.4.16",
                            "eslint": "^8.55.0",
                            "eslint-plugin-react-hooks": "^4.6.0",
                            "eslint-plugin-react-refresh": "^0.4.5",
                            "postcss": "^8.4.32",
                            "tailwindcss": "^3.4.0",
                            "typescript": "^5.3.3",
                            "vite": "^5.0.8",
                        },
                    },
                    indent=2,
                ),
                "is_template": True,
            },
            {
                "path": "vite.config.ts",
                "content": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
  },
})
""",
                "is_template": False,
            },
            {
                "path": "tailwind.config.js",
                "content": """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
""",
                "is_template": False,
            },
            {
                "path": "postcss.config.js",
                "content": """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
                "is_template": False,
            },
            {
                "path": "tsconfig.json",
                "content": json.dumps(
                    {
                        "compilerOptions": {
                            "target": "ES2020",
                            "useDefineForClassFields": True,
                            "lib": ["ES2020", "DOM", "DOM.Iterable"],
                            "module": "ESNext",
                            "skipLibCheck": True,
                            "moduleResolution": "bundler",
                            "allowImportingTsExtensions": True,
                            "resolveJsonModule": True,
                            "isolatedModules": True,
                            "noEmit": True,
                            "jsx": "react-jsx",
                            "strict": True,
                            "noUnusedLocals": True,
                            "noUnusedParameters": True,
                            "noFallthroughCasesInSwitch": True,
                        },
                        "include": ["src"],
                        "references": [{"path": "./tsconfig.node.json"}],
                    },
                    indent=2,
                ),
                "is_template": False,
            },
            {
                "path": "tsconfig.node.json",
                "content": json.dumps(
                    {
                        "compilerOptions": {
                            "composite": True,
                            "skipLibCheck": True,
                            "module": "ESNext",
                            "moduleResolution": "bundler",
                            "allowSyntheticDefaultImports": True,
                        },
                        "include": ["vite.config.ts"],
                    },
                    indent=2,
                ),
                "is_template": False,
            },
            {
                "path": "index.html",
                "content": """<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{ project_name }}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
""",
                "is_template": True,
            },
            {
                "path": "src/main.tsx",
                "content": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './styles/index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""",
                "is_template": False,
            },
            {
                "path": "src/App.tsx",
                "content": """import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
      <div className="bg-white rounded-2xl shadow-2xl p-8 max-w-md w-full">
        <h1 className="text-4xl font-bold text-gray-800 mb-4 text-center">
          {{ project_name }}
        </h1>
        <p className="text-gray-600 mb-6 text-center">
          Projet généré avec DevGenesis
        </p>
        <div className="flex flex-col items-center gap-4">
          <button
            onClick={() => setCount((count) => count + 1)}
            className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 px-8 rounded-lg transition-colors duration-200 shadow-md hover:shadow-lg"
          >
            Count: {count}
          </button>
          <p className="text-sm text-gray-500">
            Éditez <code className="bg-gray-100 px-2 py-1 rounded">src/App.tsx</code> pour commencer
          </p>
        </div>
      </div>
    </div>
  )
}

export default App
""",
                "is_template": True,
            },
            {
                "path": "src/styles/index.css",
                "content": """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
""",
                "is_template": False,
            },
            {
                "path": ".eslintrc.cjs",
                "content": """module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parser: '@typescript-eslint/parser',
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': [
      'warn',
      { allowConstantExport: true },
    ],
  },
}
""",
                "is_template": False,
            },
            {
                "path": ".gitignore",
                "content": """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
""",
                "is_template": False,
            },
            {
                "path": "README.md",
                "content": """# {{ project_name }}

Projet React + Tailwind CSS + Vite généré avec DevGenesis.

## 🚀 Démarrage rapide

```bash
# Installation des dépendances
npm install

# Lancement du serveur de développement
npm run dev

# Build de production
npm run build

# Prévisualisation du build
npm run preview
```

## 📦 Technologies utilisées

- **React 18** - Bibliothèque UI
- **TypeScript** - Typage statique
- **Vite** - Build tool ultra-rapide
- **Tailwind CSS** - Framework CSS utility-first
- **ESLint** - Linter JavaScript/TypeScript

## 📁 Structure du projet

```
src/
├── components/     # Composants réutilisables
├── pages/         # Pages de l'application
├── hooks/         # Custom hooks React
├── utils/         # Fonctions utilitaires
├── assets/        # Images, fonts, etc.
├── styles/        # Fichiers CSS globaux
└── App.tsx        # Composant principal
```

## 🎨 Personnalisation

Modifiez `tailwind.config.js` pour personnaliser le thème Tailwind CSS.

## 📝 License

MIT
""",
                "is_template": True,
            },
        ],
        "commands": ["npm install"],
        "is_builtin": True,
    }


def get_fastapi_docker_template() -> Dict[str, Any]:
    """FastAPI + Docker template"""
    return {
        "name": "FastAPI + Docker",
        "description": "API REST avec FastAPI, PostgreSQL et Docker",
        "project_type": "api_backend",
        "technologies": [
            {"name": "FastAPI", "version": "^0.109.0"},
            {"name": "Python", "version": "^3.12"},
            {"name": "Docker"},
            {"name": "PostgreSQL"},
        ],
        "structure": [
            "app",
            "app/api",
            "app/api/endpoints",
            "app/core",
            "app/models",
            "app/schemas",
            "app/services",
            "tests",
            "tests/api",
        ],
        "files": [
            {
                "path": "requirements.txt",
                "content": """fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
pydantic==2.5.3
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
alembic==1.13.1
redis==5.0.1
httpx==0.26.0
pytest==7.4.4
pytest-asyncio==0.23.3
""",
                "is_template": False,
            },
            {
                "path": "Dockerfile",
                "content": """FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    postgresql-client \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
""",
                "is_template": False,
            },
            {
                "path": "docker-compose.yml",
                "content": """version: '3.8'

services:
  api:
    build: .
    container_name: {{ project_name }}_api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/{{ project_name }}
      - REDIS_URL=redis://redis:6379
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  db:
    image: postgres:16-alpine
    container_name: {{ project_name }}_db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB={{ project_name }}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    container_name: {{ project_name }}_redis
    ports:
      - "6379:6379"

volumes:
  postgres_data:
""",
                "is_template": True,
            },
            {
                "path": ".env.example",
                "content": """# Application
APP_NAME={{ project_name }}
APP_VERSION=1.0.0
DEBUG=True

# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/{{ project_name }}

# Redis
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]
""",
                "is_template": True,
            },
            {
                "path": "app/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "app/main.py",
                "content": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API générée avec DevGenesis",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["health"])


@app.get("/")
async def root():
    return {
        "message": "Bienvenue sur l'API {{ project_name }}",
        "version": settings.APP_VERSION,
        "docs": "/docs",
    }
""",
                "is_template": True,
            },
            {
                "path": "app/core/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "app/core/config.py",
                "content": """from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "{{ project_name }}"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    DATABASE_URL: str
    REDIS_URL: str
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    BACKEND_CORS_ORIGINS: List[str] = []

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
""",
                "is_template": True,
            },
            {
                "path": "app/api/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "app/api/endpoints/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "app/api/endpoints/health.py",
                "content": """from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "{{ project_name }}",
    }
""",
                "is_template": True,
            },
            {
                "path": ".gitignore",
                "content": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv/

# Environment
.env
.env.local

# Database
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp

# Docker
docker-compose.override.yml

# Logs
*.log
""",
                "is_template": False,
            },
            {
                "path": "README.md",
                "content": """# {{ project_name }}

API FastAPI avec PostgreSQL et Docker générée avec DevGenesis.

## 🚀 Démarrage rapide

### Avec Docker (recommandé)

```bash
# Copier le fichier d'environnement
cp .env.example .env

# Démarrer les services
docker-compose up -d

# L'API est accessible sur http://localhost:8000
# Documentation interactive: http://localhost:8000/docs
```

### Sans Docker

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos paramètres

# Lancer l'application
uvicorn app.main:app --reload
```

## 📦 Technologies utilisées

- **FastAPI** - Framework web moderne et rapide
- **PostgreSQL** - Base de données relationnelle
- **Redis** - Cache et file de messages
- **Docker** - Conteneurisation
- **SQLAlchemy** - ORM Python
- **Pydantic** - Validation des données

## 📁 Structure du projet

```
app/
├── api/
│   └── endpoints/     # Routes API
├── core/             # Configuration
├── models/           # Modèles SQLAlchemy
├── schemas/          # Schémas Pydantic
└── services/         # Logique métier
```

## 🧪 Tests

```bash
pytest
```

## 📝 License

MIT
""",
                "is_template": True,
            },
        ],
        "commands": ["pip install -r requirements.txt"],
        "is_builtin": True,
    }


def get_flask_bootstrap_template() -> Dict[str, Any]:
    """Flask + Bootstrap template"""
    return {
        "name": "Flask + Bootstrap",
        "description": "Application web Flask avec Bootstrap et SQLite",
        "project_type": "web_fullstack",
        "technologies": [
            {"name": "Flask", "version": "^3.0.0"},
            {"name": "Python", "version": "^3.12"},
            {"name": "Bootstrap", "version": "5.3"},
        ],
        "structure": [
            "app",
            "app/templates",
            "app/static",
            "app/static/css",
            "app/static/js",
            "app/routes",
            "app/models",
            "tests",
        ],
        "files": [
            {
                "path": "requirements.txt",
                "content": """Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-WTF==1.2.1
python-dotenv==1.0.0
email-validator==2.1.0
""",
                "is_template": False,
            },
            {
                "path": ".env.example",
                "content": """FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
""",
                "is_template": False,
            },
            {
                "path": "run.py",
                "content": """from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
""",
                "is_template": False,
            },
            {
                "path": "app/__init__.py",
                "content": """from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    from app.routes import main, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    
    with app.app_context():
        db.create_all()
    
    return app
""",
                "is_template": False,
            },
            {
                "path": "config.py",
                "content": """import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
""",
                "is_template": False,
            },
            {
                "path": "app/routes/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "app/routes/main.py",
                "content": """from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html', title='Accueil')


@bp.route('/about')
def about():
    return render_template('about.html', title='À propos')
""",
                "is_template": False,
            },
            {
                "path": "app/routes/auth.py",
                "content": """from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def login():
    return render_template('auth/login.html', title='Connexion')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'success')
    return redirect(url_for('main.index'))
""",
                "is_template": False,
            },
            {
                "path": "app/templates/base.html",
                "content": """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ title }} - {{ project_name }}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('main.index') }}">{{ project_name }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('main.index') }}">Accueil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('main.about') }}">À propos</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <footer class="bg-light text-center text-lg-start mt-5">
        <div class="text-center p-3">
            © 2025 {{ project_name }} - Généré avec DevGenesis
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
""",
                "is_template": True,
            },
            {
                "path": "app/templates/index.html",
                "content": """{% extends "base.html" %}

{% block content %}
<div class="row">
    <div class="col-lg-8 mx-auto">
        <div class="card shadow-sm">
            <div class="card-body text-center p-5">
                <h1 class="display-4 mb-4">Bienvenue sur {{ project_name }}</h1>
                <p class="lead text-muted mb-4">
                    Application Flask générée avec DevGenesis
                </p>
                <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                    <a href="{{ url_for('main.about') }}" class="btn btn-primary btn-lg">
                        En savoir plus
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""",
                "is_template": True,
            },
            {
                "path": "app/templates/about.html",
                "content": """{% extends "base.html" %}

{% block content %}
<div class="row">
    <div class="col-lg-8 mx-auto">
        <h1 class="mb-4">À propos</h1>
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ project_name }}</h5>
                <p class="card-text">
                    Cette application a été générée automatiquement avec DevGenesis,
                    un générateur universel de projets et environnements de développement.
                </p>
                <h6 class="mt-4">Technologies utilisées :</h6>
                <ul>
                    <li>Flask - Framework web Python</li>
                    <li>Bootstrap 5 - Framework CSS</li>
                    <li>SQLAlchemy - ORM Python</li>
                    <li>Flask-Login - Gestion d'authentification</li>
                </ul>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""",
                "is_template": True,
            },
            {
                "path": "app/static/css/style.css",
                "content": """/* Custom styles for {{ project_name }} */

body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

main {
    flex: 1;
}

.navbar-brand {
    font-weight: bold;
    font-size: 1.5rem;
}

footer {
    margin-top: auto;
}
""",
                "is_template": True,
            },
            {
                "path": ".gitignore",
                "content": """# Python
__pycache__/
*.py[cod]
venv/
.venv/

# Flask
instance/
.env
*.db

# IDE
.vscode/
.idea/
""",
                "is_template": False,
            },
            {
                "path": "README.md",
                "content": """# {{ project_name }}

Application Flask avec Bootstrap générée avec DevGenesis.

## 🚀 Démarrage rapide

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer l'environnement
cp .env.example .env

# Lancer l'application
python run.py
```

L'application sera accessible sur http://localhost:5000

## 📦 Technologies

- Flask 3.0
- Bootstrap 5.3
- SQLAlchemy
- Flask-Login

## 📝 License

MIT
""",
                "is_template": True,
            },
        ],
        "commands": ["pip install -r requirements.txt"],
        "is_builtin": True,
    }


def get_python_cli_template() -> Dict[str, Any]:
    """Python CLI tool template"""
    return {
        "name": "Python CLI + Rich",
        "description": "Outil en ligne de commande Python avec Rich",
        "project_type": "cli_tool",
        "technologies": [
            {"name": "Python", "version": "^3.12"},
            {"name": "Rich"},
            {"name": "Click"},
        ],
        "structure": [
            "src",
            "src/{{ project_name_snake }}",
            "src/{{ project_name_snake }}/commands",
            "src/{{ project_name_snake }}/utils",
            "tests",
        ],
        "files": [
            {
                "path": "requirements.txt",
                "content": """click==8.1.7
rich==13.7.0
pydantic==2.5.3
""",
                "is_template": False,
            },
            {
                "path": "setup.py",
                "content": """from setuptools import setup, find_packages

setup(
    name="{{ project_name_snake }}",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.1.7",
        "rich>=13.7.0",
        "pydantic>=2.5.3",
    ],
    entry_points={
        "console_scripts": [
            "{{ project_name_snake }}=src.{{ project_name_snake }}.cli:cli",
        ],
    },
    python_requires=">=3.12",
)
""",
                "is_template": True,
            },
            {
                "path": "src/{{ project_name_snake }}/__init__.py",
                "content": """\"\"\"{{ project_name }} - CLI tool\"\"\"

__version__ = "1.0.0"
""",
                "is_template": True,
            },
            {
                "path": "src/{{ project_name_snake }}/cli.py",
                "content": """import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    \"\"\"{{ project_name }} - Outil CLI généré avec DevGenesis\"\"\"
    pass


@cli.command()
@click.option("--name", default="World", help="Nom à saluer")
def hello(name):
    \"\"\"Commande de démonstration\"\"\"
    console.print(Panel(
        f"[bold green]Bonjour, {name}![/bold green]",
        title="{{ project_name }}",
        border_style="blue"
    ))


@cli.command()
def info():
    \"\"\"Affiche les informations du projet\"\"\"
    table = Table(title="Informations du projet")
    table.add_column("Propriété", style="cyan")
    table.add_column("Valeur", style="green")
    
    table.add_row("Nom", "{{ project_name }}")
    table.add_row("Version", "1.0.0")
    table.add_row("Générateur", "DevGenesis")
    
    console.print(table)


if __name__ == "__main__":
    cli()
""",
                "is_template": True,
            },
            {
                "path": ".gitignore",
                "content": """# Python
__pycache__/
*.py[cod]
venv/
.venv/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
""",
                "is_template": False,
            },
            {
                "path": "README.md",
                "content": """# {{ project_name }}

Outil CLI Python généré avec DevGenesis.

## 🚀 Installation

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Installer en mode développement
pip install -e .
```

## 📖 Utilisation

```bash
# Afficher l'aide
{{ project_name_snake }} --help

# Commande hello
{{ project_name_snake }} hello --name "DevGenesis"

# Afficher les informations
{{ project_name_snake }} info
```

## 📦 Technologies

- Click - Framework CLI
- Rich - Affichage terminal enrichi
- Pydantic - Validation des données

## 📝 License

MIT
""",
                "is_template": True,
            },
        ],
        "commands": ["pip install -r requirements.txt", "pip install -e ."],
        "is_builtin": True,
    }


def get_nextjs_tailwind_template() -> Dict[str, Any]:
    """Next.js + Tailwind CSS template"""
    return {
        "name": "Next.js + Tailwind",
        "description": "Application Next.js avec Tailwind CSS et TypeScript",
        "project_type": "web_frontend",
        "technologies": [
            {"name": "Next.js", "version": "^14.0.0"},
            {"name": "React", "version": "^18.2.0"},
            {"name": "Tailwind CSS", "version": "^3.4.0"},
            {"name": "TypeScript", "version": "^5.3.0"},
        ],
        "structure": [
            "src",
            "src/app",
            "src/components",
            "src/lib",
            "src/types",
            "public",
        ],
        "files": [
            {
                "path": "package.json",
                "content": json.dumps(
                    {
                        "name": "{{ project_name }}",
                        "version": "0.1.0",
                        "private": True,
                        "scripts": {
                            "dev": "next dev",
                            "build": "next build",
                            "start": "next start",
                            "lint": "next lint",
                        },
                        "dependencies": {
                            "react": "^18.2.0",
                            "react-dom": "^18.2.0",
                            "next": "^14.0.4",
                        },
                        "devDependencies": {
                            "@types/node": "^20",
                            "@types/react": "^18",
                            "@types/react-dom": "^18",
                            "autoprefixer": "^10.4.16",
                            "eslint": "^8",
                            "eslint-config-next": "^14.0.4",
                            "postcss": "^8",
                            "tailwindcss": "^3.4.0",
                            "typescript": "^5",
                        },
                    },
                    indent=2,
                ),
                "is_template": True,
            },
            {
                "path": "tailwind.config.ts",
                "content": """import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
export default config
""",
                "is_template": False,
            },
            {
                "path": "tsconfig.json",
                "content": json.dumps(
                    {
                        "compilerOptions": {
                            "target": "ES2017",
                            "lib": ["dom", "dom.iterable", "esnext"],
                            "allowJs": True,
                            "skipLibCheck": True,
                            "strict": True,
                            "noEmit": True,
                            "esModuleInterop": True,
                            "module": "esnext",
                            "moduleResolution": "bundler",
                            "resolveJsonModule": True,
                            "isolatedModules": True,
                            "jsx": "preserve",
                            "incremental": True,
                            "plugins": [{"name": "next"}],
                            "paths": {"@/*": ["./src/*"]},
                        },
                        "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
                        "exclude": ["node_modules"],
                    },
                    indent=2,
                ),
                "is_template": False,
            },
            {
                "path": "next.config.js",
                "content": """/** @type {import('next').NextConfig} */
const nextConfig = {}

module.exports = nextConfig
""",
                "is_template": False,
            },
            {
                "path": "src/app/layout.tsx",
                "content": """import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: '{{ project_name }}',
  description: 'Généré avec DevGenesis',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fr">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
""",
                "is_template": True,
            },
            {
                "path": "src/app/page.tsx",
                "content": """export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 max-w-2xl w-full">
        <h1 className="text-5xl font-bold text-gray-800 mb-4">
          {{ project_name }}
        </h1>
        <p className="text-xl text-gray-600 mb-6">
          Application Next.js générée avec DevGenesis
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-blue-50 p-6 rounded-lg">
            <h3 className="font-semibold text-blue-900 mb-2">⚡ Performance</h3>
            <p className="text-sm text-blue-700">
              Next.js offre des performances optimales avec le rendu côté serveur
            </p>
          </div>
          <div className="bg-purple-50 p-6 rounded-lg">
            <h3 className="font-semibold text-purple-900 mb-2">🎨 Tailwind CSS</h3>
            <p className="text-sm text-purple-700">
              Framework CSS utility-first pour un design rapide et moderne
            </p>
          </div>
        </div>
      </div>
    </main>
  )
}
""",
                "is_template": True,
            },
            {
                "path": "src/app/globals.css",
                "content": """@tailwind base;
@tailwind components;
@tailwind utilities;
""",
                "is_template": False,
            },
            {
                "path": ".gitignore",
                "content": """# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
""",
                "is_template": False,
            },
            {
                "path": "README.md",
                "content": """# {{ project_name }}

Application Next.js avec Tailwind CSS générée avec DevGenesis.

## 🚀 Démarrage

```bash
# Installation
npm install

# Développement
npm run dev

# Build
npm run build

# Production
npm start
```

Ouvrez [http://localhost:3000](http://localhost:3000) dans votre navigateur.

## 📦 Technologies

- Next.js 14
- React 18
- TypeScript
- Tailwind CSS

## 📝 License

MIT
""",
                "is_template": True,
            },
        ],
        "commands": ["npm install"],
        "is_builtin": True,
    }


def get_django_postgresql_template() -> Dict[str, Any]:
    """Django + PostgreSQL template"""
    return {
        "name": "Django + PostgreSQL",
        "description": "Application Django avec PostgreSQL et Docker",
        "project_type": "web_fullstack",
        "technologies": [
            {"name": "Django", "version": "^5.0.0"},
            {"name": "Python", "version": "^3.12"},
            {"name": "PostgreSQL"},
            {"name": "Docker"},
        ],
        "structure": [
            "{{ project_name_snake }}",
            "{{ project_name_snake }}/settings",
            "apps",
            "apps/core",
            "static",
            "media",
            "templates",
        ],
        "files": [
            {
                "path": "requirements.txt",
                "content": """Django==5.0.0
psycopg2-binary==2.9.9
python-decouple==3.8
django-environ==0.11.2
gunicorn==21.2.0
whitenoise==6.6.0
django-crispy-forms==2.1
crispy-bootstrap5==2.0.0
""",
                "is_template": False,
            },
            {
                "path": "Dockerfile",
                "content": """FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \\
    postgresql-client \\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "{{ project_name_snake }}.wsgi:application", "--bind", "0.0.0.0:8000"]
""",
                "is_template": True,
            },
            {
                "path": "docker-compose.yml",
                "content": """version: '3.8'

services:
  db:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB={{ project_name_snake }}
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/{{ project_name_snake }}
      - DEBUG=True
    depends_on:
      - db

volumes:
  postgres_data:
""",
                "is_template": True,
            },
            {
                "path": ".env.example",
                "content": """DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/{{ project_name_snake }}
ALLOWED_HOSTS=localhost,127.0.0.1
""",
                "is_template": True,
            },
            {
                "path": "manage.py",
                "content": """#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name_snake }}.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
""",
                "is_template": True,
            },
            {
                "path": "{{ project_name_snake }}/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "{{ project_name_snake }}/wsgi.py",
                "content": """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name_snake }}.settings.production')

application = get_wsgi_application()
""",
                "is_template": True,
            },
            {
                "path": "{{ project_name_snake }}/urls.py",
                "content": """from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
""",
                "is_template": False,
            },
            {
                "path": "{{ project_name_snake }}/settings/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "{{ project_name_snake }}/settings/base.py",
                "content": """from pathlib import Path
import environ

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'crispy_forms',
    'crispy_bootstrap5',
    
    # Local apps
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ project_name_snake }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name_snake }}.wsgi.application'

DATABASES = {
    'default': env.db('DATABASE_URL')
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
""",
                "is_template": True,
            },
            {
                "path": "{{ project_name_snake }}/settings/development.py",
                "content": """from .base import *

DEBUG = True
""",
                "is_template": False,
            },
            {
                "path": "{{ project_name_snake }}/settings/production.py",
                "content": """from .base import *

DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
""",
                "is_template": False,
            },
            {
                "path": "apps/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "apps/core/__init__.py",
                "content": "",
                "is_template": False,
            },
            {
                "path": "apps/core/apps.py",
                "content": """from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
""",
                "is_template": False,
            },
            {
                "path": "apps/core/urls.py",
                "content": """from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]
""",
                "is_template": False,
            },
            {
                "path": "apps/core/views.py",
                "content": """from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html', {
        'title': '{{ project_name }}'
    })
""",
                "is_template": True,
            },
            {
                "path": "templates/base.html",
                "content": """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ project_name }}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'core:index' %}">{{ project_name }}</a>
        </div>
    </nav>

    <main class="container mt-4">
        {% block content %}{% endblock %}
    </main>

    <footer class="bg-light text-center py-3 mt-5">
        <p class="mb-0">© 2025 {{ project_name }} - Généré avec DevGenesis</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
""",
                "is_template": True,
            },
            {
                "path": "templates/core/index.html",
                "content": """{% extends 'base.html' %}

{% block content %}
<div class="row">
    <div class="col-lg-8 mx-auto">
        <div class="card shadow">
            <div class="card-body text-center p-5">
                <h1 class="display-4 mb-4">Bienvenue sur {{ project_name }}</h1>
                <p class="lead text-muted">
                    Application Django générée avec DevGenesis
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""",
                "is_template": True,
            },
            {
                "path": ".gitignore",
                "content": """# Python
__pycache__/
*.py[cod]
venv/
.venv/

# Django
*.log
db.sqlite3
/media
/staticfiles

# Environment
.env

# IDE
.vscode/
.idea/
""",
                "is_template": False,
            },
            {
                "path": "README.md",
                "content": """# {{ project_name }}

Application Django avec PostgreSQL générée avec DevGenesis.

## 🚀 Démarrage

### Avec Docker

```bash
cp .env.example .env
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Sans Docker

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accédez à http://localhost:8000

## 📦 Technologies

- Django 5.0
- PostgreSQL
- Bootstrap 5
- Docker

## 📝 License

MIT
""",
                "is_template": True,
            },
        ],
        "commands": ["pip install -r requirements.txt"],
        "is_builtin": True,
    }


def get_all_builtin_templates() -> List[Dict[str, Any]]:
    """Get all built-in templates"""
    return [
        get_react_tailwind_vite_template(),
        get_fastapi_docker_template(),
        get_flask_bootstrap_template(),
        get_python_cli_template(),
        get_nextjs_tailwind_template(),
        get_django_postgresql_template(),
    ]


def get_template_by_name(name: str) -> Dict[str, Any] | None:
    """Get a template by name"""
    templates = get_all_builtin_templates()
    for template in templates:
        if template["name"] == name:
            return template
    return None
