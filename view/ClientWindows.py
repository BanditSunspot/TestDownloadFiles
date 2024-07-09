from kivymd.uix.boxlayout import MDBoxLayout

from view.LeftCol import LeftCol
from view.RightCol import RightCol
from view.components.Footer import Footer
from view.components.TitleBar import TitleBar
from view.themes.ui.Line import Line
from updater.Updater import Updater


class ClientWindows(MDBoxLayout):
    def __init__(self, controller, **kwargs):
        super(ClientWindows, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 20

        Updater()

        # TITLE BAR COMPONENT #
        self.title_bar = TitleBar()
        self.add_widget(self.title_bar)

        # LINE TOP COMPONENT #
        self.line_top = Line()
        self.add_widget(self.line_top)

        # RIGHT AND LEFT COLUMN COMPONENT #
        self.bodyapp = MDBoxLayout(orientation="horizontal")
        self.bodyapp_left_column = LeftCol(size_hint_x=None, width=550)
        self.bodyapp_right_column = RightCol(controller)

        self.bodyapp.add_widget(self.bodyapp_left_column)
        self.bodyapp.add_widget(self.bodyapp_right_column)
        self.add_widget(self.bodyapp)

        # LINE BOTTOM COMPONENT #
        self.line_bottom = Line()
        self.add_widget(self.line_bottom)

        # FOOTER COMPONENT #
        self.footerapp = Footer()
        self.add_widget(self.footerapp)

    def switchToRegisterComponent(self, controller):
        print("Register Component")
        self.bodyapp_right_column.removeLoginLayout(controller, "Register")

    def switchToLoginComponent(self, controller, removeComp):
        print("Register Component")
        if(removeComp == "Register"):
            self.bodyapp_right_column.removeRegisterLayout(controller)
        if(removeComp == "LostPassword"):
            return self.bodyapp_right_column.removeLostPasswordLayout(controller)

    def switchToLostPasswordComponent(self, controller):
        print("Register Component")
        self.bodyapp_right_column.removeLoginLayout(controller, "LostPassword")