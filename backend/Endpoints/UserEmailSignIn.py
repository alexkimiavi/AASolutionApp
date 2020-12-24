from flask_restful import Resource, reqparse
import pyrebase
from FirebaseConfig import FirebaseConfig

class UserEmailSignIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Username')
        parser.add_argument('Password')
        args = parser.parse_args()
        FirebaseInstance = FirebaseConfig()
        auth = FirebaseInstance.getAuth()
        try:
            auth.sign_in_with_email_and_password(args['Username'], args['Password'])
        except:
            return {"msg":"bad"}
        return {"msg":"good"}