[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Application version
version = 0.1

# (str) Application version regex
version.regex = 

# (str) Orientation of the application
orientation = landscape

# (bool) Use orientation sensor
orientation_sensor = True

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# --- بخش حیاتی برای رفع خطای مسیر (Path) ---

# این مسیرها را خالی می‌گذاریم تا Buildozer خودش در پوشه home کاربر آن‌ها را بسازد
# و از مسیرهای سیستم (مثل /usr/lib) که اجازه دسترسی نداریم استفاده نکند
android.sdk_path = 
android.ndk_path = 

# تنظیم API برای هماهنگی با لاگ شما
android.api = 33
android.ndk_api = 21

# معماری برای گوشی‌های جدید
android.archs = arm64-v8a

# (bool) Android build mode (debug or release)
android.release = False

# (bool) Android accept sdk license
# این خط بسیار مهم است تا بیلد متوقف نشود
android.accept_sdk_license = True

# --- تنظیمات تکمیلی برای پایداری در CI/CD ---

# استفاده از NDK نسخه مشخص شده در لاگ شما برای جلوگیری از دانلود مجدد و خطا
# اگر در لاگ دیدی نسخه متفاوت است، اینجا تغییر بده. فعلاً مطابق لاگ تو:
# android.ndk_arguments = force

[buildozer]

# سطح لاگ را روی 2 می‌گذاریم تا اگر دوباره شکست خورد، دقیقاً بدانیم کجاست
log_level = 2
