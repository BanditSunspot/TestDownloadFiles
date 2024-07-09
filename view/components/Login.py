"""
LOGIN COMPONENTS
"""
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from view.themes.ui.ButtonApp import ButtonApp, ConnexionButton
from view.themes.ui.Input import Input


class Login(MDBoxLayout):
    def __init__(self, controller, **kwargs):
        super(Login, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter("height"))

        login_component_title = MDLabel(text="Connexion", halign="center", font_style="H4", size_hint_y=None, height=30)

        login_body_layout = MDBoxLayout(orientation="vertical", size_hint_y=None, spacing=10)
        username_input = Input(hint_text="Username...", size_hint_y=None, height=30)
        password_input = Input(hint_text="Password...", size_hint_y=None, height=30)
        connexion_btn = ConnexionButton(text="Connexion", size_hint_y=None, height=40, on_press=lambda x: self.checkLogininfos(username_input.text, password_input.text, controller))
        login_body_layout.add_widget(username_input)
        login_body_layout.add_widget(password_input)
        login_body_layout.add_widget(connexion_btn)

        login_controls = MDBoxLayout(orientation="horizontal", size_hint_y=None, spacing=10)
        register_btn = ButtonApp(text="S'inscrire", size_hint_y=None, height=40, on_press=lambda x: controller.switchRegister())
        password_lost_btn = ButtonApp(text="Mot de passe perdu ?", size_hint_y=None, height=40, on_press=lambda x: controller.switchLostPassword())
        login_controls.add_widget(register_btn)
        login_controls.add_widget(password_lost_btn)
        login_body_layout.add_widget(login_controls)

        login_controls.bind(minimum_height=login_controls.setter("height"))
        login_body_layout.bind(minimum_height=login_body_layout.setter("height"))
        self.add_widget(login_component_title)
        self.add_widget(login_body_layout)

    def checkLogininfos(self, username, password, controller):
        if(controller.tryLoginWith(username, password)):
            print("Login Success")
        else:
            print("Login Fail")
