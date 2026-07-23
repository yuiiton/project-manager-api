from repository.repository_projects import get_project_by_id_repository, get_all_projects, create_project, update_project, get_project_by_name, delete_project
from core.exceptions.commom_exceptions import ItemNotFoundError, BusinessRuleError
from models.models_projects import Project
from sqlmodel import Session
from schemas.schemas_project import ProjectCreate, ProjectUpdate


def get_project_by_id_service(session: Session, project_id: int) -> Project:
    """Retorna o projeto com o id especificado.

    Args:
        session (Session): Sessão do banco de dados.
        project_id (int): ID do projeto para ser retornado.

    Returns:
        Project: O projeto.

    Raises:
        ItemNotFoundError: Caso não exista um projeto com o ID especificado.
        
    
    """
    project = get_project_by_id_repository(session, project_id)

    if not project:
        raise ItemNotFoundError("Projeto não encontrado.")

    return project

def get_all_projects_service(session: Session) -> list[Project]:
    """Retorna todos os projetos

    Args:
        session (Session): Sessão do banco.
    
    Returns:
        list[Project]: Todos os projetos cadastrados (pode ser vazia).
        
    
    """
    project_list = get_all_projects(session)
    
    return project_list

def create_project_service(project_data: ProjectCreate, session: Session) -> Project:
    """Cria um projeto.

    Args:
        project_data (ProjectCreate): Dados do projeto.
        session (Session): Sessão do banco de dados.

    Returns:
        Project: Projecto criado.

    Raises:
        BusinessRuleError: Caso já exista um projeto cadastrado com o nome enviado.
    
    """
    project_exists = get_project_by_name(session, project_data.name)
    if project_exists:
        raise BusinessRuleError("Já existe um projeto com esse nome.")

    project = create_project(project_data, session)
    return project

def update_project_service(project_data: ProjectUpdate, project_id: int, session: Session,) -> Project:
    """Atualiza um projeto cadastrado.
    
    Args:
        project_data (ProjectCreate): Dados do projeto.
        project_id (int): ID do projeto para ser atualizado.
        session (Session): Sessão do banco de dados.
    
    Returns:
        Project: Projeto atualizado.
    
    Raises:
        ItemNotFoundError: Caso não exista um projeto com o ID especificado.
    """
    project = update_project(project_data, project_id, session)

    if not project:
        raise ItemNotFoundError("Não foi possível encontrar o projeto especificado para realizar alterações.")

    return project

def delete_project_service(project_id: int, session: Session) -> None:
    """Deleta um projeto cadastrado.

    Args:
        project_id (int): ID do projeto para ser deletado.
        session (Session): Sessão do banco de dados.
    
    Returns:
        None
    
    Raises:
        ItemNotFoundError: Caso não exista um projeto com o ID especificado.
    
    """
    project_deleted = delete_project(session, project_id)

    if not project_deleted:
        raise ItemNotFoundError("Projeto não encontrado.")
    