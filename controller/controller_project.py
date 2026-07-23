from fastapi import APIRouter, Depends, status, HTTPException
from schemas.schemas_project import ProjectResponse, ProjectCreate, ProjectUpdate
from core.database import get_session
from sqlmodel import Session
from services.service_project import get_project_by_id_service, get_all_projects_service, create_project_service, update_project_service, delete_project_service

project_router = APIRouter(prefix="/projects", tags=["Projects"])


@project_router.get("/", 
                    summary="Busca todos os projetos cadastrados.",
                    description="""Retorna todos os projetos cadastrados.
                    
                    - Caso não haja nenhum, retorna uma lista vazia.
                    """,      
                    status_code=status.HTTP_200_OK, 
                    response_model=list[ProjectResponse],)
def get_all_project_route(session: Session = Depends(get_session)):
    """Retorna todos os projetos cadastrados."""
    return get_all_projects_service(session)


@project_router.get("/{project_id}",
                    summary="Busca o projeto cadastrado com o id especificado.",
                    description="""Retorna o projeto cadastrado com o id especificado.
                    
                    - Requer ID válido.
                    """,
                    status_code=status.HTTP_200_OK, 
                    response_model=ProjectResponse,
                    responses={
                            404: {"description": "Projeto não encontrado"},
                            422: {"description": "Dados inválidos."}
    })
def get_project_route(project_id: int, session: Session = Depends(get_session)):
    """Retorna o projeto cadastrado com o id especificado."""
    return get_project_by_id_service(session, project_id)
    

@project_router.post("/", 
                     summary="Cadastra um projeto.",
                     description="""Cadastra um projeto no banco de dados.
                     
                     - É necessário fornecer corretamente os parâmetros de *project_data*.
                     - O nome do projeto não pode ser igual ao de um projeto já cadastrado.
                     """,
                     status_code=status.HTTP_201_CREATED, 
                     response_model=ProjectResponse,
                     responses={
                         400: {"description": "Já existe um projeto com esse nome."},
                         422: {"description": "Dados inválidos."}
                     })
def create_project_route(project_data: ProjectCreate, session: Session = Depends(get_session)):
    """Cadastra um projeto."""
    return create_project_service(project_data, session)

@project_router.patch("/{project_id}",
                      summary="Atualiza um projeto cadastrado.",
                      description="""Atualiza um projeto cadastrado.
                      
                      - É necessário fornecer corretamente os parâmetros de *project_data*.
                      - Todos os parâmetros são opcionais.
                      - O parâmetro *completed_at* só pode ser fornecido se *status* for igual a "concluido". 
                      """,
                      status_code=status.HTTP_200_OK, 
                      response_model=ProjectResponse,
                      responses={
                          422: {"description": "Dados inválidos."},
                          404: {"description": "Não foi possível encontrar o projeto especificado para realizar alterações."},
                          400: {
                                "description": """
                                Possíveis erros:
                                - completed_at só pode ser definido se status for 'concluido'
                                - completed_at deve ser um datetime com timezone (ex: UTC)
                                - completed_at não pode ser no futuro"""
    }
                      })
def update_project_route(project_data: ProjectUpdate, project_id: int, session: Session = Depends(get_session)):
    """Atualiza um projeto cadastrado."""
    return update_project_service(project_data, project_id, session)

@project_router.delete("/{project_id}",
                       summary="Deleta um projeto cadastrado.",
                       description="""Deleta um projeto cadastrado.
                       
                       - Requer ID válido.
                       """,
                       status_code=status.HTTP_204_NO_CONTENT,
                       responses={
                           404: {"description": "Projeto não encontrado."},
                           422: {"description": "Dados inválidos."}
                       })
def delete_project_route(project_id: int, session: Session = Depends(get_session)):
    """Deleta um projeto cadastrado."""
    delete_project_service(project_id, session)