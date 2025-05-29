from sqlmodel import Session
from app.core.db import engine
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.core.security import ALGORITHM, SECRET_KEY
import jwt
from app.models import TokenPayload, User
from jwt.exceptions import InvalidTokenError



reuseable_oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login/access-token")


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]



def get_current_user(token: Annotated[str, Depends(reuseable_oauth2)], session: SessionDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found") 
    return user  

CurrentUser = Annotated[User, Depends(get_current_user)]