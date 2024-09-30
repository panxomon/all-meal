from commons.cqrs.command import CommandWithResultHandler
from ...domain.menu import Menu
from .command import MenuUpdateCommand
from .service import MenuUpdateService

class MenuUpdateCommandHandler(CommandWithResultHandler[MenuUpdateCommand, Menu]):
    def __init__(self, update_service: MenuUpdateService):
        self.menu_update_service = update_service

    def handle(self, cmd: MenuUpdateCommand) -> tuple:
        return self.menu_update_service.execute(cmd.menu_id, cmd.menu_data)
