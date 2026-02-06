from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from first_page import FirstPage
from third_page import ThirdPage
from Article import ArticlePage
from shop import ShopPage
from tourism import tourismpage
from nano_article import NanoPage
from kivy.core.window import Window

# # تنظیم ابعاد پنجره به اندازه‌ی موبایل
# Window.size = (360, 640)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstPage(name="first"))
        sm.add_widget(ThirdPage(name="third"))
        sm.add_widget(ArticlePage(name="Article"))
        sm.add_widget(ShopPage(name="shop"))
        sm.add_widget(tourismpage(name="tourism"))
        sm.add_widget(NanoPage(name="nano"))

        return sm


if __name__ == "__main__":
    MyApp().run()
