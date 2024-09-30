from ..application.create.command import CreateMenuCommand
from ..application.list.query import  RetrieveAllMenu
from ..application.remove.command import MenuRemoveCommand
from ..application.update.command import MenuUpdateCommand



class MenuApp:
    def __init__(self, commands, queries):
        self.commands = commands
        self.queries = queries

def new_menu_app(commands, queries):
    return MenuApp(commands, queries)

class Commands:
    def __init__(self):
        self.create_menu = CreateMenuCommand
        self.update_menu = MenuUpdateCommand
        self.remove_menu = MenuRemoveCommand

class Queries:
    def __init__(self) -> None:
        self.list_all_menu = RetrieveAllMenu
