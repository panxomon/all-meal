from typing import Optional
import uuid
from ...domain.models.menu import Menu

class MenuUpdateService:
    def __init__(self, menu_repository):
        """
        Inicializa el servicio con el repositorio de menú.
        """
        self.menu_repository = menu_repository

    def execute(self, menu_id: uuid.UUID, menu_data: dict) -> tuple:
        """
        Actualiza un menú existente y lo guarda en el repositorio.

        :param menu_id: El ID del menú a actualizar.
        :param menu_data: Un diccionario con los nuevos datos del menú.
        :return: El objeto Menu actualizado o None si ocurre un error.
        """
        try:
            # Obtener el menú existente
            menu, error = self.menu_repository.get(menu_id)
            if error:
                print(f"Error al obtener el menú: {error}")
                return None

             # Actualizar los campos del menú
            menu.starter = menu_data.get("starter", menu.starter)
            menu.main_course = menu_data.get("main_course", menu.main_course)
            menu.dessert = menu_data.get("dessert", menu.dessert)
            menu.date = menu_data.get("date", menu.date)

            print(f"MENU CREADO : {menu}")

            # Guardar el menú actualizado en el repositorio
            self.menu_repository.save(menu)

            # Retornar el menú actualizado y None como error
            return menu, None
        except Exception as e:
            print(f"Error al actualizar el menú: {e}")
            return None, f"Error al actualizar el menú: {e}"
