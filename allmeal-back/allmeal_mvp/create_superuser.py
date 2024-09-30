import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'allmeal_mvp.settings') 
django.setup()

if not User.objects.filter(username='admin').exists():  
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',  
        password='admin123'  
    )
    print("Superusuario creado.")
else:
    print("El superusuario ya existe.")
