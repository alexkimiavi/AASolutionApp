from flask_restful import Resource


class AddUser(Resource):
    def post(self):
        return {"Add":"User"}