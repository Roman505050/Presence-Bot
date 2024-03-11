from sqlalchemy import (
    BigInteger,
    Column,
    Table,
    ForeignKey,
    UniqueConstraint
)
from .base import Base

students_groups_association_table = Table(
    "students_groups_association",
    Base.metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("students_id", ForeignKey("Students.id", ondelete="CASCADE")),
    Column("groups_id", ForeignKey("Groups.id", ondelete="CASCADE")),
    UniqueConstraint("students_id", "groups_id", name="unique_student_group"),
)
