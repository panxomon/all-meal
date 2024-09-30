# Repository
from order_management.menu.infrastructure.repository.menu_repository import MenuRepository

#create menu 
from order_management.menu.application.create.service import CreateMenuService
from order_management.menu.application.create.handler import CreateMenuCommandHandler

#listar menus
from order_management.menu.application.list.service import MenuListService
from order_management.menu.application.list.handler import MenuListHandler

#eliminar menu
from order_management.menu.application.remove.service import MenuRemoveService
from order_management.menu.application.remove.handler import MenuRemoveCommandHandler

#actualizar menu
from order_management.menu.application.update.service import MenuUpdateService
from order_management.menu.application.update.handler import MenuUpdateCommandHandler

from order_management.menu.application.application import MenuApp, Commands, Queries


class Bootstrap:
    def __init__(self):
         # Repositorio
        self.menu_repository = MenuRepository()

        # Servicios y Handlers

        # Crear menú
        self.create_menu_service = CreateMenuService(self.menu_repository)
        self.create_menu_handler = CreateMenuCommandHandler(self.create_menu_service)

        # Listar menús
        self.menu_list_service = MenuListService(self.menu_repository)
        self.menu_list_handler = MenuListHandler(self.menu_list_service)

        # Eliminar menú
        self.menu_remove_service = MenuRemoveService(self.menu_repository)
        self.menu_remove_handler = MenuRemoveCommandHandler(self.menu_remove_service)

        # Actualizar menú
        self.menu_update_service = MenuUpdateService(self.menu_repository)
        self.menu_update_handler = MenuUpdateCommandHandler(self.menu_update_service)

        # Inicializar los comandos y queries
        self.commands = Commands()
        self.queries = Queries()

        # Pasar handlers a los comandos y queries
        self.commands.create_menu = self.create_menu_handler
        self.commands.update_menu = self.menu_update_handler
        self.commands.remove_menu = self.menu_remove_handler
        self.queries.list_all_menu = self.menu_list_handler

        # Instanciar la aplicación con comandos y queries
        self.menu_app = MenuApp(self.commands, self.queries)
        

def load_components():    
    return Bootstrap()

