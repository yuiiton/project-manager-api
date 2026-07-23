from fastapi import Request, status
from fastapi.responses import JSONResponse
from core.exceptions.commom_exceptions import ItemNotFoundError, BusinessRuleError, InvalidValueError

async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    """Manipula exceções ItemNotFoundError retornando resposta 404."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)}
    )


async def business_rule_error_handler(request: Request, exc: BusinessRuleError):
    """Manipula exceções BusinessRuleError retornando resposta 400."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )

async def value_error_handler(request: Request, exc: InvalidValueError):
    """Manipula exceções InvalidValueError retornando resposta 400."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )