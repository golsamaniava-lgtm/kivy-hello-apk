[app]

title = Tourism App
package.name = tourismapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,kv

# فایل اصلی
entrypoint = main.py

# فایل‌ها و فولدرهای اضافی
source.include_patterns = Images/*,widgets/*,Far_Nazanin.ttf

# نسخه
version = 0.1

# نیازمندی‌های پایتون
requirements = python3,kivy,arabic_reshaper,python-bidi

# حداقل اندروید
android.minapi = 21

# معماری‌ها
android.archs = arm64-v8a,armeabi-v7a

# مجوزها (فعلاً هیچی لازم نداری)
android.permissions =

# فول‌اسکرین
fullscreen = 1

# لاگ کمتر (پایدارتر)
log_level = 2


[buildozer]

log_level = 2
warn_on_root = 1
