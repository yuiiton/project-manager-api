from schemas.schemas_project import ProjectCreate, ProjectUpdate
from sqlmodel import select, Session
from models.models_projects import Project


def get_project_by_id_repository(session: Session, project_id: int) -> Project | None:
    """Busca um projeto pelo id no banco de dados."""
    return session.get(Project, project_id)

def get_project_by_name(session: Session, project_name: str) -> Project | None:
    """Busca um projeto pelo nome no banco de dados."""
    statement = select(Project).where(Project.name == project_name)
    return session.exec(statement).first()

def get_all_projects(session: Session) -> list[Project]:
    """Busca todos os projetos no banco de dados."""
    statement = select(Project)
    return session.exec(statement).all()


def create_project(project_data: ProjectCreate, session: Session) -> Project:
    """Cria um projeto no banco de dados."""
    project = Project.model_validate(project_data)

    session.add(project)
    session.commit()
    session.refresh(project)
    return project
    


def update_project(project_update: ProjectUpdate, project_id: int, session: Session) -> Project | None:
    """Atualiza um projeto no banco de dados."""
    project = session.get(Project, project_id)

    if not project:
        return None

    update_data = project_update.model_dump(exclude_unset=True)

    project.sqlmodel_update(update_data)

    session.add(project)
    session.commit()
    session.refresh(project)

    return project


def delete_project(session: Session, project_id: int) -> bool:
    """Deleta um projeto do banco de dados."""
    project = session.get(Project, project_id)

    if not project:
        return False

    session.delete(project)
    session.commit()
    return True
    