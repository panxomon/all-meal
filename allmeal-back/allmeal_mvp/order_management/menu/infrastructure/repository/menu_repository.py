import uuid
from ...domain.models.menu import Menu
from ..persistence.postgresql import MenuPersistence

class MenuRepository:
    
    def save(self, menu: Menu) -> tuple: 
        try:           
            MenuPersistence.save(menu)  # Llama al método estático directamente
            return menu, None 
        except Exception as e:
            return None, f"Error al guardar el menú: {e}" 
        
    def get(self, menu_id: uuid.UUID) -> tuple:
        """
        Obtiene un menú con el ID dado.
        :param menu_id: El ID del menú a obtener.
        :return: El menú encontrado y None si no hay error.
        """
        try:
            menu = Menu.objects.get(id=menu_id)
            return menu, None
        except Menu.DoesNotExist:
            return None, f"Menu con ID {menu_id} no existe"
        except Exception as e:
            return None, f"Error al obtener el menú: {e}"
        
    def get_all(self) -> tuple:
        """
        Obtiene todos los menús desde la base de datos.
        """
        try:
            menus = MenuPersistence.get_all()  # Llama al método estático directamente
            return menus, None
        except Exception as e:
            return None, f"Error al obtener los menús: {e}"
      
    def remove(self, menu_id: uuid.UUID) -> tuple:
        """
        Elimina un menú con el ID dado del repositorio.
        :param menu_id: El ID del menú a eliminar.
        :return: El menú eliminado o un mensaje de error.
        """
        try:
            menu = Menu.objects.get(id=menu_id)
            menu.delete()
            return menu, None  # Retorna el menú eliminado y None como error
        except Menu.DoesNotExist:
            return None, f"Menu con ID {menu_id} no existe"
        except Exception as e:
            return None, f"Error al eliminar el menú: {e}"
