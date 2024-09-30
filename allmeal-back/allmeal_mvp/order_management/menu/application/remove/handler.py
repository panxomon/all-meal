from commons.cqrs.command import CommandWithResultHandler
from .command import MenuRemoveCommand
from .service import MenuRemoveService

class MenuRemoveCommandHandler(CommandWithResultHandler[MenuRemoveCommand, str]):
    def __init__(self, menu_remove_service: MenuRemoveService):
        self.menu_remove_service = menu_remove_service

    def handle(self, cmd: MenuRemoveCommand) -> tuple:
        """
        Maneja el comando para eliminar un menú.
        :param cmd: El comando que contiene el ID del menú a eliminar.
        :return: Mensaje de éxito o error en una tupla.
        """
        return self.menu_remove_service.execute(cmd.menu_id)
