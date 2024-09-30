PROJECT_NAME=allmeal
PYTHON=docker-compose exec web python
PIP=docker-compose exec web pip

install:
	docker-compose run --rm web pip install -r requirements.txt

up:
	docker-compose up --build -d

down:
	docker-compose down

migrate:
	$(PYTHON) manage.py migrate

makemigrations:
	$(PYTHON) manage.py makemigrations

#TODO: revisar
createsuperuser:
	$(PYTHON) manage.py createsuperuser

run:
	$(PYTHON) manage.py runserver 0.0.0.0:8000

freeze:
	$(PIP) freeze > requirements.txt

test:
	$(PYTHON) -m pytest

clean:
	docker-compose down -v --rmi all

logs:
	docker-compose logs -f
	
