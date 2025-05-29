from fastapi import APIRouter, Depends, HTTPException
from app import crud
from app.api.deps import SessionDep
from app.models import (
    User, UserCreate, UserPublic
)
from app.api.deps import CurrentUser
from typing import Any


router = APIRouter(prefix="/users", tags=["users"])



@router.post("/create-user")
def create_new_user(user_in: UserCreate, session: SessionDep):
    user = crud.get_user(username=user_in.username, session=session)
    if user:
        raise HTTPException(
            status_code=400, 
            detail="User with this email already exist"
        )
    user = crud.create_user(user_create=user_in, session=session)
    return user


@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> Any:
    """
    Get current user.
    """
    return current_user
