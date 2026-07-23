from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import lifespan
from controller.controller_project import project_router
from core.exceptions.commom_exceptions import ItemNotFoundError, BusinessRuleError, InvalidValueError
from core.exceptions.handlers import item_not_found_handler, business_rule_error_handler, value_error_handler

app = FastAPI(
    title="Project Manager API",
    description="""
    API REST para gerenciamento de projetos,
    desenvolvida com FastAPI e SQLModel.
    """,
    lifespan=lifespan
)


app.include_router(project_router)

app.add_exception_handler(ItemNotFoundError, item_not_found_handler)
app.add_exception_handler(BusinessRuleError, business_rule_error_handler)
app.add_exception_handler(InvalidValueError, value_error_handler)