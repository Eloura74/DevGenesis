"""Project generator engine for DevGenesis"""

import os
import subprocess
import shutil
from pathlib import Path
from typing import Dict, Any, List, Callable, Optional
from datetime import datetime
import json
import re

from jinja2 import Template
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID

from devgenesis.models import ProjectConfig, FileTemplate, TechnologyConfig

console = Console()


class ProjectGenerator:
    """Main project generator class"""

    def __init__(self, config: ProjectConfig, progress_callback: Optional[Callable] = None):
        self.config = config
        self.project_path = Path(config.path)
        self.progress_callback = progress_callback
        self.console = Console()

    def _log(self, message: str, level: str = "info") -> None:
        """Log a message"""
        if self.progress_callback:
            self.progress_callback(message, level)
        
        if level == "error":
            self.console.print(f"[red]❌ {message}[/red]")
        elif level == "success":
            self.console.print(f"[green]✓ {message}[/green]")
        elif level == "warning":
            self.console.print(f"[yellow]⚠ {message}[/yellow]")
        else:
            self.console.print(f"[blue]ℹ {message}[/blue]")

    def _to_snake_case(self, text: str) -> str:
        """Convert text to snake_case"""
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '_', text)
        return text.lower()

    def _render_template(self, content: str, context: Dict[str, Any]) -> str:
        """Render a Jinja2 template"""
        template = Template(content)
        return template.render(**context)

    def _create_directory_structure(self) -> None:
        """Create the project directory structure"""
        self._log(f"Création de la structure du projet dans {self.project_path}")
        
        # Create main project directory
        self.project_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        context = {
            "project_name": self.config.name,
            "project_name_snake": self._to_snake_case(self.config.name),
        }
        
        for directory in self.config.structure:
            # Render directory name with template variables
            dir_name = self._render_template(directory, context)
            dir_path = self.project_path / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            self._log(f"Créé: {dir_path.relative_to(self.project_path)}", "success")

    def _create_files(self) -> None:
        """Create project files from templates"""
        self._log("Génération des fichiers du projet")
        
        context = {
            "project_name": self.config.name,
            "project_name_snake": self._to_snake_case(self.config.name),
            "description": self.config.description or "",
            "author": os.environ.get("USER", "DevGenesis User"),
            "year": datetime.now().year,
        }
        
        for file_template in self.config.files:
            # Render file path with template variables
            file_path_str = self._render_template(file_template.path, context)
            file_path = self.project_path / file_path_str
            
            # Ensure parent directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Render file content
            if file_template.is_template:
                content = self._render_template(file_template.content, context)
            else:
                content = file_template.content
            
            # Write file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            self._log(f"Créé: {file_path.relative_to(self.project_path)}", "success")

    def _initialize_git(self) -> None:
        """Initialize Git repository"""
        if not self.config.git_init:
            return
        
        self._log("Initialisation du dépôt Git")
        
        try:
            subprocess.run(
                ["git", "init"],
                cwd=self.project_path,
                check=True,
                capture_output=True,
                text=True,
            )
            
            subprocess.run(
                ["git", "add", "."],
                cwd=self.project_path,
                check=True,
                capture_output=True,
                text=True,
            )
            
            subprocess.run(
                ["git", "commit", "-m", "Initial commit from DevGenesis"],
                cwd=self.project_path,
                check=True,
                capture_output=True,
                text=True,
            )
            
            self._log("Dépôt Git initialisé", "success")
        except subprocess.CalledProcessError as e:
            self._log(f"Erreur lors de l'initialisation Git: {e}", "warning")
        except FileNotFoundError:
            self._log("Git n'est pas installé sur ce système", "warning")

    def _create_virtual_environment(self) -> None:
        """Create Python virtual environment"""
        if not self.config.create_venv:
            return
        
        # Check if this is a Python project
        has_python = any(
            tech.name.lower() == "python" for tech in self.config.technologies
        )
        
        if not has_python:
            return
        
        self._log("Création de l'environnement virtuel Python")
        
        venv_path = self.project_path / "venv"
        
        try:
            subprocess.run(
                ["python", "-m", "venv", str(venv_path)],
                check=True,
                capture_output=True,
                text=True,
            )
            self._log("Environnement virtuel créé", "success")
        except subprocess.CalledProcessError as e:
            self._log(f"Erreur lors de la création du venv: {e}", "warning")

    def _run_commands(self) -> None:
        """Run post-generation commands"""
        if not self.config.commands:
            return
        
        self._log("Exécution des commandes d'installation")
        
        for command in self.config.commands:
            self._log(f"Exécution: {command}")
            
            try:
                # Determine if we should use venv
                venv_path = self.project_path / "venv"
                
                if venv_path.exists() and command.startswith(("pip ", "python ")):
                    # Use venv Python/pip
                    if os.name == "nt":  # Windows
                        python_exe = venv_path / "Scripts" / "python.exe"
                        pip_exe = venv_path / "Scripts" / "pip.exe"
                    else:  # Unix
                        python_exe = venv_path / "bin" / "python"
                        pip_exe = venv_path / "bin" / "pip"
                    
                    if command.startswith("pip "):
                        command = command.replace("pip", str(pip_exe), 1)
                    elif command.startswith("python "):
                        command = command.replace("python", str(python_exe), 1)
                
                result = subprocess.run(
                    command,
                    shell=True,
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=300,  # 5 minutes timeout
                )
                
                if result.returncode == 0:
                    self._log(f"Commande réussie: {command}", "success")
                else:
                    self._log(f"Erreur dans la commande: {result.stderr}", "warning")
                    
            except subprocess.TimeoutExpired:
                self._log(f"Timeout pour la commande: {command}", "warning")
            except Exception as e:
                self._log(f"Erreur lors de l'exécution: {e}", "warning")

    def _create_summary_file(self) -> None:
        """Create a project summary file"""
        summary = {
            "project_name": self.config.name,
            "description": self.config.description,
            "project_type": self.config.project_type,
            "technologies": [
                {"name": tech.name, "version": tech.version}
                for tech in self.config.technologies
            ],
            "created_at": datetime.now().isoformat(),
            "generator": "DevGenesis v1.0.0",
        }
        
        summary_path = self.project_path / ".devgenesis.json"
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        self._log("Fichier de résumé créé", "success")

    def generate(self) -> bool:
        """Generate the complete project"""
        try:
            self._log(f"🚀 Génération du projet: {self.config.name}")
            
            # Check if directory already exists
            if self.project_path.exists() and any(self.project_path.iterdir()):
                self._log(
                    f"Le répertoire {self.project_path} existe déjà et n'est pas vide",
                    "error"
                )
                return False
            
            # Step 1: Create directory structure
            self._create_directory_structure()
            
            # Step 2: Create files
            self._create_files()
            
            # Step 3: Initialize Git
            self._initialize_git()
            
            # Step 4: Create virtual environment
            self._create_virtual_environment()
            
            # Step 5: Run installation commands
            self._run_commands()
            
            # Step 6: Create summary file
            self._create_summary_file()
            
            self._log(
                f"✅ Projet généré avec succès dans {self.project_path}",
                "success"
            )
            return True
            
        except Exception as e:
            self._log(f"Erreur lors de la génération: {e}", "error")
            return False

    def validate_config(self) -> tuple[bool, List[str]]:
        """Validate project configuration"""
        errors = []
        
        if not self.config.name:
            errors.append("Le nom du projet est requis")
        
        if not self.config.project_type:
            errors.append("Le type de projet est requis")
        
        if not self.config.path:
            errors.append("Le chemin du projet est requis")
        
        if not self.config.technologies:
            errors.append("Au moins une technologie doit être sélectionnée")
        
        # Check if path is writable
        try:
            parent_path = Path(self.config.path).parent
            if not parent_path.exists():
                parent_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            errors.append(f"Impossible de créer le répertoire: {e}")
        
        return len(errors) == 0, errors


def generate_project_from_template(
    template: Dict[str, Any],
    project_name: str,
    project_path: str,
    description: Optional[str] = None,
    progress_callback: Optional[Callable] = None,
) -> bool:
    """Generate a project from a template dictionary"""
    
    # Convert template to ProjectConfig
    technologies = [
        TechnologyConfig(
            name=tech["name"],
            version=tech.get("version"),
        )
        for tech in template["technologies"]
    ]
    
    files = [
        FileTemplate(
            path=file["path"],
            content=file["content"],
            is_template=file.get("is_template", False),
        )
        for file in template["files"]
    ]
    
    config = ProjectConfig(
        name=project_name,
        description=description or template["description"],
        project_type=template["project_type"],
        path=project_path,
        technologies=technologies,
        structure=template["structure"],
        files=files,
        commands=template.get("commands", []),
        git_init=True,
        create_venv="Python" in [tech.name for tech in technologies],
    )
    
    # Validate configuration
    generator = ProjectGenerator(config, progress_callback)
    is_valid, errors = generator.validate_config()
    
    if not is_valid:
        if progress_callback:
            for error in errors:
                progress_callback(error, "error")
        return False
    
    # Generate project
    return generator.generate()
