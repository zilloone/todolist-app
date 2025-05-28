from sqlmodel import Session
from app.core.db import engine
from typing import Annotated
from fastapi import Depends



def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]