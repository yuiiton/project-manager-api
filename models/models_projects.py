from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
from schemas.schemas_project import ProjectStatus, ProjectPriority

class Project(SQLModel, table=True):
    """Modelo de Projeto armazenado no banco de dados."""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str

    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    completed_at: Optional[datetime] = None

    status: ProjectStatus = ProjectStatus.pending
    priority: ProjectPriority