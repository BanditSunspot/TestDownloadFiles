from kivymd.uix.textfield import MDTextField


class Input(MDTextField):
    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)

        self.size_hint_y = None
        self.height = 40
        self.max_height = 60