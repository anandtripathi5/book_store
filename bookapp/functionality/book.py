from constants.common_constants import DEFAULT_FALSE_FLAG, DEFAULT_TRUE_FLAG
from models import session
from models.book import Book, UserBookMapping
from utils.log_handler import function_logger


@function_logger
def get_book_details():
    book_obj = session.query(Book.id, Book.book_name).filter(
        Book.is_deleted == DEFAULT_FALSE_FLAG
    ).all()
    book_details = [dict(id=book_id, book_name=book_name) for
                    book_id, book_name in book_obj]
    book_details = dict(book_list=book_details)
    return book_details


def create_user_book_mapping_record(user_id=None, book_id=None):
    user_book_map_obj = UserBookMapping(
        user_id=user_id,
        book_id=book_id
    )
    session.add(user_book_map_obj)
    session.flush()
    return user_book_map_obj


def update_user_book_mapping_record(mapping_obj):
    mapping_obj.is_deleted = DEFAULT_FALSE_FLAG
    session.flush()
    return mapping_obj


@function_logger
def rent_book(user_id=None, book_id=None):
    response = None
    mapping_obj = session.query(UserBookMapping).filter(
        UserBookMapping.user_id == user_id,
        UserBookMapping.book_id == book_id
    ).first()
    if mapping_obj:
        if mapping_obj.is_deleted == DEFAULT_FALSE_FLAG:
            response = dict(response="BOOK-ALREADY-ADDED")
        else:
            update_user_book_mapping_record(mapping_obj)
    else:
        create_user_book_mapping_record(
            user_id=user_id, book_id=book_id)

    return response or dict(response="success")


@function_logger
def delete_book(user_id=None, book_id=None):
    session.query(UserBookMapping).filter(
        UserBookMapping.user_id == user_id,
        UserBookMapping.book_id == book_id
    ).update(dict(is_deleted=DEFAULT_TRUE_FLAG))
