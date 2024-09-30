from ...domain.models import Menu
from typing import List

class MenuListService:
    def __init__(self, menu_repository):
        """
        Inicializa el servicio con el repositorio de menú.
        """
        self.menu_repository = menu_repository

    def get_all_menus(self) -> List[Menu]:
        """
        Obtiene todos los menús almacenados en el repositorio.
        """
        try:
            menus, error = self.menu_repository.get_all()
            if error:
                return None, error
            return menus, None
        except Exception as e:
            return None, f"Error al obtener los menús: {e}"