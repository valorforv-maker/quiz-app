[app]
title = Bilgi Yarismasi
package.name = bilgiyarismasi
package.domain = com.myapp

source.dir = .
# Eğer oyununa ikon veya ses eklersen buraya wav,mp3,ttf eklemeyi unutma
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0

# setuptools eklemek paketleme hatalarını önler
requirements = python3,pygame-ce,setuptools

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

# Modern uyumluluk için
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
