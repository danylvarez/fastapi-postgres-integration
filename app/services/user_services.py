from typing import Optional
from fastapi import HTTPException, Query


from ..db import database
from ..models.user_models import User
from ..schemas.user_schemas import UserCreate, UserUpdate


async def fetch_users(
    user_id: Optional[int] = None,
    page_number: int = 1,
    page_size: int = Query(10, alias="limit"),
):
    if user_id is not None:
        async with database:
            # Fetch a single user by ID
            user_record = await User.objects.get_or_none(id=user_id)
            if user_record is None:
                # Raise an exception if the user is not found
                raise HTTPException(status_code=404, detail="User not found")
            return user_record
    else:
        # Pagination logic for listing users
        offset = (page_number - 1) * page_size
        async with database:
            # Fetch a list of users with pagination
            user_list = await User.objects.limit(page_size).offset(offset).all()
            return user_list


async def create_new_user(user_details: UserCreate):
    async with database:
        # Create a new user record in the database
        new_user = await User.objects.create(**user_details.dict())
        return new_user


async def update_user(user_id: int, user_update_data: UserUpdate):
    async with database:
        # Check if the user exists
        existing_user = await User.objects.get_or_none(id=user_id)
        if existing_user is None:
            # Raise an exception if the user is not found
            raise HTTPException(status_code=404, detail="User not found")

        # Prepare the data for update
        update_data = user_update_data.dict(exclude_unset=True)

        # Update the existing user
        updated_user = await existing_user.update(**update_data)

        return updated_user


async def delete_user(user_id: int):
    async with database:
        # Check if the user exists
        existing_user = await User.objects.get_or_none(id=user_id)
        if existing_user is None:
            # Raise an exception if the user is not found
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        await existing_user.delete()

        return {"detail": "User successfully deleted"}
