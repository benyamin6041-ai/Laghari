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

# --- بخش اصلاح شده برای رفع خطای نسخه ---
# (str) Application version
version = 0.1

# (str) Application version regex
# (این بخش را خالی بگذار تا همان نسخه بالا اعمال شود)
version.regex = 

# --- بقیه تنظیمات ---

# (str) Orientation of the application
orientation = landscape

# (bool) Use orientation sensor
orientation_sensor = True

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (str) Android SDK path
android.sdk_path = 

# (str) Android NDK path
android.ndk_path = 

# (int) Android API to use
android.api = 33

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Android build mode (debug or release)
android.release = False

# (bool) Android accept sdk license
android.accept_sdk_license = True

[buildozer]
log_level = 2
