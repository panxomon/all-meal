# Variables
PROJECT_NAME=allmeal
PYTHON=docker-compose exec web python
PIP=docker-compose exec web pip

# Instalar dependencias
install:
	docker-compose run --rm web pip install -r requirements.txt

# Iniciar el contenedor y construirlo si es necesario
up:
	docker-compose up --build -d

# Detener los contenedores
down:
	docker-compose down

# Ejecutar migraciones de la base de datos
migrate:
	$(PYTHON) manage.py migrate

# Crear nuevas migraciones
makemigrations:
	$(PYTHON) manage.py makemigrations

# Crear un superusuario para el admin de Django
createsuperuser:
	$(PYTHON) manage.py createsuperuser

# Correr el servidor de Django
run:
	$(PYTHON) manage.py runserver 0.0.0.0:8000

# Instalar nuevas dependencias y agregar al requirements.txt
freeze:
	$(PIP) freeze > requirements.txt

# Ejecutar pruebas
test:
	$(PYTHON) -m pytest

# Limpiar contenedores y volúmenes
clean:
	docker-compose down -v --rmi all

# Ver logs de los contenedores
logs:
	docker-compose logs -f
	
# create-superuser:
#     python create_superuser.py
