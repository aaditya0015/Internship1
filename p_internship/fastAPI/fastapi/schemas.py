from pydantic import BaseModel, EmailStr

# Schema used when creating a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr


# Schema used when returning user data
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True