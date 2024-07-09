"""
LOGIN COMPONENTS
"""
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox

import re

from view.components.AppPopUp import AppPopUp


class RegisterComp(MDBoxLayout):
    def __init__(self, controller, **kwargs):
        super(RegisterComp, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter("height"))
        self.regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.regexUsername = r'\b[A-Za-z_]{4,12}\b'
        self.regexPassword = r'\b[A-Za-z0-9_]{8,16}\b'

        register_title = MDLabel(text="Inscription", halign="center", font_style="H4", size_hint_y=None, height=30)

        register_body_layout = MDBoxLayout(orientation="vertical", size_hint_y=None)
        username_input = TextInput(hint_text="Username...", size_hint_y=None, height=30)
        password_input = TextInput(hint_text="Password...", size_hint_y=None, height=30)
        email_input = TextInput(hint_text="Email...", size_hint_y=None, height=30)

        # RULES CHECK / CONDITION GENERAL D'UTILISATION
        rules_check_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None)
        rules_checkbox = MDCheckbox(size_hint=(None, None),size=(40, 40))
        rules_text = MDLabel(text="Condition generale d'utilisation", halign="right", padding=(0, 0, 15, 0))
        rules_check_layout.add_widget(rules_checkbox)
        rules_check_layout.add_widget(rules_text)

        connexion_btn = Button(text="Inscription", size_hint_y=None, height=40, on_press=lambda x: self.checkInfos(username_input.text, password_input.text, email_input.text, rules_checkbox.active, controller))

        register_body_layout.add_widget(username_input)
        register_body_layout.add_widget(password_input)
        register_body_layout.add_widget(email_input)
        register_body_layout.add_widget(rules_check_layout)
        register_body_layout.add_widget(connexion_btn)

        rules_check_layout.bind(minimum_height=rules_check_layout.setter("height"))
        register_body_layout.bind(minimum_height=register_body_layout.setter("height"))

        self.add_widget(register_title)
        self.add_widget(register_body_layout)

    def checkInfos(self, username, password, email, checkBox, controller):
        isEmailValid = False
        isUsernameValid = False
        isPasswordValid = False
        if(re.fullmatch(self.regexEmail, email)):
            print("email Valid")
            isEmailValid = True
        else:
            popUpError = AppPopUp()
            self.add_widget(popUpError)

        if (re.fullmatch(self.regexUsername, username)):
            print("username Valid")
            isUsernameValid = True
        else:
            popUpError = AppPopUp()
            self.add_widget(popUpError)

        if (re.fullmatch(self.regexPassword, password)):
            print("password Valid")
            isPasswordValid = True
        else:
            popUpError = AppPopUp()
            self.add_widget(popUpError)

        if(isPasswordValid and isUsernameValid and isEmailValid and checkBox):
            return controller.register(username, password, email)