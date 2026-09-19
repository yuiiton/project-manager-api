from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

engine = create_engine(settings.database_url)

def create_tables():
    """Cria todas as tabelas definidas nos modelos SQLModel no banco de dados."""
    SQLModel.metadata.create_all(engine)

def get_session ():
    """Fornece uma sessão de banco de dados para injeção de dependência."""
    with Session(engine) as session:
        yield session