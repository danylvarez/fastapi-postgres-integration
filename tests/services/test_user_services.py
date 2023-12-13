import pytest
from app.db import database
from app.models.user_models import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.services.user_services import (
    create_new_user,
    fetch_users,
    update_user,
    delete_user,
)


@pytest.fixture(scope="module")
async def test_db():
    await database.connect()
    yield

    await database.disconnect()


@pytest.mark.asyncio
async def test_create_new_user(test_db):
    user_details = UserCreate(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        company_name="Test Company",
        address="Test Address",
        city="Test City",
        state="TS",
        zip="12345",
        phone1="123-456-7890",
        phone2="098-765-4321",
        department="Testing",
    )
    new_user = await create_new_user(user_details)
    assert new_user.id is not None
    assert new_user.first_name == "Test"


@pytest.mark.asyncio
async def test_fetch_users(test_db):
    users = await fetch_users(page_number=1, page_size=10)
    assert users is not None
    assert len(users) >= 0


@pytest.mark.asyncio
async def test_update_user(test_db):
    user_update_data = UserUpdate(first_name="Updated")
    updated_user = await update_user(2, user_update_data)
    assert updated_user.first_name == "Updated"


@pytest.mark.asyncio
async def test_delete_user(test_db):
    delete_response = await delete_user(2)
    assert delete_response == {"detail": "User successfully deleted"}

    with pytest.raises(Exception):
        await fetch_users(user_id=2)
