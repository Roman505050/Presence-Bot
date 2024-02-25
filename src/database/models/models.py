from sqlalchemy import (
    DateTime,
)
from sqlalchemy.orm import (
    mapped_column
)
from sqlalchemy.sql import func
from typing import Annotated
import datetime

created_at = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), default=func.timezone('Europe/Kiev', func.now()))]
updated_at = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), 
        default=func.timezone('Europe/Kiev', func.now()),
        onupdate=func.timezone('Europe/Kiev', func.now())
    )]

