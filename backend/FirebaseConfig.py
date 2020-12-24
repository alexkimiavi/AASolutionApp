import pyrebase


class FirebaseConfig():

    def __init__(self):
        self.firebaseConfig = {
            "apiKey": "AIzaSyCL-ynwv_X-OBRCYG8aAIwK8DDE31Qfjzo",
            "authDomain": "aasolutionsappdevelopment.firebaseapp.com",
            "databaseURL": "https://aasolutionsappdevelopment-default-rtdb.firebaseio.com",
            "projectId": "aasolutionsappdevelopment",
            "storageBucket": "aasolutionsappdevelopment.appspot.com",
            "messagingSenderId": "995602919228",
            "appId": "1:995602919228:web:d999df3fb7c34ef9d6b839",
            "measurementId": "G-3N8CPFBMZP"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        self.storage = self.firebase.storage()
    def getConfig(self):
        return firebaseConfig
    def getFirebase(self):
        return firebase
    def getAuth(self):
        return self.auth
    def getStorage(self):
        return self.storage
    def getDb(self):
        return self.db
