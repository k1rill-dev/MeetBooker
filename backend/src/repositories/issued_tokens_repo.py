from src.adapters.models import IssuedTokens
from src.adapters.repository import SQLAlchemyRepository


class IssuedTokensRepository(SQLAlchemyRepository):
    model = IssuedTokens
