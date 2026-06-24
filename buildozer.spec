[app]

title = Nymala Academy
package.name = nymalaacademy
package.domain = com.nymala

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 1.0

# IMPORTANT: stable Kivy version
requirements = python3,kivy==2.1.0
python.version = 3.10

orientation = portrait
fullscreen = 0

# Android settings (stable)
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

android.archs = arm64-v8a, armeabi-v7a

# Accept licenses (fix your previous error)
android.accept_sdk_license = True

android.allow_backup = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
