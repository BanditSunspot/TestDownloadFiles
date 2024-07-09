
"""
LAUNCHER CONTROLLER
"""

from models.LauncherModel import LauncherModel
from view.ClientWindows import ClientWindows

class LauncherController:
    def __init__(self):

        self.client_model = LauncherModel(self)
        self.client_windows = ClientWindows(self)

    def register(self, username, password, email):
        self.switchLogin("Register")
        return self.client_model.registerNewUser(username, password, email)

    def switchRegister(self):
        print("inscrire")
        self.client_windows.switchToRegisterComponent(self)

    def switchLogin(self, removeComp):
        print("login")
        self.client_windows.switchToLoginComponent(self, removeComp)

    def switchLostPassword(self):
        print("lost password")
        self.client_windows.switchToLostPasswordComponent(self)

    def tryLoginWith(self, username, password):
        print("Login access in review")
        return self.client_model.checkLogin(username, password)

    def getBackPasswordwithEmail(self, email):
        print("Controller get back password with email:", email)
        self.switchLogin("LostPassword")
    def getBackPasswordwithUsername(self, username):
        print("Controller get back password with username:", username)
        self.switchLogin("LostPassword")


