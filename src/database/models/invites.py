from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    BigInteger
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from src.database.models.models import (
    created_at,
    updated_at
)
from .base import Base


class Invites(Base):
    __tablename__ = "Invites"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("Groups.id", ondelete='CASCADE'), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    patronymic_name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
