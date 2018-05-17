import unittest

from flask_jwt_extended import decode_token
from passlib.hash import pbkdf2_sha256

from flask_app import create_app
from functionality.book import get_book_details, \
    create_user_book_mapping_record, delete_book, \
    update_user_book_mapping_record, rent_book
from functionality.login import is_password_match, validate_user
from functionality.users import get_user_name_by_user_name
from models import session
from models.book import Book, UserBookMapping
from models.users import User


class TestBook(unittest.TestCase):
    def setUp(self):
        super(TestBook, self).setUp()
        self.maxDiff = None
        self.app = create_app()
        self.session = session
        user_obj = User(
            username="user_test",
            email="user@test.com",
            password=pbkdf2_sha256.hash("pass")
        )
        self.session.add(user_obj)
        self.session.flush()
        self.user_id = int(user_obj.id)
        book_obj = Book(
            book_name="python"
        )
        self.session.add(book_obj)
        self.session.flush()
        self.book_id = int(book_obj.id)

    def tearDown(self):
        super(TestBook, self).tearDown()
        self.session.rollback()

    def test_get_book_details_true(self):
        with self.app.app_context():
            session_obj = session.query(Book.id, Book.book_name).filter(
                Book.is_deleted == 0).all()
            response = get_book_details()
            self.assertEqual(
                response['book_list'][0],
                dict(
                    id=session_obj[0].id,
                    book_name=session_obj[0].book_name
                )
            )

    def test_create_user_book_mapping_record(self):
        with self.app.app_context():
            response = create_user_book_mapping_record(
                user_id=self.user_id,
                book_id=self.book_id
            )
            session_obj = session.query(UserBookMapping).filter(
                UserBookMapping.book_id == self.book_id,
                UserBookMapping.user_id == self.user_id
            ).first()
            self.assertEqual(response.id, session_obj.id)

    def test_update_user_book_mapping_record_functional_test(self):
        with self.app.app_context():
            response = create_user_book_mapping_record(
                user_id=self.user_id,
                book_id=self.book_id
            )
            delete_book(user_id=self.user_id,book_id=self.book_id)
            update_user_book_mapping_record(response)
            self.assertEqual(response.is_deleted, 0)

    def test_rent_book_already_added(self):
        with self.app.app_context():
            response = create_user_book_mapping_record(
                user_id=self.user_id,
                book_id=self.book_id
            )
            data = dict(
                user_id=self.user_id,
                book_id=self.book_id
            )
            self.assertEqual(
                rent_book(**data),
                dict(response="BOOK-ALREADY-ADDED")
            )

    def test_rent_book_deleted_book(self):
        with self.app.app_context():
            data = dict(
                user_id=self.user_id,
                book_id=self.book_id
            )
            response = create_user_book_mapping_record(**data)
            delete_book(**data)
            self.assertEqual(
                rent_book(**data),
                dict(response="success")
            )

    def test_rent_book(self):
        with self.app.app_context():
            data = dict(
                user_id=self.user_id,
                book_id=self.book_id
            )
            self.assertEqual(
                rent_book(**data),
                dict(response="success")
            )
