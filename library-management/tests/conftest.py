import os

import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.database import Base
from app.db.database import get_db


#########################################################################
# Test Database
#########################################################################

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "sqlite:///./test.db"
)

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)


#########################################################################
# Create tables once
#########################################################################

Base.metadata.create_all(bind=engine)


#########################################################################
# Override Dependency
#########################################################################

def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


#########################################################################
# Test Client
#########################################################################

@pytest.fixture(scope="session")
def client():

    with TestClient(app) as client:
        yield client


#########################################################################
# Database Session
#########################################################################

@pytest.fixture()
def db():

    connection = engine.connect()

    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()

    transaction.rollback()

    connection.close()


#########################################################################
# Clean Database
#########################################################################

@pytest.fixture(autouse=True)
def clean_tables(db):

    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())

    db.commit()

    yield