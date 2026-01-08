from pydantic import BaseModel, EmailStr, constr
from typing import Optional

# what client sends to create user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8, max_length=256)


# what API returns to client
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

# Update User 
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    class Config:
        orm_mode = True



