[app]

# App information
title = Nymala Academy
package.name = nymalaacademy
package.domain = com.nymala

# Source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

# Version
version = 1.0

# Requirements
requirements = python3,kivy==2.3.0

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.ndk_api = 24

# Automatically accept Android SDK licenses
android.accept_sdk_license = True

# Build APK instead of AAB
android.debug_artifact = apk
android.release_artifact = apk

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Enable backup
android.allow_backup = True

# Keep screen awake (optional)
android.wakelock = False

# Bootstrap
p4a.bootstrap = sdl2

# Python-for-Android settings
p4a.branch = master

# iOS (unused)
ios.codesign.allowed = false

[buildozer]

# Logging level
log_level = 2

# Warn when running as root
warn_on_root = 1
