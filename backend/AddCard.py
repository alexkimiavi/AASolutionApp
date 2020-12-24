from flask_restful import Resource
import requests

baseUrl = "https://sandbox.privacy.com"
API_KEY = '83c64194-b5fe-4bf6-aeb5-56d6a57d87ff'
headers = { 'Content-Type':'application/json','Authorization': 'api-key ' +API_KEY}

class AddCard(Resource):
    def get(self):
        data = {"type":"SINGLE_USE"}
        r = requests.post(baseUrl + '/v1/card', headers=headers, json=data)
        return r.json()