from ...domain.models.menu import Menu

class MenuPersistence:
    @staticmethod
    def save(menu: Menu):       
        menu.save() 

    @staticmethod
    def get_all() -> list:     
        return list(Menu.objects.all()) 
