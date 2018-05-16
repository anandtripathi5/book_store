from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

session = None
session_obj = None


def _get_db_session_obj(database_url):
    global session_obj
    session_obj = sessionmaker(bind=create_engine(database_url))
    return session_obj


def get_session(database_url=None):
    db_session_obj = _get_db_session_obj(database_url)
    global session
    session = scoped_session(db_session_obj)
    return session
