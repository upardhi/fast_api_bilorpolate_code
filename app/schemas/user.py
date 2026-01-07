from pydantic import BaseModel, EmailStr
from typing import Optional

# what client sends to create user
class UserCreate(BaseModel):
    name: str
    email: EmailStr


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

