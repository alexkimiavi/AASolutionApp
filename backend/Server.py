from flask import Flask
from flask_restful import Api
import braintree
import requests
import pyrebase

# Packages
from FirebaseConfig import FirebaseConfig
from Endpoints.AssignCardToUser import AssignCardToUser
from Endpoints.AddUser import AddUserFromEmail
from Endpoints.AddFriend import AddFriend
from Endpoints.UserEmailSignIn import UserEmailSignIn

myFirebaseConfig = FirebaseConfig()

app = Flask(__name__)
api = Api(app)
api.add_resource(AssignCardToUser, '/AssignCardToUser')
api.add_resource(AddUserFromEmail, '/AddUser')
api.add_resource(AddFriend, '/AddFriend')
api.add_resource(UserEmailSignIn, '/UserEmailSignIn')

if __name__ == '__main__':
    app.run(debug=True)