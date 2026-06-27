
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
