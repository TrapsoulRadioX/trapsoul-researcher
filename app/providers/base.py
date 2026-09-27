from abc import ABC, abstractmethod
from app.models import ResearchRequest, TrendItem

class Provider(ABC):
    name = "base"
    @abstractmethod
    async def search(self, request: ResearchRequest) -> list[TrendItem]: ...
