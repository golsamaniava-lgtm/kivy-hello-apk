from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class RectButton(Button):
    def __init__(self, bg_color=(0, 0.5, 0, 1), **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        self.bg_color = bg_color

        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = Rectangle()

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
