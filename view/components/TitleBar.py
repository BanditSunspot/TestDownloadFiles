"""
TITLEBAR COMPONENTS
"""
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class TextTitleLayout(FloatLayout):
    pass

class ImageTitleLayout(FloatLayout):
    pass

class TitleBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super(TitleBar, self).__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = None
        #self.pos_hint = {'center_x': 0.25, 'center_y': 1}
        self.height = 10

        afo_title = MDLabel(text="AfterLife Online", font_style="H6", halign="left")

        self.add_widget(ImageTitleLayout())
        self.add_widget(TextTitleLayout())






