import uuid

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from commons.bootstrap.bootstrap import load_components
from ...application.create.command import CreateMenuCommand
from ...application.update.command import MenuUpdateCommand
from ...application.remove.command import MenuRemoveCommand
from ...application.list.query import RetrieveAllMenu

components = load_components()

@api_view(['GET'])
def get_all_menus(request):
    query = RetrieveAllMenu()
    result, error = components.queries.list_all_menu.handle(query)    

    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

    if not result:
        return Response({"error": "No menus found"}, status=status.HTTP_404_NOT_FOUND)
    
    serialized_menus = [menu.to_dict() for menu in result]
    
    return Response({"data": serialized_menus}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_menu(request):    
    menu_data = {        
        "date": request.data.get("date"),
        "starter": request.data.get("starter"),
        "main_course": request.data.get("main_course"),
        "dessert": request.data.get("dessert")
    }
    
    command = CreateMenuCommand(menu=menu_data)
    
    result, error = components.commands.create_menu.handle(command)
    
    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"data": result}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_menu(request, menu_id: uuid.UUID):
    menu_data = {
        "date": request.data.get("date"),
        "starter": request.data.get("starter"),
        "main_course": request.data.get("main_course"),
        "dessert": request.data.get("dessert")
    }   
    
    command = MenuUpdateCommand(menu_id=menu_id, menu_data=menu_data)
    result, error = components.commands.update_menu.handle(command)

    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

    if result is None:
        return Response({"error": "No se pudo actualizar el menú"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"data": result.to_dict()}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove_menu(request, menu_id: uuid.UUID):  
    command = MenuRemoveCommand(menu_id=menu_id)
    
    # Ejecutar el handler para eliminar el menú
    result, error = components.commands.remove_menu.handle(command)

    if error:
        return Response({"error": error}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": result}, status=status.HTTP_204_NO_CONTENT)
