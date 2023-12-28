import datetime
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Column, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


Base = declarative_base()


class Admin(Base):
    __tablename__ = "admin_account"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"


# class Article(Base):
#     __tablename__ = "article"
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     article_head: Mapped[str] = mapped_column(String())
#     article_body: Mapped[Text] = mapped_column(Text)
#     article_time: Mapped[DateTime] = mapped_column(DateTime(), default=datetime.datetime.now())
#     article_picture: Mapped[List["Picture"]] = relationship(back_populates="picture_foreign", cascade="all, delete-orphan")
#
#     def __repr__(self) -> str:
#         return f"article(article_head={self.article_head!r})"
#
#
# class Picture(Base):
#     __tablename__ = "picture"
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     picture_url: Mapped[str] = mapped_column(String())
#     picture_foreign_id: Mapped[int] = mapped_column(ForeignKey("picture.id"))
#     picture_time: Mapped[DateTime] = mapped_column(DateTime(), default=datetime.datetime.now)
#     picture_foreign: Mapped["Article"] = relationship(back_populates="article_picture")
#
#     def __repr__(self) -> str:
#         return f"picture(picture_url={self.picture_url!r})"


class Photo(Base):
    __tablename__ = "photo"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    photo_path: Mapped[str] = mapped_column(String())
    photo_time: Mapped[DateTime] = mapped_column(DateTime(), default=datetime.datetime.now)
    photo_location: Mapped[str] = mapped_column(String())
    photo_sentence: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"photo(photo={self.photo_path!r})"

