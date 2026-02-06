from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse


class CircleButton(Button):
    def __init__(self, color=(1, 0, 0, 1), shadow_color=(0, 0, 0, 0.3), **kwargs):
        super().__init__(**kwargs)

        # حذف بک‌گراند پیش‌فرض
        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        # رنگ دایره و سایه
        self.color_value = color
        self.shadow_color = shadow_color

        # رسم اولیه (اندازه صفر تا بعد از bind آپدیت شود)
        with self.canvas.before:
            Color(*self.shadow_color)
            self.shadow = Ellipse(size=(0, 0), pos=(0, 0))

            Color(*self.color_value)
            self.circle = Ellipse(size=(0, 0), pos=(0, 0))

        # هماهنگ شدن گرافیک با تغییر اندازه و موقعیت
        self.bind(pos=self.update_graphics, size=self.update_graphics)

        # آپدیت اولیه برای قرار گرفتن درست دایره و سایه
        self.update_graphics()

    def update_graphics(self, *args):
        # سایه
        self.shadow.pos = (self.pos[0] - 6, self.pos[1] - 6)
        self.shadow.size = (self.size[0] + 12, self.size[1] + 12)

        # خود دایره
        self.circle.pos = self.pos
        self.circle.size = self.size
