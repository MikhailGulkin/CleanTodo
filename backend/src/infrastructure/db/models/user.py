from uuid import UUID, uuid4

from sqlalchemy import False_
from sqlalchemy.orm import Mapped, mapped_column

from .base import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    deleted: Mapped[bool] = mapped_column(default=False, server_default=False_())
