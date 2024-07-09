from kivymd.app import MDApp
from kivy.core.window import Window

from controller.LauncherController import LauncherController
from kivy.lang import Builder

Builder.load_file("./KvFiles/KvFunctions.kv")


class AfoLauncherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.material_style = "M3"
        Window.size = 1000, 720
        controller = LauncherController()
        return controller.client_windows


if __name__ == "__main__":
    AfoLauncherApp().run()
