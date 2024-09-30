import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MenuService } from '../../../services/menu/menu.service';
import { Menu } from '../../../models/menu-admin/menu-model';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

// Define un tipo para los campos editables
type EditableField = 'starter' | 'main_course' | 'dessert';

@Component({
  standalone: true,
  selector: 'app-menu-admin',
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class MenuAdminComponent implements OnInit {
  menus: Menu[] = [];
  editedValue: string | null = null;
  editingMenuId: string | null = null;
  editingField: string | null = null;

  constructor(private menuService: MenuService) { }

  isEditing(menuId: string, field: string): boolean {
    return this.editingMenuId === menuId && this.editingField === field;
  }

  editMenuField(menu: Menu, field: EditableField): void {
    this.editedValue = menu[field]; // Asigna el valor a editar
    this.editingMenuId = menu.id;
    this.editingField = field;
  }

  stopEditing(): void {
    this.editedValue = null;
    this.editingMenuId = null;
    this.editingField = null;
  }

  ngOnInit(): void {
    this.loadMenus();
  }

  loadMenus(): void {
    this.menuService.getMenus().subscribe({
      next: (response) => {
        this.menus = response.data;  // Asegúrate de que 'response.data' contenga los menús
      },
      error: (err) => {
        console.error('Error al obtener menús', err);
      }
    });
  }

  removeMenu(menuId: string): void {
    this.menuService.deleteMenu(menuId).subscribe({
      next: () => {
        this.menus = this.menus.filter(menu => menu.id !== menuId);
        console.log('Menú eliminado con éxito');
      },
      error: (err) => {
        console.error('Error al eliminar menú', err);
      }
    });
  }

  updateMenu(menuId: string, field: EditableField, newValue: string): void {
    const menuToUpdate = this.menus.find(menu => menu.id === menuId);
    if (menuToUpdate) {
        // Crea un objeto con todos los campos del menú
        const updatedData = {
            id: menuToUpdate.id,
            date: menuToUpdate.date, // Mantén la fecha actual
            starter: field === 'starter' ? newValue : menuToUpdate.starter,
            main_course: field === 'main_course' ? newValue : menuToUpdate.main_course,
            dessert: field === 'dessert' ? newValue : menuToUpdate.dessert
        };

        this.menuService.updateMenu(menuId, updatedData).subscribe({
            next: (response) => {
                console.log('Menú actualizado con éxito:', response);                
                this.menus[this.menus.findIndex(menu => menu.id === menuId)] = updatedData;
                this.stopEditing();
            },
            error: (error) => {
                console.error('Error al actualizar el menú:', error);
            },
        });
    }
}

}
