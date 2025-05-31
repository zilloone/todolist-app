from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from datetime import datetime, date, time
from sqlalchemy import Date, Column, Time



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


class TaskBase(SQLModel):
    title: str
    description: str | None = None
    event_date: date = Field(sa_column=Column(Date))
    event_time: time = Field(sa_column=Column(Time)) 



class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    owner_id: int | None = Field(default=None, foreign_key="user.id")


class TaskCreate(TaskBase):
    pass


class TaskPublic(TaskBase):
    id: int
    owner_id: int


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"



# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None



    
    