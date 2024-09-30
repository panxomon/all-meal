import uuid
from typing import Optional

class MenuRemoveService:
    def __init__(self, menu_repository):
        """
        Inicializa el servicio con el repositorio de menú.
        """
        self.menu_repository = menu_repository

    def execute(self, menu_id: uuid.UUID) -> Optional[str]:
        """
        Elimina un menú existente en el repositorio.

        :param menu_id: El ID del menú a eliminar.
        :return: Un mensaje de éxito o None si ocurre un error.
        """
        try:
            # Intentar eliminar el menú con el ID proporcionado
            menu, error = self.menu_repository.remove(menu_id)
            
            if error:
                return None, f"Error al eliminar el menú: {error}"
            
            return f"Menu {menu_id} eliminado exitosamente", None
        except Exception as e:
            # Manejar cualquier error que ocurra
            return None, f"Error al eliminar el menú: {e}"
