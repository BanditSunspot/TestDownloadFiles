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


class LostPasswordComp(MDBoxLayout):
    def __init__(self, controller, **kwargs):
        super(LostPasswordComp, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter("height"))

        lostpassword_title = MDLabel(text="Saisir Email ou Username:", halign="center", font_style="H4", size_hint_y=None, height=30)

        lostpassword_body_layout = MDBoxLayout(orientation="vertical", size_hint_y=None)
        username_input = TextInput(hint_text="Username...", size_hint_y=None, height=30)
        email_input = TextInput(hint_text="Email...", size_hint_y=None, height=30)

        lostpassword_btn = Button(text="Récupérer Mot de Passe", size_hint_y=None, height=40, on_press=lambda x: self.checkInfos(username_input.text, email_input.text, controller))

        lostpassword_body_layout.add_widget(username_input)
        lostpassword_body_layout.add_widget(email_input)
        lostpassword_body_layout.add_widget(lostpassword_btn)

        self.add_widget(lostpassword_title)
        self.add_widget(lostpassword_body_layout)

    def checkInfos(self, username, email, controller):
        isUsername = False
        isEmail = False
        if(username != ""):
            isUsername = True
        if (email != ""):
            isEmail = True

        if(isEmail):
            return controller.getBackPasswordwithEmail(email)
        if(isUsername):
            return controller.getBackPasswordwithUsername(username)