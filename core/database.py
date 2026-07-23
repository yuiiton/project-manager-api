from sqlmodel import SQLModel, create_engine, Session
from contextlib import asynccontextmanager

engine = create_engine("sqlite:///./data/app.db", connect_args={"check_same_thread": False})

def create_tables():
    """Cria todas as tabelas definidas nos modelos SQLModel no banco de dados."""
    SQLModel.metadata.create_all(engine)

def get_session ():
    """Fornece uma sessão de banco de dados para injeção de dependência."""
    with Session(engine) as session:
        yield session

@asynccontextmanager
async def lifespan(app):
    """Gerencia o ciclo de vida da aplicação: cria as tabelas ao iniciar."""
    create_tables()
    yield