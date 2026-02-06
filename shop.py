from arabic_reshaper import reshape as re
from bidi.algorithm import get_display as gd
import itertools
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.screenmanager import Screen

Window.clearcolor = (1, 1, 1, 1)

prices = {
    "نان": 30000,
    "برنج": 450000,
    "ماکارونی": 60000,
    "آرد": 70000,
    "شکر": 80000,
    "نمک": 50000,
    "روغن": 300000,
    "کره": 90000,
    "شیر": 60000,
    "پنیر": 140000,
    "ماست": 150000,
    "تخم مرغ": 350000,
    "گوشت قرمز": 1600000,
    "مرغ": 240000,
    "ماهی": 500000,
    "عدس":  340000,
    "لوبیا": 550000,
    "نخود":  300000,
    "سیب زمینی": 45000,
    "پیاز": 40000,
    "گوجه فرنگی": 50000,
    "خیار": 60000,
    "هویج": 40000,
    "کاهو": 50000,
    "سیب": 100000,
    "پرتقال": 85000,
    "موز": 170000,
    "خرما": 350000,
    "چای": 1200000,
    "قهوه": 1500000
}


class MultiStateCheckBox(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click_count = 0
        self.background_normal = ''
        self.bind(on_release=self.on_click)

    def on_click(self, *args):
        self.click_count += 1
        if self.click_count > 2:
            self.click_count = 0
        self.update_tick()

    def update_tick(self):
        self.canvas.after.clear()
        if self.click_count == 1:
            with self.canvas.after:
                Color(0, 1, 0, 1)
                Line(points=[self.x + 3, self.y + 10, self.x + 8, self.y + 3, self.x + 17, self.y + 20], width=2)
        elif self.click_count == 2:
            with self.canvas.after:
                Color(1, 0, 0, 1)
                Line(points=[self.x + 3, self.y + 10, self.x + 8, self.y + 3, self.x + 17, self.y + 20], width=2)


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=15, padding=15, **kwargs)

        # سقف قیمت
        price_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        price_label = Label(text=gd(re("سقف قیمت")), font_name='Far_Nazanin.ttf',
                            size_hint_x=0.3, color=(0, 0, 0, 1))
        self.price_input = TextInput(hint_text=gd(re("عدد وارد کنید")),
                                     font_name='Far_Nazanin.ttf',
                                     input_filter='int', multiline=False,
                                     size_hint_x=0.4, height=30,
                                     foreground_color=(0, 0, 0, 1))
        price_layout.add_widget(self.price_input)
        price_layout.add_widget(price_label)

        # مواد غذایی
        product_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=450)
        product_label = Label(text=gd(re("مواد غذایی اساسی")),
                              font_name='Far_Nazanin.ttf',
                              size_hint_y=None, height=30, color=(0, 0, 0, 1))

        self.food_items = list(prices.keys())
        self.checkboxes = {}

        checkbox_grid = GridLayout(cols=3, spacing=5, padding=5, size_hint_y=None, height=400)

        for item in self.food_items:
            row = BoxLayout(orientation='horizontal', spacing=2, size_hint_y=None, height=30)
            cb = MultiStateCheckBox(size_hint=(None, None), size=(20, 20))
            self.checkboxes[item] = cb
            row.add_widget(cb)
            row.add_widget(Label(text=gd(re(item)), font_name='Far_Nazanin.ttf',
                                 size_hint=(None, None), height=25, width=80, color=(0, 0, 0, 1)))
            checkbox_grid.add_widget(row)

        product_layout.add_widget(product_label)
        product_layout.add_widget(checkbox_grid)

        # دکمه عملیات + لیبل نتیجه
        action_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        action_button = Button(text=gd(re("عملیات")), font_name='Far_Nazanin.ttf',
                               size_hint=(None, None), size=(80, 35),
                               color=(0, 0, 0, 1), background_color=(0, 1, 0, 0.5))
        action_button.bind(on_release=self.calculate)

        self.result_label = Label(text=gd(re("نتایج انتخاب‌ها اینجا نمایش داده می‌شود")),
                                  font_name='Far_Nazanin.ttf', size_hint_x=0.7, color=(0, 0, 0, 1))

        action_layout.add_widget(self.result_label)
        action_layout.add_widget(action_button)

        self.add_widget(price_layout)
        self.add_widget(product_layout)
        self.add_widget(action_layout)

        self.ezafe = 0
        self.lazem = 0

    def calculate(self, *args):
        saghf = int(self.price_input.text) if self.price_input.text.isdigit() else 0
        green_kala = []
        red_kala = []

        for item, cb in self.checkboxes.items():
            if cb.click_count == 1:
                green_kala.append(item)
            elif cb.click_count == 2:
                red_kala.append(item)

        less = min(prices[item] for item in green_kala) if green_kala else None

        kol_kala = green_kala + red_kala
        kol_price = sum(prices[item] for item in kol_kala)
        red_price = sum(prices[item] for item in red_kala)

        if saghf == 0:
            self.result_label.text = gd(re("سقف قیمت را وارد کنید"))
            return

        if red_price > saghf:
            self.result_label.text = gd(re("امکان خرید کالاهای ضروری را هم ندارید"))
            return

        if saghf < less:
            self.result_label.text = gd(re("امکان خرید هیچ یک از کالاها را ندارید"))
            return

        if kol_price <= saghf:
            if kol_price == saghf:
                self.result_label.text = gd(re('خرید موفق'))
                return
            else:
                self.ezafe = saghf - kol_price
                self.result_label.text = gd(re('خرید موفق')) + "\n" + gd(
                    re('باقی مانده {} تومان')).format(self.ezafe)
                return

        self.lazem = kol_price - saghf
        self.result_label.text = gd(re('خرید ناموفق')) + gd(
            re('به {} تومان دیگر نیاز دارید')).format(self.lazem)

        items_to_remove = None

        for r in range(1, len(green_kala) + 1):
            for combo in itertools.combinations(green_kala, r):
                temp_kol_price = kol_price - sum(prices[item] for item in combo)
                if temp_kol_price <= saghf:
                    items_to_remove = combo
                    break
            if items_to_remove:
                break

        if items_to_remove:
            items_str = "، ".join(items_to_remove)
            self.result_label.text += gd(
                re("\nبا حذف کالاهای: {} می‌توانید خرید خود را انجام دهید.")).format(items_str)
        else:
            self.result_label.text += gd(re("\nبا حذف کالاهای سبز نیز امکان رسیدن به سقف قیمت وجود ندارد."))


class ShopPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MyLayout())
