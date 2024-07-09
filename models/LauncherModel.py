
import json
class LauncherModel:
    def __init__(self, controller):

        self.controller = controller
        self.db = "./user.json"
        self.dbcontent = []
        self.loadDB()

    def registerNewUser(self, username, password, email):
        fileusers = self.dbcontent
        print(fileusers[0])
        with open(self.db, "w") as file:
            data = {"username": username, "password": password, "email": email}
            self.dbcontent[0].get("users").append(data)
            json.dump(self.dbcontent[0], file, indent=4)

    def checkLogin(self, username, password):
        print(username, password)
        if(username == "Test_"):
            return True
        else:
            return False

    def loadDB(self):
        with open(self.db, 'r') as file:
            fileusers = json.load(file)
            self.dbcontent.append(fileusers)
            print(self.dbcontent[0].get("users"))