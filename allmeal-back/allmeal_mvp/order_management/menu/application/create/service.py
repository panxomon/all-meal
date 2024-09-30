import uuid

from ...domain.models import Menu
from ...infrastructure.repository.menu_repository import MenuPersistence

class CreateMenuService:
    def __init__(self, menu_repository):
        self.menu_repository = menu_repository

    def execute(self,  menu_data: dict) -> tuple:
        try:
             
            menu_id = uuid.uuid4()
            
            nuevo_menu = Menu(
                id=menu_id,
                date=menu_data['date'] , 
                starter=menu_data['starter'], 
                main_course=menu_data['main_course'], 
                dessert=menu_data['dessert']
            )
            
            result, error = self.menu_repository.save(nuevo_menu)  

            if error:
                return None, error
            
            return {
                "success": True,
                "id": str(result.id),  
                "date": result.date,
                "starter": result.starter,
                "main_course": result.main_course,
                "dessert": result.dessert,
            }, None       
            
        except Exception as e:
            return None, f"Error al crear el menú: {e}"
