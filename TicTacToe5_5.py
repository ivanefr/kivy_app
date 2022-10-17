from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

# Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class MyApp(App):
    def __init__(self):
        self.switch = True
        super().__init__()

    def tic_tac_toe(self, arg):
        arg.disabled = True
        if self.switch:
            arg.text = 'X'
        else:
            arg.text = 'O'
        self.switch = not self.switch
        coordinate = (
            (0, 1, 2, 3, 4), (5, 6, 7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19), (20, 21, 22, 23, 24),
            # по оси X
            (0, 5, 10, 15, 20), (1, 6, 11, 16, 21), (2, 7, 12, 17, 22), (3, 8, 13, 18, 23),
            (4, 9, 14, 19, 24),
            # по оси Y
            (20, 16, 12, 8, 4), (0, 6, 12, 18, 24),
            # по диагонали D
            # (0, 1, 2), (3, 4, 5,), (6, 7, 8,),
            # (0, 3, 6), (1, 4, 7), (2, 5, 8),
            # (0, 4, 8), (2, 4, 6)
        )

        vector = lambda item: [self.buttons[i].text for i in item]

        for item in coordinate:
            if vector(item).count("X") == 5 or vector(item).count("O") == 5:
                for i in item:
                    self.buttons[i].color = [0, 1, 0, 1]
                for button in self.buttons:
                    button.disabled = True
                break

    def restart(self, instance):
        self.switch = True
        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ''
            button.disabled = False

    def build(self):
        self.title = "Крестики - Нолики"
        self.buttons = []
        root = BoxLayout(orientation="vertical", padding=5)
        grid = GridLayout(cols=5)

        for _ in range(25):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=20,
                disabled=False,
                on_press=self.tic_tac_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)

        root.add_widget(grid)

        root.add_widget(
            Button(
                text="restart",
                size_hint=[1, 0.1],
                on_press=self.restart
            )
        )

        return root


if __name__ == '__main__':
    MyApp().run()
