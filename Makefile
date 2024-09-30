.PHONY: up down

up:
	docker-compose up --build

down:
	docker-compose down

env:
	cp ./allmeal-back/allmeal_mvp/.env.example ./allmeal-back/allmeal_mvp/.env

