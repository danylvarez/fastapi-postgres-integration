import pytest
from app.models.user_models import User


def test_user_model_attributes():
    user = User()
    assert hasattr(user, "id")
    assert hasattr(user, "first_name")
    assert hasattr(user, "last_name")
    assert hasattr(user, "company_name")
    assert hasattr(user, "address")
    assert hasattr(user, "city")
    assert hasattr(user, "state")
    assert hasattr(user, "zip")
    assert hasattr(user, "phone1")
    assert hasattr(user, "phone2")
    assert hasattr(user, "email")
    assert hasattr(user, "department")


def test_user_model_table_name():
    assert User.Meta.tablename == "users"
