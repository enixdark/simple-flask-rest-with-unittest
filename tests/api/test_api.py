import os
import unittest
# from faker import Faker
from app import application, db
from app.models.user import User
import json


class TestApi(unittest.TestCase):

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

    def test_get_user(self):
        response = self.client.get(
            '/user/%d' % self.user.id,
        )
        data = json.loads(response.data)
        self.assertEqual(data['username'], "quandc")
        self.assertEqual(data['email'], "quandc@example.com")
        self.assertEqual(data['delete'], False)

    def test_create_user(self):
        self.assertEqual(User.query.count(), 1)
        response = self.client.post(
            '/users', data=json.dumps({"username": "hello", "email":
                       "test@example.com",
                       "password": "12345678"
                                       }), content_type='application/json'
        )
        self.assertEqual('202 ACCEPTED', response.status)
        self.assertEqual(User.query.count(), 2)

    def test_update_user(self):
        user = User.query.first()
        response = self.client.put(
            '/user/%d' % user.id, data=json.dumps({
                "username": "hello",
                "password": "12345678"
            }), content_type='application/json'
        )
        self.assertEqual('202 ACCEPTED', response.status)
        user = User.query.first()
        self.assertEqual("hello", user.username)

    def test_delete_user(self):
        id = User.query.first().id
        response = self.client.delete(
            '/user/%d' % self.user.id
        )
        self.assertEqual(User.query.filter_by(id=id).first().delete, True)
if __name__ == '__main__':
    unittest.main()
