from app.core import security
from app.api.deps import SECRET_KEY, SessionDep, get_current_user
from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.core import security
from app import crud
from app.models import Token



router = APIRouter(prefix="/auth", tags=["login"])

@router.post("/login/access-token")
def access_token_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep
):
    user = crud.authenticate_user(
        username=form_data.username, password=form_data.password, session=session
    )
    print(user.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    access_token_expire = timedelta(minutes=3)
    return Token(
        access_token=security.create_access_token(
            subject=user.username, expires_delta=access_token_expire
        )
    )
    