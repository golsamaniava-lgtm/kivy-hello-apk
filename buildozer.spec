[app]

title = IranTourism
package.name = irantourism
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,ttf

version = 0.1

requirements = python3,kivy==2.3.1,arabic_reshaper,python-bidi

orientation = portrait

fullscreen = 0

icon.filename = %(source.dir)s/icon.png

presplash.filename = %(source.dir)s/presplash.png


[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

android.api = 31
android.minapi = 21

android.sdk = 31
android.ndk = 25b

android.permissions = INTERNET

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

android.allow_backup = True

android.gradle_dependencies = 

android.enable_androidx = True

android.enable_jetifier = True

android.use_aapt2 = True

android.ndk_api = 21


[app:android.gradle]

# خالی بماند


[app:android.signing]

# خالی بماند
