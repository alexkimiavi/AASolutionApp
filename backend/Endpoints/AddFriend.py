from flask_restful import Resource


class AddFriend(Resourse):
    """ This will add a friend for the user """
    def post(self):
        return {"Add":"Friend"}
