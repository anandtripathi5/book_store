import unittest
from passlib.hash import pbkdf2_sha256

from flask_app import create_app
from functionality.book import delete_book
from functionality.user_statment import get_number_of_books_charge
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
        book_obj = Book(
            book_name="data"
        )
        self.session.add(book_obj)
        self.session.flush()
        self.book_id_2 = int(book_obj.id)
        user_book_mapping = UserBookMapping(
            user_id=self.user_id,
            book_id=self.book_id
        )
        self.session.add(user_book_mapping)
        self.session.flush()
        user_book_mapping = UserBookMapping(
            user_id=self.user_id,
            book_id=self.book_id_2
        )
        self.session.add(user_book_mapping)
        self.session.flush()

    def tearDown(self):
        super(TestBook, self).tearDown()
        self.session.rollback()

    def test_get_number_of_books_charge(self):
        with self.app.app_context():
            response = get_number_of_books_charge(user_id=self.user_id)
            self.assertEqual(response, dict(book_charges=2, number_of_books=2))

    def test_get_number_of_books_charge_deleted_book(self):
        with self.app.app_context():
            delete_book(user_id=self.user_id, book_id=self.book_id_2)
            response = get_number_of_books_charge(user_id=self.user_id)
            self.assertEqual(response, dict(book_charges=1, number_of_books=1))
