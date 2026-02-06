[app]

title = MyKivyApp
package.name = mykivyapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf

version = 0.1

requirements = python3,kivy,arabic_reshaper,python-bidi

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.private_storage = True

log_level = 2
