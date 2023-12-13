import pytest
import sqlalchemy
import databases
from app.db import database, metadata, engine
from app.config import settings


def test_database_connection():
    assert isinstance(database, databases.Database)
    assert database.url == settings.db_url


def test_sqlalchemy_engine_creation():
    assert isinstance(engine, sqlalchemy.engine.base.Engine)
    assert str(engine.url) == settings.db_url


def test_sqlalchemy_metadata():
    assert isinstance(metadata, sqlalchemy.MetaData)
