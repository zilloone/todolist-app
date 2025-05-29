from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr



class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    full_name: str | None = Field(default=None, max_length=255)


class UserCreate(UserBase):
    username: str = Field(unique=True)
    password: str = Field(max_length=60)

    

class UserRegister(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    full_name: str | None = Field(default=None, max_length=255)
    username: str = Field(unique=True)
    password: str = Field(max_length=60)



class UserPublic(UserBase):
    id: int
    username: str = Field(unique=True)



class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    hashed_password: str = Field(max_length=60)


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"



# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None



    
    