from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project.controller import project_router
from core.exceptions.commom_exceptions import AppError
from core.exceptions.handlers import app_error_handler

app = FastAPI(
    title="Project Manager API",
    description="""
    API REST para gerenciamento de projetos,
    desenvolvida com FastAPI e SQLModel.
    """,
)


app.include_router(project_router)

app.add_exception_handler(AppError, app_error_handler)
