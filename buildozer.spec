[app]
title = KivyApp
package.name = kivyapp
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 1

android.api = 33
android.minapi = 21

# 🔴 خیلی مهم
android.sdk_build_tools = 33.0.2
android.ndk = 25b

android.accept_sdk_license = True
android.enable_androidx = True
android.permissions = INTERNET

log_level = 2
