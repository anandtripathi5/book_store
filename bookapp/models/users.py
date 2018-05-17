# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text

from base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(126), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    email = Column(String(126), nullable=False, unique=True)
    created_on = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(DateTime, nullable=False,
                         server_default=text(
                             "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
                         ))
    is_deleted = Column(Integer, server_default=text("'0'"))

    def __repr__(self):
        return self.username
