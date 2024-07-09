"""
LINE / SEPARATOR COMPONENTS
"""

from kivy.uix.image import Image

class Line(Image):
    def __init__(self, **kwargs):
        super(Line, self).__init__(**kwargs)

        self.size_hint_y = None
        self.height = 1
        self.color = "#ffffff"



