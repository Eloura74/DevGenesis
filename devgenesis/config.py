"""Configuration management for DevGenesis"""

from pathlib import Path
from typing import Dict, Any
import json

# Application paths
APP_DIR = Path(__file__).parent
ROOT_DIR = APP_DIR.parent
TEMPLATES_DIR = APP_DIR / "templates"
USER_TEMPLATES_DIR = ROOT_DIR / "user_templates"
DATABASE_PATH = ROOT_DIR / "devgenesis.db"

# Ensure directories exist
USER_TEMPLATES_DIR.mkdir(exist_ok=True)
TEMPLATES_DIR.mkdir(exist_ok=True)

# Application settings
APP_NAME = "DevGenesis"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Générateur universel de projets et environnements de développement"

# UI Configuration
UI_CONFIG = {
    "window_title": f"{APP_NAME} v{APP_VERSION}",
    "window_width": 1400,
    "window_height": 900,
    "min_width": 1200,
    "min_height": 700,
    "theme": "dark",  # dark or light
}

# Supported technologies
SUPPORTED_LANGUAGES = [
    "Python",
    "JavaScript",
    "TypeScript",
    "Go",
    "Rust",
    "Java",
    "C#",
]

FRONTEND_FRAMEWORKS = [
    "React",
    "Vue",
    "Svelte",
    "Next.js",
    "Nuxt.js",
    "Angular",
    "Solid.js",
]

BACKEND_FRAMEWORKS = [
    "FastAPI",
    "Flask",
    "Django",
    "Express",
    "NestJS",
    "Gin",
    "Actix",
]

CSS_FRAMEWORKS = [
    "Tailwind CSS",
    "Bootstrap",
    "Material-UI",
    "Chakra UI",
    "Ant Design",
    "Bulma",
]

BUILD_TOOLS = [
    "Vite",
    "Webpack",
    "Rollup",
    "esbuild",
    "Parcel",
    "Turbopack",
]

DATABASES = [
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "SQLite",
    "Redis",
    "Supabase",
]

DEVOPS_TOOLS = [
    "Docker",
    "Docker Compose",
    "Kubernetes",
    "GitHub Actions",
    "GitLab CI",
]

# Project type categories
PROJECT_TYPES = {
    "web_frontend": {
        "name": "Frontend Web Application",
        "icon": "category_frontend",
        "description": "Application web moderne avec React, Vue ou autre framework frontend",
        "recommended_tech": ["React", "Tailwind CSS", "Vite", "TypeScript"],
    },
    "web_fullstack": {
        "name": "Full-Stack Web Application",
        "icon": "category_fullstack",
        "description": "Application complète avec frontend et backend intégrés",
        "recommended_tech": ["React", "FastAPI", "PostgreSQL", "Docker"],
    },
    "api_backend": {
        "name": "API Backend",
        "icon": "category_backend",
        "description": "API REST ou GraphQL avec base de données",
        "recommended_tech": ["FastAPI", "PostgreSQL", "Docker", "Redis"],
    },
    "ai_ml": {
        "name": "AI / Machine Learning",
        "icon": "category_ai",
        "description": "Projet d'intelligence artificielle ou machine learning",
        "recommended_tech": ["Python", "PyTorch", "Jupyter", "FastAPI"],
    },
    "cli_tool": {
        "name": "CLI Tool / Automation",
        "icon": "category_cli",
        "description": "Outil en ligne de commande ou script d'automatisation",
        "recommended_tech": ["Python", "Rich", "Click", "Poetry"],
    },
    "mobile": {
        "name": "Mobile Application",
        "icon": "category_mobile",
        "description": "Application mobile cross-platform",
        "recommended_tech": ["React Native", "Expo", "TypeScript"],
    },
    "desktop": {
        "name": "Desktop Application",
        "icon": "category_desktop",
        "description": "Application desktop multi-plateforme",
        "recommended_tech": ["Electron", "React", "TypeScript", "Tauri"],
    },
    "iot": {
        "name": "IoT / Embedded",
        "icon": "category_iot",
        "description": "Projet IoT ou système embarqué",
        "recommended_tech": ["Python", "MicroPython", "MQTT", "Docker"],
    },
}


def load_user_config() -> Dict[str, Any]:
    """Load user configuration from file"""
    config_file = ROOT_DIR / "user_config.json"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_user_config(config: Dict[str, Any]) -> None:
    """Save user configuration to file"""
    config_file = ROOT_DIR / "user_config.json"
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
