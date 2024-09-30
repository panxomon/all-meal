from .service import MenuListService
from commons.cqrs.query import QueryHandler
from .query import RetrieveAllMenu

class MenuListHandler(QueryHandler[RetrieveAllMenu, str]):
    def __init__(self, menu_list_service: MenuListService):
        self.menu_list_service =  menu_list_service

    def handle(self, qry: RetrieveAllMenu) -> tuple:        
               
        return  self.menu_list_service.get_all_menus()
