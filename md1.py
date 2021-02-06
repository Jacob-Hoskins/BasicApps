from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class demoApp(MDApp):

    def build(self):
        return

    def show_input(self):
        print(self.root.ids.username.text)
        print(self.root.ids.password.text)

demoApp().run()