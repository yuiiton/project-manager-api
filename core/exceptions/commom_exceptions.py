class AppError(Exception):
    """Handler génerico dos erros da aplicação"""
    status_code = 400
    pass

class BusinessRuleError(AppError):
    """Erros gerais de regra de negócio"""
    status_code = 400
    pass

class ItemNotFoundError(AppError):
    """Item não encontrado no banco"""
    status_code = 404
    pass

class InvalidValueError(AppError):
    """Erros gerais de valores incorretos."""
    status_code=400
    pass

