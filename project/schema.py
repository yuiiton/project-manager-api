from enum import Enum
from datetime import datetime, timezone
from core.exceptions.commom_exceptions import InvalidValueError
from pydantic import BaseModel, ConfigDict, Field, field_validator


class ProjectStatus(str, Enum):
    pending = "pendente"
    in_progress = "em_progresso"
    completed = "concluido"
    cancelled = "cancelado"


class ProjectPriority(int, Enum):
    high = 1
    medium = 2
    low = 3


class ProjectCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1, max_length=1000)
    priority: ProjectPriority = Field(..., description="Prioridade do projeto")

    @field_validator("name", "description")
    @classmethod
    def strip_strings(cls, v: str) -> str:
        """Remove espaços em branco do início e fim da string e valida se não está vazia."""
        v = v.strip()
        if not v:
            raise InvalidValueError("Campo não pode ser vazio ou conter apenas espaços.")
        return v


class ProjectUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, min_length=1, max_length=1000)
    status: ProjectStatus | None = None
    priority: ProjectPriority | None = None
    completed_at: datetime | None = None

    @field_validator("name", "description")
    @classmethod
    def strip_strings(cls, v):
        """Remove espaços em branco do início e fim da string, se não for None."""
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise InvalidValueError("Campo não pode ser vazio ou conter apenas espaços.")
        return v

    @field_validator("completed_at")
    @classmethod
    def validate_completed_at(cls, v, info):
        """Valida que completed_at seja UTC-aware, no passado e só com status 'concluido'."""
        status = info.data.get("status")

        if v is None:
            return None

        if status is not None and status != ProjectStatus.completed:
            raise InvalidValueError("completed_at só pode ser definido se status for 'concluido'.")

        if v.tzinfo is None or v.tzinfo.utcoffset(v) is None:
            raise InvalidValueError("completed_at deve ser um datetime com timezone (UTC).")

        now_utc = datetime.now(tz=timezone.utc)
        if v > now_utc:
            raise InvalidValueError("completed_at não pode ser no futuro.")

        return v


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str

    status: ProjectStatus
    priority: ProjectPriority

    created_at: datetime
    completed_at: datetime | None = None