# schemas/user_schema.py

from pydantic import BaseModel, EmailStr, constr
from typing import Optional


class UserCreate(BaseModel):
    first_name: constr(max_length=50)
    last_name: constr(max_length=50)
    company_name: constr(max_length=100)
    address: constr(max_length=100)
    city: constr(max_length=50)
    state: constr(max_length=2)
    zip: constr(max_length=10)
    phone1: constr(max_length=20)
    phone2: constr(max_length=20)
    email: constr(max_length=100)
    department: constr(max_length=50)


class UserUpdate(BaseModel):
    first_name: Optional[constr(max_length=50)] = None
    last_name: Optional[constr(max_length=50)] = None
    company_name: Optional[constr(max_length=100)] = None
    address: Optional[constr(max_length=100)] = None
    city: Optional[constr(max_length=50)] = None
    state: Optional[constr(max_length=2)] = None
    zip: Optional[constr(max_length=10)] = None
    phone1: Optional[constr(max_length=20)] = None
    phone2: Optional[constr(max_length=20)] = None
    email: Optional[constr(max_length=100)] = None
    department: Optional[constr(max_length=50)] = None


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    company_name: str
    address: str
    city: str
    state: str
    zip: str
    phone1: str
    phone2: str
    email: str
    department: str
