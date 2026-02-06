from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from arabic_reshaper import reshape as re
from bidi.algorithm import get_display as gd

from widgets.round_button import RoundButton
from widgets.red import RedRoundButton
from widgets.green import GreenRoundButton


class ThirdPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # پس‌زمینه سفید
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        scroll = ScrollView(size_hint=(1, 1))

        main_layout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=20,
            padding=20
        )
        main_layout.bind(minimum_height=main_layout.setter("height"))

        items = [
            ("img1.png", "page1", "دستیار اقتصادی", "shop"),
            ("img2.png", "page2", "دستیار گردشگری", "tourism"),
            ("img3.png", "Article", "دستیار علمی", "textpage3"),
        ]

        for img, circle_target, text, rect_target in items:

            row = FloatLayout(size_hint_y=None, height=220)



            # دکمه مستطیلی اول — فاصله بیشتر از دایره
            rect_btn_1 = RedRoundButton(
                text=gd(re(text)),
                font_name="Far_Nazanin.ttf",
                size_hint=(0.5, 0.2),
                height=90,
                pos_hint={"center_y": 0.65, "x": 0.32}
            )
            rect_btn_1.bind(on_release=lambda x, t=rect_target: setattr(self.manager, "current", t))
            row.add_widget(rect_btn_1)

            # دکمه مستطیلی دوم — فاصله بیشتر از دایره
            rect_btn_2 = GreenRoundButton(
                text=gd(re("مقالات")),
                font_name="Far_Nazanin.ttf",
                size_hint=(0.5, 0.2),
                height=90,
                pos_hint={"center_y": 0.30, "x": 0.32}
            )
            rect_btn_2.bind(on_release=lambda x, t=circle_target: setattr(self.manager, "current", t))
            row.add_widget(rect_btn_2)

            main_layout.add_widget(row)

        scroll.add_widget(main_layout)
        self.add_widget(scroll)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos


