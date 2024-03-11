from sqlalchemy import (
    Integer,
    ForeignKey,
    Boolean,
    DateTime,
    BigInteger
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from src.database.models.models import (
    created_at,
    updated_at
)
from .base import Base
import datetime


class Register(Base):
    __tablename__ = "Register"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("Students.id", ondelete='CASCADE'), nullable=False)
    presence: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("Schedule.id"), nullable=False)
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    schedule = relationship("Schedule", back_populates="register")