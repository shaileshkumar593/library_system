Part	Folder	Files
✅ Part 1	db	database.py, base.py
Part 2	models	book.py, member.py, borrowing.py
Part 3	schemas	Pydantic models
Part 4	repository	Database CRUD layer
Part 5	services	Business logic
Part 6	api	FastAPI routes
Part 7	core	Config & Exceptions
Part 8	dependencies	Dependency Injection
Part 9	main.py	Application entry point
Part 10	Alembic	Migration setup
Part 11	Docker	Dockerfile & docker-compose
Part 12	Tests	Unit & Integration tests
Part 13	README	Complete documentation



# Library Management System

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker

---

## Start Database

docker compose up postgres

---

## Run Migration

alembic upgrade head

---

## Run API

uvicorn app.main:app --reload

---

## Swagger

http://localhost:8000/docs

---

## API Endpoints

POST /books

GET /books

PUT /books/{id}

DELETE /books/{id}

POST /members

GET /members

POST /borrowings

POST /borrowings/return

GET /borrowings/member/{id}
