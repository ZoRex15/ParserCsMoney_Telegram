from .models import Base, User

from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker


class Database:
    __engine = create_engine(url='sqlite:///database/database.db', echo=True)
    __session = sessionmaker(__engine)

    @classmethod
    def create_tables(cls) -> None:
        with cls.__engine.begin() as conn:
            Base.metadata.create_all(conn)

    @classmethod
    def add_user(cls, user_id: int) -> None:
        with cls.__session() as session:

            user = session.get(User, user_id)

            if not user:
                user = User(
                    user_id=user_id)
                session.add(user)
                session.commit()
            else:
                print('Пользователь уже в БД')
        
        

    @classmethod
    def set_filters(cls, user_id: int, max_price: float, min_price: float) -> None:
        with cls.__session() as session:
            stmt = update(User).where(User.user_id == user_id)
            stmt = stmt.values(max_price=max_price, min_price=min_price)
            session.execute(stmt)
            session.commit()
