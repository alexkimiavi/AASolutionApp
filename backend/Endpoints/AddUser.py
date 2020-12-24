from flask_restful import Resource


""" Post Request"""
class AddUser(Resource):
    def post(self):
        return {"Add":"User"}