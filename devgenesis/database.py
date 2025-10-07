"""Database service layer for DevGenesis"""

from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
import json

from devgenesis.models import (
    ProjectTemplate,
    ProjectHistory,
    SessionLocal,
    init_database,
)
from devgenesis.templates.builtin_templates import get_all_builtin_templates


class DatabaseService:
    """Service for database operations"""

    def __init__(self):
        init_database()
        self._ensure_builtin_templates()

    def _get_session(self) -> Session:
        """Get a database session"""
        return SessionLocal()

    def _ensure_builtin_templates(self) -> None:
        """Ensure built-in templates are in the database"""
        session = self._get_session()
        try:
            # Check if we already have built-in templates
            existing_count = session.query(ProjectTemplate).filter_by(is_builtin=True).count()
            
            if existing_count > 0:
                return
            
            # Add built-in templates
            builtin_templates = get_all_builtin_templates()
            
            for template_data in builtin_templates:
                template = ProjectTemplate(
                    name=template_data["name"],
                    description=template_data["description"],
                    project_type=template_data["project_type"],
                    technologies=json.dumps(template_data["technologies"]),
                    structure=json.dumps(template_data["structure"]),
                    files=json.dumps(template_data["files"]),
                    commands=json.dumps(template_data.get("commands", [])),
                    is_builtin=True,
                )
                session.add(template)
            
            session.commit()
        finally:
            session.close()

    def get_all_templates(self) -> List[Dict[str, Any]]:
        """Get all templates from database"""
        session = self._get_session()
        try:
            templates = session.query(ProjectTemplate).all()
            return [template.to_dict() for template in templates]
        finally:
            session.close()

    def get_template_by_id(self, template_id: int) -> Optional[Dict[str, Any]]:
        """Get a template by ID"""
        session = self._get_session()
        try:
            template = session.query(ProjectTemplate).filter_by(id=template_id).first()
            return template.to_dict() if template else None
        finally:
            session.close()

    def get_template_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a template by name"""
        session = self._get_session()
        try:
            template = session.query(ProjectTemplate).filter_by(name=name).first()
            return template.to_dict() if template else None
        finally:
            session.close()

    def get_templates_by_type(self, project_type: str) -> List[Dict[str, Any]]:
        """Get templates by project type"""
        session = self._get_session()
        try:
            templates = session.query(ProjectTemplate).filter_by(project_type=project_type).all()
            return [template.to_dict() for template in templates]
        finally:
            session.close()

    def create_template(
        self,
        name: str,
        description: str,
        project_type: str,
        technologies: List[Dict[str, Any]],
        structure: List[str],
        files: List[Dict[str, Any]],
        commands: List[str],
    ) -> Dict[str, Any]:
        """Create a new custom template"""
        session = self._get_session()
        try:
            template = ProjectTemplate(
                name=name,
                description=description,
                project_type=project_type,
                technologies=json.dumps(technologies),
                structure=json.dumps(structure),
                files=json.dumps(files),
                commands=json.dumps(commands),
                is_builtin=False,
            )
            session.add(template)
            session.commit()
            session.refresh(template)
            return template.to_dict()
        finally:
            session.close()

    def update_template(
        self,
        template_id: int,
        **kwargs: Any,
    ) -> Optional[Dict[str, Any]]:
        """Update a template"""
        session = self._get_session()
        try:
            template = session.query(ProjectTemplate).filter_by(id=template_id).first()
            
            if not template:
                return None
            
            # Don't allow updating built-in templates
            if template.is_builtin:
                return None
            
            # Update fields
            for key, value in kwargs.items():
                if hasattr(template, key):
                    if key in ["technologies", "structure", "files", "commands"]:
                        setattr(template, key, json.dumps(value))
                    else:
                        setattr(template, key, value)
            
            session.commit()
            session.refresh(template)
            return template.to_dict()
        finally:
            session.close()

    def delete_template(self, template_id: int) -> bool:
        """Delete a template"""
        session = self._get_session()
        try:
            template = session.query(ProjectTemplate).filter_by(id=template_id).first()
            
            if not template:
                return False
            
            # Don't allow deleting built-in templates
            if template.is_builtin:
                return False
            
            session.delete(template)
            session.commit()
            return True
        finally:
            session.close()

    def add_project_history(
        self,
        project_name: str,
        project_path: str,
        template_name: Optional[str],
        technologies: List[str],
        status: str = "success",
    ) -> Dict[str, Any]:
        """Add a project to history"""
        session = self._get_session()
        try:
            history = ProjectHistory(
                project_name=project_name,
                project_path=project_path,
                template_name=template_name,
                technologies=json.dumps(technologies),
                status=status,
            )
            session.add(history)
            session.commit()
            session.refresh(history)
            return history.to_dict()
        finally:
            session.close()

    def get_project_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get project generation history"""
        session = self._get_session()
        try:
            history = (
                session.query(ProjectHistory)
                .order_by(ProjectHistory.created_at.desc())
                .limit(limit)
                .all()
            )
            return [item.to_dict() for item in history]
        finally:
            session.close()

    def clear_history(self) -> bool:
        """Clear all project history"""
        session = self._get_session()
        try:
            session.query(ProjectHistory).delete()
            session.commit()
            return True
        finally:
            session.close()

    def search_templates(self, query: str) -> List[Dict[str, Any]]:
        """Search templates by name or description"""
        session = self._get_session()
        try:
            templates = (
                session.query(ProjectTemplate)
                .filter(
                    (ProjectTemplate.name.ilike(f"%{query}%"))
                    | (ProjectTemplate.description.ilike(f"%{query}%"))
                )
                .all()
            )
            return [template.to_dict() for template in templates]
        finally:
            session.close()

    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics"""
        session = self._get_session()
        try:
            total_templates = session.query(ProjectTemplate).count()
            builtin_templates = session.query(ProjectTemplate).filter_by(is_builtin=True).count()
            custom_templates = total_templates - builtin_templates
            total_projects = session.query(ProjectHistory).count()
            successful_projects = (
                session.query(ProjectHistory).filter_by(status="success").count()
            )
            
            return {
                "total_templates": total_templates,
                "builtin_templates": builtin_templates,
                "custom_templates": custom_templates,
                "total_projects": total_projects,
                "successful_projects": successful_projects,
            }
        finally:
            session.close()
