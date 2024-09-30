"""
URL configuration for allmeal_mvp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from order_management.menu.infrastructure.http.controller import (
    get_all_menus, create_menu, update_menu, remove_menu
)

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', RedirectView.as_view(url='/menus/', permanent=True)),  # Redirige la raíz a /menus/
    path('menus/', get_all_menus, name='get_all_menus'),  # GET: listar menús
    path('menus/create/', create_menu, name='create_menu'),  # POST: crear menú
    path('menus/<uuid:menu_id>/update/', update_menu, name='update_menu'),  # PUT: actualizar menú
    path('menus/<uuid:menu_id>/delete/', remove_menu, name='remove_menu'),  # DELETE: eliminar menú
]

