from app.api.deps import SessionDep
from app.models import User, UserCreate
from sqlmodel import select
from app.core.security import verify_password, get_password_hash


def get_user(username: str, session: SessionDep):
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    return user


def authenticate_user(username: str, password: str, session: SessionDep):
    db_user = get_user(username=username, session=session)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
    

def create_user(user_create: UserCreate, session: SessionDep) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj