export PYTHONPATH=.

run:
	uvicorn src.api.api:app --reload

migration:
	alembic upgrade head

install:
	pip install -r requirements.txt

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down