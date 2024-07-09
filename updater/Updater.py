import ctypes  # An included library with Python install.

from kivymd.uix.boxlayout import MDBoxLayout
from urllib.request import urlretrieve
import os

class Updater(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Updater, self).__init__(**kwargs)
        self.ServerUrl = "https://github.com/BanditSunspot/TestDownloadFiles"
        self.Mbox('Update detected', 'Current version: 1.0.0.1\nNew version: 1.0.0.2', 1)

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)