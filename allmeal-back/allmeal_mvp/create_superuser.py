import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'allmeal_mvp.settings')  # Reemplaza 'allmeal_mvp' con el nombre de tu proyecto
django.setup()

# Verificar si el superusuario ya existe
if not User.objects.filter(username='admin').exists():  # Cambia 'admin' por el nombre de usuario que desees
    User.objects.create_superuser(
        username='admin',  # Cambia 'admin' por tu nombre de usuario
        email='admin@example.com',  # Cambia el correo si es necesario
        password='admin123'  # Cambia 'admin123' por tu contraseña
    )
    print("Superusuario creado.")
else:
    print("El superusuario ya existe.")
