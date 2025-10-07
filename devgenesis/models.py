"""Database models for DevGenesis"""

from datetime import datetime
from typing import Optional, List, Dict, Any
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, Field
import json

from devgenesis.config import DATABASE_PATH

Base = declarative_base()


class ProjectTemplate(Base):
    """Database model for project templates"""

    __tablename__ = "project_templates"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)
    description = Column(Text)
    project_type = Column(String(100), nullable=False)
    technologies = Column(Text, nullable=False)  # JSON string
    structure = Column(Text, nullable=False)  # JSON string
    files = Column(Text, nullable=False)  # JSON string
    commands = Column(Text)  # JSON string
    is_builtin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "project_type": self.project_type,
            "technologies": json.loads(self.technologies),
            "structure": json.loads(self.structure),
            "files": json.loads(self.files),
            "commands": json.loads(self.commands) if self.commands else [],
            "is_builtin": self.is_builtin,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class ProjectHistory(Base):
    """Database model for project generation history"""

    __tablename__ = "project_history"

    id = Column(Integer, primary_key=True)
    project_name = Column(String(200), nullable=False)
    project_path = Column(String(500), nullable=False)
    template_name = Column(String(200))
    technologies = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="success")  # success, failed, in_progress

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "project_name": self.project_name,
            "project_path": self.project_path,
            "template_name": self.template_name,
            "technologies": json.loads(self.technologies) if self.technologies else [],
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "status": self.status,
        }


# Pydantic models for validation
class TechnologyConfig(BaseModel):
    """Configuration for a technology"""

    name: str
    version: Optional[str] = None
    install_command: Optional[str] = None
    config_files: List[str] = Field(default_factory=list)


class FileTemplate(BaseModel):
    """Template for a file to be generated"""

    path: str
    content: str
    is_template: bool = False  # If true, use Jinja2 templating


class ProjectConfig(BaseModel):
    """Configuration for a project to be generated"""

    name: str
    description: Optional[str] = None
    project_type: str
    path: str
    technologies: List[TechnologyConfig]
    structure: List[str]  # List of directories to create
    files: List[FileTemplate]
    commands: List[str] = Field(default_factory=list)  # Commands to run after generation
    git_init: bool = True
    create_venv: bool = True


# Database initialization
engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_database() -> None:
    """Initialize the database"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
