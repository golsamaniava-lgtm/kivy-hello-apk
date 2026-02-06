from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from arabic_reshaper import reshape as re
from bidi.algorithm import get_display as gd

from round_button import RoundButton   # ← مهم

from kivy.core.window import Window

# # تنظیم ابعاد پنجره به اندازه‌ی موبایل
# Window.size = (360, 640)

class ClickableLabel(ButtonBehavior, Label):
    pass


class ArticlePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # پس‌زمینه سفید
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # اسکرول
        scroll = ScrollView(size_hint=(1, 1))

        # لایهٔ اصلی
        main_layout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=25,
            padding=20
        )
        main_layout.bind(minimum_height=main_layout.setter("height"))

        # لیست عکس‌ها و صفحات مقصد
        items = [
            ("nano.jpg", "nano", "ایران قوی در فناوری نانو"),
            ("hasteyi.jpg", "page2", "ایران قوی در فناوری هسته ای"),
            ("moshaki.jpg", "page3", "ایران قوی در سلاح موشکی"),
            ("energy.jpg", "page4", "ایران قوی در انرژی های پاک"),
        ]

        for img_src, target_page, label_text in items:

            row = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=260,
                spacing=10
            )

            img = Image(
                source=img_src,
                size_hint=(1, None),
                height=200,
                allow_stretch=True,
                keep_ratio=False
            )

            lbl = ClickableLabel(
                text=gd(re(label_text)),
                font_name="Far_Nazanin.ttf",
                font_size=20,
                size_hint=(1, None),
                height=40,
                halign="right",
                valign="middle",
                color=(0, 0, 0, 1)
            )
            lbl.bind(on_release=lambda x, t=target_page: setattr(self.manager, "current", t))
            lbl.bind(size=lambda inst, val: setattr(inst, "text_size", val))

            row.add_widget(img)
            row.add_widget(lbl)

            main_layout.add_widget(row)

        # ----------------------------------------------------
        # دکمهٔ گرد انتهایی (RoundButton)
        # ----------------------------------------------------
        bottom_btn = RoundButton(
            text=gd(re("بازگشت")),
            font_name="Far_Nazanin.ttf",
            font_size=20,
            size_hint=(0.2, None),
            height=70
        )

        # رنگ آبی کم‌رنگ
        bottom_btn.normal_color = (0.4, 0.6, 1, 1)
        bottom_btn.pressed_color = (0.3, 0.5, 0.9, 1)

        # لینک صفحهٔ مقصد
        bottom_btn.bind(on_release=lambda x: setattr(self.manager, "current", "third"))

        # فاصله از آخرین آیتم
        main_layout.add_widget(BoxLayout(size_hint_y=None, height=30))
        main_layout.add_widget(bottom_btn)
        # ----------------------------------------------------

        scroll.add_widget(main_layout)
        self.add_widget(scroll)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos
