import unittest

from flask_jwt_extended import decode_token
from passlib.hash import pbkdf2_sha256

from flask_app import create_app
from functionality.login import is_password_match, validate_user
from functionality.users import get_user_name_by_user_name
from models import session
from models.users import User


class TestUsers(unittest.TestCase):
    def setUp(self):
        super(TestUsers, self).setUp()
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

    def tearDown(self):
        super(TestUsers, self).tearDown()
        self.session.rollback()

    def test_is_password_match_true(self):
        with self.app.app_context():
            hash_password = pbkdf2_sha256.hash("pass")
            flag = is_password_match(
                hash_password=hash_password, password="pass")
            self.assertEqual(True, flag)

    def test_is_password_match_false(self):
        with self.app.app_context():
            hash_password = pbkdf2_sha256.hash("pass")
            flag = is_password_match(
                hash_password=hash_password, password="pss")
            self.assertEqual(False, flag)

    def test_validate_user_not_found(self):
        data = dict(user_name="test", password="hello")
        with self.app.app_context():
            self.assertRaises(
                ValueError,
                validate_user,
                **data
            )

    def test_validate_user_password_not_match(self):
        data = dict(user_name="user_test", password="pass1")
        with self.app.app_context():
            self.assertRaises(
                ValueError,
                validate_user,
                **data
            )

    def test_validate_user_positive(self):
        data = dict(user_name="user_test", password="pass")
        with self.app.app_context():
            response = validate_user(**data)
            obj = get_user_name_by_user_name(user_name=data['user_name'])
            user_id = decode_token(response.get("access_token"))['identity']
            self.assertEqual(user_id, int(obj.id))
