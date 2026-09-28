from fastapi import Request
from fastapi.responses import JSONResponse
from core.exceptions.commom_exceptions import AppError

async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": str(exc)}
    )