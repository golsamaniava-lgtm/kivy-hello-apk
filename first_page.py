from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from arabic_reshaper import reshape as re
from bidi.algorithm import get_display as gd

from widgets.round_button import RoundButton
from widgets.circle_button import CircleButton


class FirstPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # پس‌زمینه سفید
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # تصاویر
        top_image = Image(
            source="Images/top.jpg",
            size_hint=(0.4, 0.25),
            pos_hint={"center_x": 0.5, "top": 1},
        )

        bottom_right_image = Image(
            source="Images/right.jpg",
            size_hint=(0.25, 0.27),
            pos_hint={"right": 1, "bottom": 0},
        )

        bottom_left_image = Image(
            source="Images/left.jpg",
            size_hint=(0.25, 0.3),
            pos_hint={"left": 1, "bottom": 0},
        )

        # دکمه شروع
        start_button = RoundButton(
            text=gd(re("شروع")),
            font_size=22,
            font_name="Far_Nazanin.ttf",
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        start_button.bind(on_release=lambda x: setattr(self.manager, "current", "third"))

        # سه دکمه دایره‌ای
        red_btn = CircleButton(color=(1, 0, 0, 1), size_hint=(None, None), size=(30, 30))
        white_btn = CircleButton(color=(1, 1, 1, 1), size_hint=(None, None), size=(30, 30))
        green_btn = CircleButton(color=(0, 1, 0, 1), size_hint=(None, None), size=(30, 30))

        red_btn.bind(on_release=lambda x: setattr(self.manager, "current", "third"))
        white_btn.bind(on_release=lambda x: setattr(self.manager, "current", "second"))
        green_btn.bind(on_release=lambda x: setattr(self.manager, "current", "third"))

        # --- چیدمان جدید و ریسپانسیو ---
        circle_anchor = AnchorLayout(
            anchor_x="center",
            anchor_y="center",
            size_hint=(1, None),
            height=self.height * 0.12,
            pos_hint={"center_y": 0.38}
        )

        circle_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, None),
            height=60,
            spacing=self.width * 0.05
        )

        circle_layout.add_widget(red_btn)
        circle_layout.add_widget(white_btn)
        circle_layout.add_widget(green_btn)

        circle_anchor.add_widget(circle_layout)

        # ریسپانسیو کردن فاصله‌ها هنگام تغییر اندازه صفحه
        self.bind(size=lambda *args: self.update_circle_layout(circle_layout))

        # اضافه کردن ویجت‌ها
        layout.add_widget(top_image)
        layout.add_widget(bottom_right_image)
        layout.add_widget(bottom_left_image)
        layout.add_widget(start_button)
        layout.add_widget(circle_anchor)

        self.add_widget(layout)

    def update_circle_layout(self, layout):
        layout.spacing = self.width * 0.04

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos
