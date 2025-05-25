from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
import sqlalchemy as sa


class TimestampedModel(SQLModel):
    created_at: Optional[datetime] = Field(
        sa_column_kwargs={
            "server_default": sa.sql.text("CURRENT_TIMESTAMP"),
        })
    updated_at: Optional[datetime] = Field(
        sa_column_kwargs={
            "onupdate": sa.func.now(),
        }
    )

class User(TimestampedModel, table=True):
    id: int | None = Field(primary_key=True)
    email: str = Field(unique=True)
    password: str = Field()

class Post(TimestampedModel, table=True):
    id: int | None = Field(primary_key=True)
    user_id: int = Field()
    title: str = Field()
    content: str = Field()
