from flask_restful import Resource, reqparse
import pyrebase

from FirebaseConfig import FirebaseConfig
""" Post Request"""
class AddUserFromEmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Username')
        parser.add_argument('Password')
        args = parser.parse_args()
        try:
            auth = FirebaseConfig().getAuth()
            auth.create_user_with_email_and_password(args['Username'], args['Password'])
        except:
            return{"msg":"bad"}
        return {"msg":"good"}
