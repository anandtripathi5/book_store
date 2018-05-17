# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text, Index, \
    ForeignKey, Numeric
from sqlalchemy.orm import relationship

from base import Base


class BookType(Base):
    __tablename__ = 'book_type'

    id = Column(Integer, primary_key=True)
    book_type = Column(String(126), nullable=False)
    charge = Column(Numeric(20, 6), nullable=False)
    created_on = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_deleted = Column(Integer, server_default=text("'0'"))
    fixed_days = Column(Integer, nullable=False, server_default=text("'0'"))
    fixed_charges = Column(Numeric(20, 6), nullable=False,
                           server_default=text("'0.000000'"))


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String(128), nullable=False)
    created_on = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(DateTime, nullable=False,
                         server_default=text(
                             "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_deleted = Column(Integer, server_default=text("'0'"))
    book_type_id = Column(ForeignKey(u'book_type.id'), nullable=False, index=True)

    book_type = relationship(u'BookType')


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