from kivymd.uix.button import MDRaisedButton

class ButtonApp(MDRaisedButton):
    def __init__(self, **kwargs):
        super(ButtonApp, self).__init__(**kwargs)

        self.size_hint_x = 1

class FooterButton(MDRaisedButton):
    def __init__(self, **kwargs):
        super(FooterButton, self).__init__(**kwargs)


class ConnexionButton(MDRaisedButton):
    def __init__(self, **kwargs):
        super(ConnexionButton, self).__init__(**kwargs)

        self.size_hint_x = 1


