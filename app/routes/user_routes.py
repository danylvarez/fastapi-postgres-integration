from typing import Optional
from fastapi import Query, APIRouter


from ..schemas.user_schemas import UserUpdate, UserCreate
from ..services import user_services


router = APIRouter()


# Endpoint to fetch users. Can filter by user_id.
@router.get("/users/")
async def fetch_users(
    user_id: Optional[int] = None,
    page_number: int = 1,
    page_size: int = Query(10, alias="limit"),
):
    return await user_services.fetch_users(
        user_id=user_id, page_number=page_number, page_size=page_size
    )


# Endpoint to create a new user
@router.post("/users/")
async def create_new_user(user_details: UserCreate):
    return await user_services.create_new_user(user_details=user_details)


# Endpoint to update an existing user
@router.put("/users/{user_id}")
async def update_user(user_id: int, user_update_data: UserUpdate):
    return await user_services.update_user(
        user_id=user_id, user_update_data=user_update_data
    )


# Endpoint to delete a user
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return await user_services.delete_user(user_id=user_id)
