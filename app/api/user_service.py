from flask_restful import (
    Resource,
    marshal,
    marshal_with,
    fields,
    reqparse,
    abort)
from app.models.user import User
from flask import request

user_fields = {
    "id": fields.String,
    "username": fields.String,
    "password": fields.String,
    "email": fields.String,
    "delete": fields.Boolean
}


class UserBase(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username', location='json')
        self.reqparse.add_argument(
            'password',
            type=str,
            default="",
            required=True,
            location='json')
        self.reqparse.add_argument(
            'email',
            type=str,
            default="",
            required=True,
            location='json')
        self.reqparse.add_argument('delete', type=bool, location='json')
        super(UserBase, self).__init__()


class UserService(UserBase):

    @marshal_with(user_fields)
    def get(self):
        return User.all(), 200

    def post(self):
        args = self.reqparse.parse_args()
        user = User(**args)
        if(user.save()):
            return 'create %s success' % user.username, 202
        return ' %s not found' % user.email, 404


class UserServiceList(UserBase):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username', location='json')
        self.reqparse.add_argument(
            'password',
            type=str,
            default="",
            required=True,
            location='json')
        self.reqparse.add_argument('delete', type=bool, location='json')

    def get(self, id):
        user = User.get(id)
        if user and (not user.delete):
            return marshal(User.get(id), user_fields), 201
        return "Not Found", 404

    def delete(self, id):
        user = User.get(id)
        if user and (not user.delete):
            user.remove()
            return "Delete success", 204
        return "Not Found", 404

    def put(self, id):
        args = self.reqparse.parse_args()
        user = User.get(id)
        if user and (not user.delete) and user.update(**args):
            return 'update %s success' % user.email, 202
        return ' %s not found' % user.email, 404
