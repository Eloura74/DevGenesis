"""Custom project configuration system for DevGenesis"""

from typing import Dict, List, Any, Optional
from pathlib import Path
import json
import yaml

from devgenesis.config import ROOT_DIR


class CustomProjectConfig:
    """Gestionnaire de configurations de projets personnalisées"""
    
    def __init__(self):
        self.custom_configs_dir = ROOT_DIR / "custom_configs"
        self.custom_configs_dir.mkdir(exist_ok=True)
    
    def save_config(self, name: str, config: Dict[str, Any]) -> bool:
        """Sauvegarde une configuration personnalisée"""
        try:
            config_file = self.custom_configs_dir / f"{name}.json"
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
            return False
    
    def load_config(self, name: str) -> Optional[Dict[str, Any]]:
        """Charge une configuration personnalisée"""
        try:
            config_file = self.custom_configs_dir / f"{name}.json"
            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return None
    
    def list_configs(self) -> List[str]:
        """Liste toutes les configurations personnalisées"""
        return [f.stem for f in self.custom_configs_dir.glob("*.json")]
    
    def delete_config(self, name: str) -> bool:
        """Supprime une configuration personnalisée"""
        try:
            config_file = self.custom_configs_dir / f"{name}.json"
            if config_file.exists():
                config_file.unlink()
                return True
            return False
        except Exception as e:
            print(f"Erreur lors de la suppression: {e}")
            return False
    
    def export_config(self, name: str, export_path: str) -> bool:
        """Exporte une configuration vers un fichier"""
        try:
            config = self.load_config(name)
            if config:
                export_file = Path(export_path)
                with open(export_file, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2, ensure_ascii=False)
                return True
            return False
        except Exception as e:
            print(f"Erreur lors de l'export: {e}")
            return False
    
    def import_config(self, import_path: str, name: Optional[str] = None) -> bool:
        """Importe une configuration depuis un fichier"""
        try:
            import_file = Path(import_path)
            if not import_file.exists():
                return False
            
            with open(import_file, 'r', encoding='utf-8') as f:
                if import_file.suffix == '.json':
                    config = json.load(f)
                elif import_file.suffix in ['.yml', '.yaml']:
                    config = yaml.safe_load(f)
                else:
                    return False
            
            config_name = name or import_file.stem
            return self.save_config(config_name, config)
        except Exception as e:
            print(f"Erreur lors de l'import: {e}")
            return False


# Configuration template pour créer facilement des projets personnalisés
CUSTOM_CONFIG_TEMPLATE = {
    "name": "Mon Template Personnalisé",
    "description": "Description de mon template",
    "project_type": "custom",
    "technologies": [
        {
            "name": "Technologie 1",
            "version": "1.0.0",
            "install_command": "npm install technologie1"
        }
    ],
    "structure": [
        "src",
        "src/components",
        "src/utils",
        "tests",
        "docs"
    ],
    "files": [
        {
            "path": "README.md",
            "content": "# {{ project_name }}\n\n{{ description }}",
            "is_template": True
        },
        {
            "path": "package.json",
            "content": "{\n  \"name\": \"{{ project_name }}\",\n  \"version\": \"1.0.0\"\n}",
            "is_template": True
        }
    ],
    "commands": [
        "npm install",
        "npm run build"
    ],
    "options": {
        "git_init": True,
        "create_venv": False,
        "install_deps": True
    }
}


# Suggestions de technologies par catégorie
TECHNOLOGY_SUGGESTIONS = {
    "frontend": {
        "frameworks": ["React", "Vue", "Svelte", "Angular", "Solid.js", "Preact"],
        "styling": ["Tailwind CSS", "Bootstrap", "Material-UI", "Chakra UI", "Styled Components"],
        "build_tools": ["Vite", "Webpack", "Rollup", "esbuild", "Parcel"],
        "state_management": ["Redux", "Zustand", "Jotai", "Recoil", "MobX"],
        "routing": ["React Router", "Vue Router", "TanStack Router"],
    },
    "backend": {
        "python": ["FastAPI", "Flask", "Django", "Tornado", "Sanic"],
        "nodejs": ["Express", "NestJS", "Fastify", "Koa", "Hapi"],
        "go": ["Gin", "Echo", "Fiber", "Chi"],
        "rust": ["Actix", "Rocket", "Axum", "Warp"],
    },
    "database": {
        "sql": ["PostgreSQL", "MySQL", "SQLite", "MariaDB"],
        "nosql": ["MongoDB", "Redis", "Cassandra", "CouchDB"],
        "orm": ["SQLAlchemy", "Prisma", "TypeORM", "Sequelize"],
    },
    "devops": {
        "containerization": ["Docker", "Podman", "Kubernetes"],
        "ci_cd": ["GitHub Actions", "GitLab CI", "Jenkins", "CircleCI"],
        "monitoring": ["Prometheus", "Grafana", "ELK Stack"],
    },
    "testing": {
        "unit": ["Jest", "Vitest", "Pytest", "Mocha"],
        "e2e": ["Playwright", "Cypress", "Selenium"],
        "api": ["Postman", "Insomnia", "HTTPie"],
    },
    "mobile": {
        "frameworks": ["React Native", "Flutter", "Ionic", "Capacitor"],
        "tools": ["Expo", "Metro", "Android Studio", "Xcode"],
    },
    "desktop": {
        "frameworks": ["Electron", "Tauri", "Qt", "GTK"],
        "languages": ["JavaScript", "Rust", "C++", "Python"],
    }
}


# Patterns de structure de projet par type
PROJECT_STRUCTURE_PATTERNS = {
    "monorepo": {
        "structure": [
            "packages",
            "packages/frontend",
            "packages/backend",
            "packages/shared",
            "apps",
            "tools",
            "docs"
        ],
        "files": [
            {"path": "package.json", "content": "{\n  \"workspaces\": [\"packages/*\", \"apps/*\"]\n}"},
            {"path": "turbo.json", "content": "{}"},
            {"path": "pnpm-workspace.yaml", "content": "packages:\n  - 'packages/*'\n  - 'apps/*'"}
        ]
    },
    "microservices": {
        "structure": [
            "services",
            "services/api-gateway",
            "services/auth-service",
            "services/user-service",
            "shared",
            "infrastructure",
            "docker"
        ],
        "files": [
            {"path": "docker-compose.yml", "content": "version: '3.8'\nservices:"},
            {"path": "kubernetes/deployment.yaml", "content": "apiVersion: apps/v1"}
        ]
    },
    "clean_architecture": {
        "structure": [
            "src",
            "src/domain",
            "src/domain/entities",
            "src/domain/repositories",
            "src/application",
            "src/application/use_cases",
            "src/infrastructure",
            "src/infrastructure/database",
            "src/infrastructure/api",
            "src/presentation",
            "tests"
        ]
    },
    "feature_based": {
        "structure": [
            "src",
            "src/features",
            "src/features/auth",
            "src/features/user",
            "src/features/dashboard",
            "src/shared",
            "src/shared/components",
            "src/shared/utils",
            "src/shared/hooks"
        ]
    }
}


def get_technology_suggestions(category: str) -> Dict[str, List[str]]:
    """Obtient les suggestions de technologies pour une catégorie"""
    return TECHNOLOGY_SUGGESTIONS.get(category, {})


def get_structure_pattern(pattern: str) -> Dict[str, Any]:
    """Obtient un pattern de structure de projet"""
    return PROJECT_STRUCTURE_PATTERNS.get(pattern, {})


def create_custom_template(
    name: str,
    description: str,
    technologies: List[Dict[str, str]],
    structure: List[str],
    files: List[Dict[str, Any]],
    commands: List[str],
    project_type: str = "custom"
) -> Dict[str, Any]:
    """Crée un template personnalisé"""
    return {
        "name": name,
        "description": description,
        "project_type": project_type,
        "technologies": technologies,
        "structure": structure,
        "files": files,
        "commands": commands,
        "is_builtin": False
    }
