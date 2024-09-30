import uuid

class MenuRemoveCommand:
    def __init__(self, menu_id: uuid.UUID):
        """
        Comando para eliminar un menú basado en su ID.
        """
        self.menu_id = menu_id
