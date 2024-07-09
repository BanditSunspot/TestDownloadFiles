"""
LOGIN COMPONENTS
"""
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from view.themes.ui.ButtonApp import ButtonApp, FooterButton


class Footer(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Footer, self).__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 40

        left_footer_layout = MDBoxLayout(spacing=10)
        discord_btn = FooterButton(text="Discord", size_hint=(None, None), height=40, width=100)
        youtube_btn = FooterButton(text="Youtube", size_hint=(None, None), height=40, width=100)
        left_footer_layout.add_widget(discord_btn)
        left_footer_layout.add_widget(youtube_btn)


        right_footer_layout = MDBoxLayout(spacing=10, adaptive_size=True)
        redit_btn = FooterButton(text="Redit", size_hint_y=None, height=40)
        help_btn = FooterButton(text="?", size_hint_y=None, height=40)
        right_footer_layout.add_widget(redit_btn)
        right_footer_layout.add_widget(help_btn)

        self.add_widget(left_footer_layout)
        self.add_widget(right_footer_layout)