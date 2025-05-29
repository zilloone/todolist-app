from app.api.deps import SessionDep
from app.models import User
from sqlmodel import select
from app.core.security import verify_password


def get_user(username: str, session: SessionDep):
    statement = select(User).where(User.email == username)
    user = session.exec(statement).one()
    return user


def authenticate_user(username: str, password: str, session: SessionDep):
    db_user = get_user(username=username, session=session)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
    