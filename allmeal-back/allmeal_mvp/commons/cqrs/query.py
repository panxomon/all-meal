from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Definimos los tipos genéricos
Q = TypeVar('Q')  # Consulta
R = TypeVar('R')  # Resultado de consulta

class QueryHandler(ABC, Generic[Q, R]):
    @abstractmethod
    def handle(self, query: Q) -> R:
        """Maneja una consulta y devuelve un resultado."""
        pass

# # Ejemplo de una consulta concreta
# class GetMenuQuery:
#     def __init__(self, menu_id):
#         self.menu_id = menu_id

# # Implementación del manejador de consultas
# class GetMenuQueryHandler(QueryHandler[GetMenuQuery, str]):
#     def handle(self, query: GetMenuQuery) -> str:
#         # Lógica para obtener un menú
#         return f"Details of menu with ID '{query.menu_id}'"
