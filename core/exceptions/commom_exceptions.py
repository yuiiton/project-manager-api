class BusinessRuleError(Exception):
    """Erros gerais de regra de negócio"""
    pass

class ItemNotFoundError(Exception):
    """Item não encontrado no banco"""
    pass

class InvalidValueError(Exception):
    """Erros gerais de valores incorretos."""
    pass