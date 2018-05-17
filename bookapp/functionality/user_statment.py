import datetime

from constants.common_constants import DEFAULT_FALSE_FLAG, DEFAULT_TRUE_FLAG
from models import session
from models.book import Book, UserBookMapping, BookType
from utils.log_handler import function_logger


def get_number_of_books_charge(user_id=None):
    now = datetime.datetime.now()
    book_details = session.query(
        UserBookMapping.created_on,
        BookType.charge,
        BookType.fixed_days,
        BookType.fixed_charges
    ).join(
        Book, Book.id == UserBookMapping.book_id
    ).join(
        BookType,
        BookType.id == Book.book_type_id
    ).filter(
        UserBookMapping.is_deleted == DEFAULT_FALSE_FLAG,
        Book.is_deleted == DEFAULT_FALSE_FLAG,
        UserBookMapping.user_id == user_id
    ).all()
    
    # total charge of rest days + total charge of initial days
    # if total days is greater than fixed days
    # (charge(total_days - fixed days)) + fixed charge
    # else
    # fixed charge
    book_details = [
        ((((now-time).days+1)-fixed_days)*charge if
         (((now-time).days+1)-fixed_days)*charge > 0 else 0)+fixed_charges for
        time, charge, fixed_days, fixed_charges in book_details]
    return dict(
        number_of_books=len(book_details),
        book_charges=sum(book_details)
    )


@function_logger
def get_user_statement(user_id=None):
    return get_number_of_books_charge(user_id=user_id)