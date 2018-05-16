import unittest

from flask_app import create_app
from functionality.users import get_user_name_by_user_name, check_user_exist, \
    create_user_entry, create_user
from models import session
from models.users import User


class TestUsers(unittest.TestCase):
    def setUp(self):
        super(TestUsers, self).setUp()
        self.app = create_app()
        self.session = session
        user_obj = User(
            username="anand1",
            email="anand@anand.com",
            password="anand"
        )
        self.session.add(user_obj)
        self.session.flush()
        self.user_id = int(user_obj.id)

    def tearDown(self):
        super(TestUsers, self).tearDown()
        self.session.rollback()

    def test_get_user_name_by_user_name_user_found(self):
        with self.app.app_context():
            user_obj = get_user_name_by_user_name(user_name="anand1")
            self.assertEqual(int(user_obj.id), self.user_id)

    def test_get_user_name_by_user_name_deleted_user_not_found(self):
        self.session.query(User).filter(
            User.username == "anand1").update(dict(is_deleted=1))
        with self.app.app_context():
            user_obj = get_user_name_by_user_name(user_name="anand1")
            self.assertNotEqual(user_obj, self.user_id)

    def test_check_user_exist(self):
        with self.app.app_context():
            self.assertRaises(
                ValueError,
                check_user_exist,
                user_name="anand1"
            )

    def test_create_user_entry(self):
        with self.app.app_context():
            data = dict(
                user_name="anand2",
                email="anand1@anand.com",
                password="hello"
            )
            user_obj = create_user_entry(**data)
            user_obj_query = self.session.query(User).filter(
                User.username == "anand2"
            ).first()
            self.assertEqual(user_obj, user_obj_query)

    def test_create_user_functionality_key_error(self):
        with self.app.app_context():
            data = dict(
            )
            self.assertRaises(KeyError, create_user, **data)

    def test_create_user_functionality_value_error(self):
        with self.app.app_context():
            data = dict(
                user_name=123
            )
            self.assertRaises(ValueError, create_user, **data)

    def test_create_user_functionality(self):
        with self.app.app_context():
            data = dict(
                user_name="test",
                email="test@test.com",
                password="test",

            )
            response_id = create_user(**data)
            user_id = self.session.query(User).filter(
                User.username == "test"
            ).first()
            self.assertEqual(response_id, int(user_id.id))
