from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle


class RedRoundButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        self.normal_color = (0.70, 0.0, 0.10, 1)
        self.pressed_color = (0.70, 0.0, 0.10, 1)

        with self.canvas.before:
            Color(*self.normal_color)
            self.rect = RoundedRectangle(radius=[30])

        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(on_press=self.on_press_effect)
        self.bind(on_release=self.on_release_effect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press_effect(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.pressed_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[30])

    def on_release_effect(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.normal_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[30])
