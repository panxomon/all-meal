from commons.cqrs.command import CommandWithResultHandler
from .command import CreateMenuCommand
from .service import CreateMenuService

class CreateMenuCommandHandler(CommandWithResultHandler[CreateMenuCommand, str]):
    def __init__(self, create_menu_service: CreateMenuService):
        self.create_menu_service = create_menu_service

    def handle(self, cmd: CreateMenuCommand) -> tuple:        
        return self.create_menu_service.execute(cmd.menu)
