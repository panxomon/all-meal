# infrastructure/persistence/postgresql.py
from ...domain.models.menu import Menu

class MenuPersistence:
    @staticmethod
    def save(menu: Menu):
        # Implementa la lógica para guardar en la base de datos
        menu.save()  # Asumiendo que Menu tiene un método save() que interactúa con PostgreSQL

    @staticmethod
    def get_all() -> list:
        # Implementa la lógica para obtener todos los menús desde la base de datos
        return list(Menu.objects.all())  # Esto debería retornar una lista de objetos Menu
