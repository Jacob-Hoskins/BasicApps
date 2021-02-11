from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.clock import Clock
import time

Builder.load_file('myApp.kv')

class ClockScreen(Widget):
    pass


class FirstApp(App):

    def build(self):
        return ClockScreen()

    def on_start(self):
        Clock.schedule_interval(self.updateClock, 1)

    def updateClock(self, *args):
        print(args)
        #create time variable, if var doesnt work here create it in the ClockScreen class and call it here
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        clockTime = f'{hour}:{minute}'
        #update label
        self.root.ids.clock.text = clockTime


FirstApp().run()