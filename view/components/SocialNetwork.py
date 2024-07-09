"""
LOGIN COMPONENTS
"""
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SocialNetwork(MDBoxLayout):
    def __init__(self, **kwargs):
        super(SocialNetwork, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.bind(minimum_height=self.setter("height"))

        social_network_loyout = MDBoxLayout(orientation="horizontal")
        redit_btn = Button(text="Redit", size_hint_y=None, height=40)
        discord_btn = Button(text="Discord", size_hint_y=None, height=40)
        youtube_btn = Button(text="Youtube", size_hint_y=None, height=40)
        official_site_btn = Button(text="WebSite", size_hint_y=None, height=40)
        social_network_loyout.add_widget(redit_btn)
        social_network_loyout.add_widget(discord_btn)
        social_network_loyout.add_widget(youtube_btn)
        social_network_loyout.add_widget(official_site_btn)

        social_network_loyout.bind(minimum_height=social_network_loyout.setter("height"))
        self.add_widget(social_network_loyout)



