from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Text,
)
from sqlalchemy.orm import (
    relationship, 
    Mapped, 
    mapped_column, 
    DeclarativeBase
)
from sqlalchemy.sql import func
from typing import Annotated
import datetime

from src.database.enums import Role, Week, Day

created_at = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), default=func.now())]
updated_at = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), 
        default=func.now(),
        onupdate=func.now()
    )]

class Base(DeclarativeBase):
    pass

class Students(Base):
    __tablename__ = "Students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    photo_id: Mapped[str] = mapped_column(String(255), nullable=False)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("Groups.id"), nullable=False)
    role: Mapped[Role] = mapped_column(String(30), nullable=False, default=Role.STUDENT.value)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    group = relationship("Groups", back_populates="students")

class Groups(Base):
    __tablename__ = "Groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    course: Mapped[int] = mapped_column(Integer(1), nullable=False)
    year: Mapped[int] = mapped_column(Integer(4), nullable=False)
    profession: Mapped[int] = mapped_column(Integer(3), nullable=False)
    monitor_id: Mapped[int] = mapped_column(Integer, ForeignKey("Students.id"), nullable=False)
    admin_id: Mapped[int] = mapped_column(Integer, ForeignKey("Students.id"), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    students = relationship("Students", back_populates="group")
    Schedule = relationship("Schedule", back_populates="group")

class Schedule(Base):
    __tablename__ = "Schedule"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("Groups.id"), nullable=False)
    week: Mapped[Week] = mapped_column(String(10), nullable=False)
    day: Mapped[Day] = mapped_column(String(20), nullable=False)
    couple: Mapped[int] = mapped_column(Integer(1), nullable=False)
    lesson: Mapped[str] = mapped_column(String(255), nullable=False)
    teacher: Mapped[str] = mapped_column(String(255), nullable=False)
    classroom: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    group = relationship("Groups", back_populates="schedule")

class Register(Base):
    __tablename__ = "Register"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("Students.id"), nullable=False)
    presence: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    schedule_id: Mapped[int] = mapped_column(Integer, ForeignKey("Schedule.id"), nullable=False)
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    active_to: Mapped[datetime.datetime] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]