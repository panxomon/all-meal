// create-menu.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { MenuService } from '../../../services/menu/menu.service'; 
import { CommonModule } from '@angular/common';
import { AbstractControl, ValidationErrors } from '@angular/forms';
import { Router } from '@angular/router'; 


function futureDateValidator(control: AbstractControl): ValidationErrors | null {
  const selectedDate = new Date(control.value);
  const currentDate = new Date();
  return selectedDate < currentDate ? { pastDate: true } : null;
}

  
@Component({
  standalone: true, 
  selector: 'app-create-menu',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css'],
  imports: [ReactiveFormsModule, CommonModule],
})
export class CreateMenuComponent  {
  menuForm: FormGroup;

  constructor(private fb: FormBuilder, private menuService: MenuService, private router: Router) {
    this.menuForm = this.fb.group({
      date: ['', [Validators.required, futureDateValidator]],
      starter: ['', Validators.required],
      main_course: ['', Validators.required],
      dessert: ['', Validators.required],
    });
  } 


  onSubmit(): void {
    if (this.menuForm.valid) {
      this.menuService.createMenu(this.menuForm.value).subscribe({
        next: (response) => {
          console.log('Menú creado con éxito:', response);
          this.router.navigate(['/admin']);
        },
        error: (error) => {
          console.error('Error al crear el menú:', error);
        },
      });
    } else {
      console.log('El formulario no es válido');
    }
  }

}
