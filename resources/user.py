import sqlite3
from flask_restful import Resource, reqparse
from flask import request
from models.user import UserModel


class UserRegister(Resource):

    user_parser = reqparse.RequestParser()
    user_parser.add_argument('username',
        type = str,
        required=True,
        help='This field cannot be left blank!'
    )
    user_parser.add_argument('password',
        type = str,
        required=True,
        help='This field cannot be left blank!'
    )

    def post(self):
        data = UserRegister.user_parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message':'A user with that username already exist'}, 400
        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {'message':'An error ocurred saving the user'},500
        return {'message':'User created successfully'}, 201
