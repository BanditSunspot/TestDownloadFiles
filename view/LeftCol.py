from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image

from view.components.DevBlog import DevBlog
from view.components.SocialNetwork import SocialNetwork


class LeftCol(MDBoxLayout):
    def __init__(self, **kwargs):
        super(LeftCol, self).__init__(**kwargs)

        self.orientation = "vertical"

        # DEV BLOG COMPONENTS #
        dev_blog_component = DevBlog()

        self.add_widget(dev_blog_component)
