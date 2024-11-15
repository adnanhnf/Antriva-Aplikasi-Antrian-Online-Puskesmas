from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from kivy.properties import NumericProperty, StringProperty
from datetime import datetime, timedelta
from firebase_admin import auth, db
from kivy.clock import Clock

# Set the window size like in previous screens
Window.size = (400, 700)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'InfoAntrian.kv')
Builder.load_file(kv_path)

class InfoQueueScreen(Screen):
    current_queue = NumericProperty(0)
    your_queue = NumericProperty(0)
    estimated_time = StringProperty('00:00')
    remaining_minutes = NumericProperty(0)
    remaining_seconds = NumericProperty(0)
    update_event = None
    timer_event = None

    def on_enter(self):
        # Mulai update periodik saat masuk screen
        self.start_updates()

    def on_leave(self):
        # Hentikan update saat keluar screen
        self.stop_updates()

    def start_updates(self):
        # Update setiap 5 detik
        self.update_event = Clock.schedule_interval(lambda dt: self.update_queue_info(), 5)
        # Update timer setiap detik
        self.timer_event = Clock.schedule_interval(lambda dt: self.update_timer(), 1)
        # Update pertama kali
        self.update_queue_info()

    def stop_updates(self):
        if self.update_event:
            self.update_event.cancel()
        if self.timer_event:
            self.timer_event.cancel()

    def update_timer(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        elif self.remaining_minutes > 0:
            self.remaining_minutes -= 1
            self.remaining_seconds = 59
        
        self.estimated_time = f'{self.remaining_minutes:02d}:{self.remaining_seconds:02d}'

    def update_queue_info(self):
        try:
            app = App.get_running_app()
            user_email = app.current_user_email
            if not user_email:
                return

            user = auth.get_user_by_email(user_email)
            uid = user.uid

            # Ambil data antrian aktif user
            antrian_ref = db.reference('antrian_aktif').child(uid)
            antrian_data = antrian_ref.get()

            if antrian_data:
                today = datetime.now().strftime('%Y-%m-%d')
                if antrian_data['tanggal_antrian'] == today:
                    poli = antrian_data['poli']
                    self.your_queue = antrian_data['nomor_antrian']
                    
                    # Ambil dan update nomor antrian yang sedang dilayani
                    poli_ref = db.reference(f'antrian_harian/{today}/{poli}')
                    poli_data = poli_ref.get() or {}
                    
                    # Ambil current_number, jika None maka gunakan 0
                    current_number = poli_data.get('current_number', 0)
                    
                    # Update current_queue hanya jika berbeda dari nilai sekarang
                    if self.current_queue != current_number:
                        self.current_queue = current_number
                        
                        # Hitung ulang estimasi waktu
                        queue_difference = max(0, self.your_queue - self.current_queue)
                        total_minutes = queue_difference * 5  # 5 menit per pasien
                        
                        self.remaining_minutes = total_minutes
                        self.remaining_seconds = 0
                else:
                    # Reset jika bukan hari ini
                    self.reset_queue_info()
            else:
                self.reset_queue_info()

        except Exception as e:
            print(f"Error updating queue info: {e}")

    def reset_queue_info(self):
        self.your_queue = 0
        self.current_queue = 0
        self.remaining_minutes = 0
        self.remaining_seconds = 0
        self.estimated_time = '00:00'

    def on_current_queue(self, instance, value):
        if hasattr(self, 'ids'):
            self.ids.current_queue_label.text = f'{value:03d}'

    def on_your_queue(self, instance, value):
        if hasattr(self, 'ids'):
            self.ids.your_queue_label.text = f'{value:03d}'

    def on_estimated_time(self, instance, value):
        if hasattr(self, 'ids'):
            self.ids.estimated_time_label.text = f'ESTIMASI WAKTU {value}'