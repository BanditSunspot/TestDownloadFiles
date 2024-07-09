from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout


class AppPopUp(MDRelativeLayout):
    def __init__(self, **kwargs):
        super(AppPopUp, self).__init__(**kwargs)
        self.md_bg_color = "red"

        popUpMsg = MDLabel(text = "error")

        self.add_widget(popUpMsg)