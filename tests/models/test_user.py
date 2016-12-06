import os
import unittest
# from faker import Faker
from app import application, db
from app.models.user import User
import tempfile


class TestUser(unittest.TestCase):

    def setUp(self):
        # self.db, application.config['DATABASE'] = tempfile.mkstemp()
        # application.config.from_pyfile('config/development.cfg')
        application.config['TESTING'] = True
        self.client = application.test_client()
        self.db = db
        self.db.create_all()
        self.user = User.create(
            username="quandc",
            password='12345678',
            email='quandc@example.com'
        )

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_create_user(self):
        self.assertEqual(User.query.count(), 1)
        self.user = User.create(
            username="hello",
            password='12345678',
            email='hello@example.com'
        )
        self.assertEqual(User.query.count(), 2)

    def test_get_user(self):
        user = User.query.first()
        self.assertEqual("quandc", user.username)
        self.assertEqual("quandc@example.com", user.email)
        self.assertEqual(False, user.delete)

    def test_delete_user(self):
        user = User.query.first()
        self.assertEqual(False, user.delete)
        user.remove()
        self.assertEqual(True, user.delete)

if __name__ == '__main__':
    unittest.main()
