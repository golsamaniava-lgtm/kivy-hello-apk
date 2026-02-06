from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.graphics import Ellipse, StencilPush, StencilUse, StencilUnUse, StencilPop


class CircleImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update_mask, size=self.update_mask)

    def update_mask(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            StencilPush()
            Ellipse(pos=self.pos, size=self.size)
            StencilUse()

        self.canvas.after.clear()
        with self.canvas.after:
            StencilUnUse()
            StencilPop()
