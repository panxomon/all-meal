# AllMeal

![Angular](https://img.shields.io/badge/Angular-18-red)
![Docker](https://img.shields.io/badge/Docker-v20.10.8-blue)
![Python](https://img.shields.io/badge/Python-3.x-brightgreen)
![Django](https://img.shields.io/badge/Django-3.x-blueviolet)

# AllMeal

AllMeal es una empresa dedicada a la entrega de comidas por delivery a oficinas. Actualmente, gestionan los pedidos mediante WhatsApp, enviando los menús a los empleados de las empresas inscritas al servicio. Los empleados responden con sus pedidos, que luego son anotados manualmente por un empleado de AllMeal, lo que ha generado problemas de confusión, retrasos y errores en la contabilidad.

## Contexto

La empresa AllMeal ha decidido avanzar en sus procesos de ventas y fidelización de clientes construyendo un software para poder hacer pedidos online. Este es un MVP (Producto Mínimo Viable) que se implementará inicialmente en una sola empresa, cuyo principal canal de comunicación será Slack. 

#### Funcionalidades

- Crear y administrar menús.
- Actualizar valores de los menús con un doble clic.
- Eliminar menús con un clic en el icono ❌.
- Integración con Slack para enviar los menús a los empleados.

### Estructura del Proyecto

```plaintext
allmeal-back/    # Backend (Django)
allmeal-front/   # Frontend (Angular)
```

### Requisitos Previos
```plaintext
- Python 3.x
- Node.js (versión 14.x o superior)
- npm (incluido con Node.js)
- Angular CLI (versión 18.x)
- Virtualenv para el entorno de Python (opcional)
```

### Instalación de Angular CLI
```
npm install -g @angular/cli@18
```


## Instrucciones para Levantar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/panxomon/all-meal/tree/main
   cd allmeal

2. Asegúrate de tener Docker y Docker Compose instalados.

## Configuración del Entorno

Antes de ejecutar la aplicación, debes configurar el archivo de entorno. Para hacerlo, sigue estos pasos:

1. crea un archivo de environment:

   ```bash
   make env

2. Levanta los servicios:

    ```bash    
    make up
    ```

4. Accede a:
    ``` 
    Backend: http://localhost:8000
    Frontend: http://localhost:4200
    ```
5. Para detener los servicios:
    ```
    make down    
    ```

### Instrucciones para Probar la API con Postman
1. Abre Postman.

2. Importa la colección se encuentra en /allmeal-back/postman_collection

Configura el entorno para que apunte a:

    Backend: http://localhost:8000

