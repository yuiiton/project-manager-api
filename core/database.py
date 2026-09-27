from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

engine = create_engine(settings.database_url)

def get_session ():
    """Fornece uma sessão de banco de dados para injeção de dependência."""
    with Session(engine) as session:
        yield session