# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text, Index, \
    ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String(128), nullable=False)
    created_on = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(DateTime, nullable=False,
                         server_default=text(
                             "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_deleted = Column(Integer, server_default=text("'0'"))


class UserBookMapping(Base):
    __tablename__ = 'user_book_mapping'
    __table_args__ = (
        Index('user_id', 'user_id', 'book_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey(u'users.id'), nullable=False)
    book_id = Column(ForeignKey(u'books.id'), nullable=False, index=True)
    created_on = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    is_deleted = Column(Integer, server_default=text("'0'"))

    book = relationship(u'Book')
    user = relationship(u'User')