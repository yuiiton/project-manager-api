import pytest
from schemas.schemas_project import ProjectCreate, ProjectPriority

def test_project_valido():
    project = ProjectCreate(
        name="Meu projeto",
        description="Minha descrição",
        priority=ProjectPriority.high,
    )

    assert project.name == "Meu projeto"
    assert project.description == "Minha descrição"
    assert project.priority == ProjectPriority.high

def test_project_create_remove_espacos():
    project = ProjectCreate(
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
            None
        ]
)
def test_project_create_nome_invalido(name):
    with pytest.raises(ValueError):
        ProjectCreate(
            name=name,
            description="Descrição válida",
            priority=ProjectPriority.medium,
        )