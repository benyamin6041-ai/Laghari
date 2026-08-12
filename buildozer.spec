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
# نکته مهم: حتما نسخه python و kivy را اینجا چک کن
requirements = python3,kivy

# (str) Orientation of the application
orientation = landscape

# (bool) Use orientation sensor
orientation_sensor = True

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# --- بخش حیاتی برای رفع خطای Aidl و SDK در GitHub Actions ---

# (str) Android SDK path
# در گیت‌هاب، این مسیر را خالی بگذار تا Buildozer از مسیرهای پیش‌فرض سیستم استفاده کند، 
# اما ما در YAML مسیر را ست کرده‌ایم.
android.sdk_path = 

# (str) Android NDK path
android.ndk_path = 

# (int) Android API to use
# استفاده از API 33 یا 34 برای سازگاری با استانداردهای جدید گوگل
android.api = 33

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Android NDK arguments
android.ndk_arguments = force

# (bool) Android arch to build for (android:armeabi-v7a, 16, arm64-v8a, 24, x86, 32)
# برای اکثر گوشی‌های جدید arm64-v8a بهتر است
android.archs = arm64-v8a

# (bool) Android build mode (debug or release)
android.release = False

# (bool) Android use p4a (python-for-android)
android.accept_sdk_license = True

# (list) Android extra requirements
# اگر نیاز به کتابخانه‌های خاصی داری اینجا اضافه کن
android.extras =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Use buildozer to build the app
android.accept_sdk_license = True
