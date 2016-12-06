from app import db
from werkzeug.security import (generate_password_hash, check_password_hash)
from flask_validator import (ValidateString, ValidateEmail, ValidateBoolean)
from base import CRUDMixin


class User(CRUDMixin, db.Model):
    __tablename__ = 'users'
    # id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String())
    delete = db.Column(db.Boolean, unique=False, default=False)

    def __init__(self, username, password, email, delete=False):
        self.username = username
        self.setpassword(password)
        self.email = email
        self.delete = delete

    # @property
    # def password(self):
    #   return self._password

    # @password.setter
    # def password(self, password):
    #   self._password = generate_password_hash(password)

    def setpassword(self, password):
        self.password = generate_password_hash(password)

    def update(self, **kwargs):
        for attr, value in kwargs.iteritems():
            if(attr == 'password'):
                self.setpassword(value)
            else:
                setattr(self, attr, value)
        return self.save() or self

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @classmethod
    def __declare_last__(cls):
        ValidateString(User.username)
        ValidateString(User.password)
        ValidateEmail(User.email)
        ValidateBoolean(User.delete)

    def __repr__(self):
        return '<User %s>' % self.email
