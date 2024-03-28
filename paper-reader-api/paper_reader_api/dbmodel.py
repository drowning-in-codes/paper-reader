from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Paper(db.Model):
    paper_id: Mapped[int] = mapped_column(primary_key=True)
    updated_time: Mapped[str] = mapped_column(unique=True)
    published: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    summary: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column(String(64))
