import uuid

from ...domain.menu import Menu

class MenuUpdateCommand:
    def __init__(self, menu_id: uuid.UUID, menu_data: dict):
        self.menu_id = menu_id
        self.menu_data = menu_data
