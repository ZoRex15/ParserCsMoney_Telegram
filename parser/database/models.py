from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declared_attr
from typing import List


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    max_price: Mapped[float] = mapped_column(nullable=True)
    min_price: Mapped[float] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f'User(user_id={self.user_id!r}, max_price={self.max_price!r}, min_price={self.min_price!r})'
    