from flask_restful import Resource


"""Post Request"""
class AddFriend(Resource):
    """ This will add a friend for the user """
    """ The data will be a username of said friend"""
    def post(self):
        return {"Add":"Friend"}
