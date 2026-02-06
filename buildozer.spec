[app]

# اسم برنامه
title = اIran

# اسم پکیج (فقط حروف کوچیک)
package.name = mykivyapp
package.domain = org.test

# فایل اصلی
source.dir = .
source.main = main.py

# فایل‌هایی که باید برن داخل apk
source.include_exts = py,kv,png,jpg,jpeg,ttf

# فولدرهایی که داری
source.include_patterns = image/*,widgets/*

# نسخه
version = 0.1

# کتابخونه‌ها
requirements = python3,kivy,python-bidi,arabic-reshaper

# اندروید
orientation = portrait
fullscreen = 1

android.api = 31
android.minapi = 21
android.ndk = 25b

# معماری (همینو نگه دار)
android.archs = arm64-v8a,armeabi-v7a

# جاوا
android.gradle_dependencies = implementation 'androidx.appcompat:appcompat:1.6.1'

# لاگ بیشتر (برای دیباگ)
log_level = 2

[buildozer]
warn_on_root = 0
