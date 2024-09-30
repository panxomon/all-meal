from abc import ABC, abstractmethod
from typing import TypeVar, Generic


Q = TypeVar('Q')  # Consulta
R = TypeVar('R')  # Resultado de consulta

class QueryHandler(ABC, Generic[Q, R]):
    @abstractmethod
    def handle(self, query: Q) -> R:
        pass
