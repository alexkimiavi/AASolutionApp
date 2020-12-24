from flask import Flask
from flask_restful import Api
from AddCard import AddCard
import braintree
import requests
import pyrebase


app = Flask(__name__)
api = Api(app)


api.add_resource(AddCard, '/AddCard')

if __name__ == '__main__':
    app.run(debug=True)