from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    email: str = Field(unique=True)
    password: str = Field()
