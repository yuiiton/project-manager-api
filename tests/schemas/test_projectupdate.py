import pytest
from datetime import datetime, timezone, timedelta
from schemas.schemas_project import ProjectUpdate, ProjectPriority, ProjectStatus

def test_project_update_valido():
    project = ProjectUpdate(
        name="Meu projeto",
        description="Minha descrição",
        priority=ProjectPriority.high
    )

    assert project.name == "Meu projeto"
    assert project.description == "Minha descrição"
    assert project.priority == ProjectPriority.high

def test_project_update_sem_campos():
    project = ProjectUpdate()

    assert project.name is None
    assert project.description is None
    assert project.status is None
    assert project.priority is None
    assert project.completed_at is None
    

def test_project_create_remove_espacos():
    project = ProjectUpdate(
        name="  Meu projeto  ",
        description="  Uma descrição  ",
        priority=ProjectPriority.medium,
    )

    assert project.name == "Meu projeto"
    assert project.description == "Uma descrição"

@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "\n",
        "\t",   
    ]
)
def test_project_update_name_invalido(name):
    with pytest.raises(ValueError):
        project = ProjectUpdate(
            name=name
        )

def test_project_update_completed_at_valido():
    """Testa se a data de conclusão é aceita quando válida (UTC, no passado e status completed)."""
    past_date = datetime.now(timezone.utc) - timedelta(days=1)
    
    project = ProjectUpdate(
        status=ProjectStatus.completed,
        completed_at=past_date
    )

    assert project.completed_at == past_date
    assert project.status == ProjectStatus.completed


def test_project_update_completed_at_status_invalido():
    """Testa se falha ao passar completed_at com um status diferente de 'completed'."""
    past_date = datetime.now(timezone.utc) - timedelta(days=1)
    
    with pytest.raises(ValueError) as exc_info:
        ProjectUpdate(
            status=ProjectStatus.in_progress,
            completed_at=past_date
        )
    
    assert "completed_at só pode ser definido se status for 'concluido'" in str(exc_info.value)


def test_project_update_completed_at_sem_timezone():
    """Testa se falha ao passar uma data sem timezone (naive datetime)."""
    naive_date = datetime.now() - timedelta(days=1)  # Sem tzinfo
    
    with pytest.raises(ValueError) as exc_info:
        ProjectUpdate(
            status=ProjectStatus.completed,
            completed_at=naive_date
        )
    
    assert "completed_at deve ser um datetime com timezone (UTC)" in str(exc_info.value)


def test_project_update_completed_at_futuro():
    """Testa se falha ao passar uma data de conclusão no futuro."""
    future_date = datetime.now(timezone.utc) + timedelta(days=1)
    
    with pytest.raises(ValueError) as exc_info:
        ProjectUpdate(
            status=ProjectStatus.completed,
            completed_at=future_date
        )
    
    assert "completed_at não pode ser no futuro" in str(exc_info.value)