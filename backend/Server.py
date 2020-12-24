from flask import Flask
from flask_restful import Api
import braintree
import requests
import pyrebase

# Packages
from Endpoints.AssignCardToUser import AssignCardToUser
from Endpoints.AddUser import AddUser
from Endpoints.AddFriend import AddFriend

app = Flask(__name__)
api = Api(app)


api.add_resource(AssignCardToUser, '/AssignCardToUser')
api.add_resource(AddUser, '/AddUser')
api.add_resource(AddFriend, '/AddFriend')

if __name__ == '__main__':
    app.run(debug=True)