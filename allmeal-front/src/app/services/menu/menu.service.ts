import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Menu } from '../../models/menu-admin/menu-model';  

@Injectable({
  providedIn: 'root'
})
export class MenuService {
  private apiUrl = 'http://127.0.0.1:8000/menus'; 

  constructor(private http: HttpClient) { }
  
  createMenu(menu: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/create/`, menu);
  }

  
  getMenus(): Observable<{ data: Menu[] }> {  
    return this.http.get<{ data: Menu[] }>(this.apiUrl);
  }  

  updateMenu(menuId: string, updatedData: any): Observable<any> {

    console.log('Datos recibidos para actualizar:', updatedData);


    
    const fullMenuData = {
      id: menuId,
      date: updatedData.date || new Date().toISOString().split('T')[0],
      starter: updatedData.starter || 'starter', 
      main_course: updatedData.main_course || 'main-course',
      dessert: updatedData.dessert || 'dessert'
    };

    return this.http.put(`${this.apiUrl}/${menuId}/update/`, fullMenuData);
}

  // Método para eliminar un menú
  deleteMenu(menuId: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${menuId}/delete/`);
  }
}
