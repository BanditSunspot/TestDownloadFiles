"""
LOGIN COMPONENTS
"""
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from view.themes.ui.Line import Line

class DevBlog(MDBoxLayout):
    def __init__(self, **kwargs):
        super(DevBlog, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 20
        self.testLog01 = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel nulla ornare sapien "
                        "condimentum dignissim.")
        self.testLog02 = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel nulla ornare sapien "
                          "condimentum dignissim. Quisque ultricies finibus hendrerit. Praesent sagittis sapien eu "
                          "neque molestie, eget pretium nisi aliquam. Aenean odio odio, sodales et tortor nec, "
                          "elementum dignissim magna. Integer quis finibus augue, quis mollis ligula. Integer eget "
                          "justo eget magna accumsan commodo.")
        self.testLog03 = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel nulla ornare sapien "
                          "condimentum dignissim. Quisque ultricies finibus hendrerit. Praesent sagittis sapien eu "
                          "neque molestie, eget pretium nisi aliquam. Aenean odio odio, sodales et tortor nec, "
                          "elementum dignissim magna. Integer quis finibus augue, quis mollis ligula. Integer eget "
                          "justo eget magna accumsan commodo.")

        devblog_scrollview = ScrollView(bar_inactive_color="#FFFFFF", bar_color="#FFF000")
        devblog_scrollview_content = MDBoxLayout(orientation="vertical", size_hint_y=None, spacing=20, padding=(0, 0, 30, 0))

        # LOG 01
        log01 = MDBoxLayout(orientation="vertical", size_hint_y=None)
        log01_title = MDLabel(text="Log01 Title", halign="left", font_style="H5", size_hint_y=None, height=40)
        log01_text = MDLabel(text=self.testLog01, halign="left", font_style="Body1", size_hint_y=None)

        log01.add_widget(log01_title)
        log01.add_widget(log01_text)
        log01_text.bind(texture_size=log01_text.setter("size"))
        log01.bind(minimum_height=log01.setter("height"))

        # LOG 02
        log02 = MDBoxLayout(orientation="vertical", size_hint_y=None)
        log02_title = MDLabel(text="Log02 Title", halign="left", font_style="H5", size_hint_y=None, height=40)
        log02_text = MDLabel(text=self.testLog02, halign="left", font_style="Body1", size_hint_y=None)

        log02.add_widget(log02_title)
        log02.add_widget(log02_text)
        log02_text.bind(texture_size=log02_text.setter("size"))
        log02.bind(minimum_height=log02.setter("height"))

        # LOG 03
        log03 = MDBoxLayout(orientation="vertical", size_hint_y=None)
        log03_title = MDLabel(text="Log03 Title", halign="left", font_style="H5", size_hint_y=None, height=40)
        log03_text = MDLabel(text=self.testLog03, halign="left", font_style="Body1", size_hint_y=None)

        log03.add_widget(log03_title)
        log03.add_widget(log03_text)
        log03_text.bind(texture_size=log03_text.setter("size"))
        log03.bind(minimum_height=log03.setter("height"))


        devblog_scrollview_content.bind(minimum_height=devblog_scrollview_content.setter("height"))
        devblog_scrollview_content.add_widget(log01)
        devblog_scrollview_content.add_widget(Line())
        devblog_scrollview_content.add_widget(log02)
        devblog_scrollview_content.add_widget(Line())
        devblog_scrollview_content.add_widget(log03)
        devblog_scrollview_content.add_widget(Line())




        devblog_scrollview.add_widget(devblog_scrollview_content)

        self.add_widget(devblog_scrollview)







