from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

from view.components.Login import Login
from view.components.LostPasswordComp import LostPasswordComp
from view.components.RegisterComp import RegisterComp

class ImageRightColLayout(FloatLayout):
    pass

class RightCol(MDBoxLayout):
    def __init__(self, controller, **kwargs):
        super(RightCol, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.testDescription = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel nulla ornare sapien "
                          "condimentum dignissim. Quisque ultricies finibus hendrerit. Praesent sagittis sapien eu "
                          "neque molestie, eget pretium nisi aliquam.")


        right_col_description = MDLabel(text=self.testDescription, font_style="Body1", halign="center")
        #self.add_widget(right_col_description)
        self.add_widget(ImageRightColLayout())

        # CONNEXION #
        self.login_layout = Login(controller)
        self.add_widget(self.login_layout)

    def displayRegisterLayout(self, controller):

        # Register #
        self.register_layout = RegisterComp(controller)
        self.add_widget(self.register_layout)

    def displayLoginLayout(self, controller):

        # CONNEXION #
        self.login_layout = Login(controller)
        self.add_widget(self.login_layout)

    def displayLostPasswordLayout(self, controller):

        # CONNEXION #
        self.lostpassword_layout = LostPasswordComp(controller)
        self.add_widget(self.lostpassword_layout)

    def removeLoginLayout(self, controller, request):
        self.remove_widget(self.login_layout)
        if(request == "Register"):
            self.displayRegisterLayout(controller)
        if(request == "LostPassword"):
            self.displayLostPasswordLayout(controller)

    def removeRegisterLayout(self, controller):
        self.remove_widget(self.register_layout)
        self.displayLoginLayout(controller)

    def removeLostPasswordLayout(self, controller):
        self.remove_widget(self.lostpassword_layout)
        self.displayLoginLayout(controller)