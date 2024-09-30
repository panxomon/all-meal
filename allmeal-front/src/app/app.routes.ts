import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { provideHttpClient } from '@angular/common/http';
import { Routes, provideRouter } from '@angular/router';
import { MenuAdminComponent } from './components/menu/admin/admin.component'; 
import { CreateMenuComponent } from './components/menu/create/create.component'; 

export const appRoutes: Routes = [
  {path: 'admin', component: MenuAdminComponent,},
  {path:'admin/create', component: CreateMenuComponent}  
];

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),  
    provideRouter(appRoutes)  
  ]
});