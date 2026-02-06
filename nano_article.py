from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle

from arabic_reshaper import reshape as re
from bidi.algorithm import get_display as gd


# ایمیج قابل کلیک
class ClickableImage(ButtonBehavior, Image):
    pass


class NanoPage(Screen):
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

        # -------------------------------
        #  لیبل عنوان
        # -------------------------------
        title_text = "پیشرفت‌های ایران در فناوری نانو"
        title_label = Label(
            text=gd(re(title_text)),
            font_name="Far_Nazanin.ttf",
            font_size=32,
            size_hint_y=None,
            height=60,
            halign="center",
            valign="middle",
            color=(0, 0, 0, 1)
        )
        title_label.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        main_layout.add_widget(title_label)

        # -------------------------------
        #  متن ۵۰۰ کلمه‌ای
        # -------------------------------
        nano_text = """
ایران طی دو دههٔ اخیر توانسته است جایگاه ویژه‌ای در حوزهٔ فناوری نانو به دست آورد و به یکی از کشورهای پیشرو در این عرصه تبدیل شود. توسعهٔ فناوری نانو در ایران از اوایل دههٔ ۱۳۸۰ با تدوین برنامه‌های ملی و ایجاد ستاد ویژهٔ توسعهٔ فناوری نانو آغاز شد. این ستاد با هدف‌گذاری دقیق، حمایت از پژوهشگران، ایجاد زیرساخت‌های آزمایشگاهی و تشویق صنایع به استفاده از فناوری‌های نوین، مسیر رشد این حوزه را هموار کرد. یکی از مهم‌ترین عوامل موفقیت ایران در این زمینه، سرمایه‌گذاری گسترده در آموزش و تربیت نیروی انسانی متخصص بوده است. دانشگاه‌های کشور رشته‌ها و گرایش‌های مرتبط با نانو را راه‌اندازی کردند و هزاران دانشجو در مقاطع مختلف در این حوزه آموزش دیدند. این روند باعث شد ایران از نظر تولید مقالات علمی در حوزهٔ نانو به رتبه‌های بالای جهانی برسد و در برخی سال‌ها حتی در میان پنج کشور برتر دنیا قرار گیرد.

پیشرفت ایران تنها به تولید علم محدود نمانده و در حوزهٔ تجاری‌سازی نیز دستاوردهای قابل توجهی داشته است. صدها شرکت دانش‌بنیان در زمینهٔ تولید محصولات نانویی شکل گرفته‌اند که در حوزه‌هایی مانند پزشکی، داروسازی، نساجی، ساختمان، آب و محیط زیست فعالیت می‌کنند. برای مثال، تولید نانوفیلترهای تصفیهٔ آب، رنگ‌های نانویی ضدباکتری، داروهای مبتنی بر نانوذرات و تجهیزات پزشکی پیشرفته از جمله محصولاتی هستند که در داخل کشور توسعه یافته و حتی به بازارهای جهانی صادر می‌شوند. ایران همچنین موفق شده است استانداردهای ملی و بین‌المللی مرتبط با فناوری نانو را تدوین و اجرا کند که این امر نقش مهمی در افزایش کیفیت محصولات و اعتماد بازار داشته است.

در حوزهٔ زیرساخت، ایران شبکهٔ گسترده‌ای از آزمایشگاه‌های تخصصی نانو ایجاد کرده که به پژوهشگران و شرکت‌ها خدمات پیشرفته ارائه می‌دهند. این آزمایشگاه‌ها مجهز به دستگاه‌های مدرن مانند میکروسکوپ‌های الکترونی، سیستم‌های سنتز نانوذرات و تجهیزات تحلیل سطح هستند. وجود چنین زیرساخت‌هایی باعث شده پژوهشگران ایرانی بتوانند پروژه‌های پیچیده و کاربردی را در داخل کشور انجام دهند. علاوه بر این، ایران در زمینهٔ ثبت اختراع نیز رشد چشمگیری داشته و تعداد زیادی پتنت در حوزهٔ نانو در داخل و خارج از کشور به ثبت رسانده است.

در مجموع، پیشرفت‌های ایران در فناوری نانو نتیجهٔ ترکیب هوشمندانهٔ سیاست‌گذاری، آموزش، پژوهش، زیرساخت و تجاری‌سازی است. این روند نشان می‌دهد که با برنامه‌ریزی دقیق و حمایت مستمر، می‌توان در حوزه‌های پیشرفتهٔ علمی و فناوری به جایگاه‌های برتر جهانی دست یافت. آیندهٔ فناوری نانو در ایران روشن به نظر می‌رسد و انتظار می‌رود با ادامهٔ این مسیر، سهم کشور در بازار جهانی محصولات نانویی افزایش یابد و نقش مهم‌تری در اقتصاد دانش‌بنیان ایفا کند.
        """

        body_label = Label(
            text=gd(re(nano_text)),
            font_name="Far_Nazanin.ttf",
            font_size=18,
            size_hint_y=None,
            halign="right",
            valign="top",
            color=(0, 0, 0, 1)
        )
        body_label.bind(
            texture_size=lambda inst, val: setattr(inst, "height", inst.texture_size[1]),
            size=lambda inst, val: setattr(inst, "text_size", val)
        )
        main_layout.add_widget(body_label)

        # -------------------------------
        #  تصویر نواری پایین صفحه
        # -------------------------------
        img = ClickableImage(
            source="Images/nanolink.jpg",
            size_hint=(1, None),
            height=200,
            allow_stretch=True,
            keep_ratio=False
        )
        img.bind(on_release=lambda x: setattr(self.manager, "current", "Article"))
        main_layout.add_widget(img)

        scroll.add_widget(main_layout)
        self.add_widget(scroll)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos
