from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file('calc.kv')
Window.size = (500, 700)


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def number_clicked(self, button):
        #create a variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text

        #determine if zero is in prior
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'


    def equals(self):
        prior = self.ids.calc_input.text
        #addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0

            # loop through list:
            for number in num_list:
                answer = answer + int(number)

            print(answer)
            self.ids.calc_input.text = str(answer)

        if "-" in prior:
            num_list = prior.split("-")
            answer = 0

            # loop through list:
            for number in num_list:
                answer = answer - int(number)

            print(answer)
            self.ids.calc_input.text = str(answer)

        if "*" in prior:
            num_list = prior.split("*")
            answer = 1

            # loop through list:
            for number in num_list:
                answer = answer * int(number)

            print(answer)
            self.ids.calc_input.text = str(answer)

        if "/" in prior:
            num_list = prior.split("/")
            answer = 0

            # loop through list:
            for number in num_list:
                answer = answer / int(number)

            print(answer)
            self.ids.calc_input.text = str(answer)

class Calculator(App):

    def build(self):
        return MyLayout()


Calculator().run()