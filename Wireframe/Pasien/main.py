from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, DictProperty, BooleanProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os
from NavigasiBar.InfoAntrian import InfoQueueScreen
from NavigasiBar.RiwayatPasien import HistoryScreen
from NavigasiBar.ProfilPasien import ProfilScreen
from NavigasiBar.NotifikasiPasien import NotificationScreen

# Set window size
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class WelcomeScreen(Screen): # Logika Tampilan Welcome Pasien !!
    def login(self):
        self.manager.current = 'login'

class LoginScreen(Screen): # Logika Tampilan Login Pasien !!
    def validate_credentials(self): 
        # Mendapatkan input dari user
        email = self.ids.email.text 
        password = self.ids.password.text 
        
        # Validasi email dan password
        if email == 'a' and password == 'a': 
            self.manager.current = 'home' 
        else: 
            self.ids.error_label.text = 'Email atau password salah.' 
    
    def go_back(self):
        self.manager.current = 'welcome'

class PoliBox(BoxLayout): # Logika Tampilan Beranda Pasien !!
    poli_id = StringProperty('')
    poli_name = StringProperty('')  # Properti untuk nama poli
    status_text = StringProperty('Tersedia')  # Default status
    is_available = BooleanProperty(True)

    def on_poli_id(self, instance, value):
        app = App.get_running_app()
        if app and app.root:
            poli_data = app.root.poli_status.get(value, {})
            self.poli_name = poli_data.get('name', '')  # Ambil nama poli
            self.update_status(poli_data.get('available', False))  # Perbarui status

    def update_status(self, status):
        self.is_available = status
        # Mengupdate status menjadi teks
        self.status_text = 'Tersedia' if status else 'Tidak\nTersedia'

class HomeScreen(Screen):
    poli_status = DictProperty({
        'A': {'name': 'Poli Umum', 'available': True},
        'B': {'name': 'Poli Gigi', 'available': True},
        'C': {'name': 'Poli Anak', 'available': False},
        'D': {'name': 'Poli KIA', 'available': True}
    })

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_number = 0
        # Memanggil on_poli_status pada inisialisasi
        self.on_poli_status(self, self.poli_status)

    def on_poli_status(self, instance, value):
        # Update semua PoliBox widget ketika poli_status berubah
        for poli_id in value:
            if hasattr(self.ids, f'poli_{poli_id.lower()}'):
                poli_box = getattr(self.ids, f'poli_{poli_id.lower()}')
                poli_box.poli_id = poli_id  # Menetapkan poli_id untuk setiap PoliBox
                poli_box.update_status(value[poli_id]['available'])
                poli_box.poli_name = value[poli_id]['name']  # Mengatur nama poli

class TakeTheQueueScreen(Screen):
    def go_back(self):
        self.manager.current = 'home'
    
    def cancel(self):
        self.manager.current = 'home'    
    
    def ambil_antrian(self):
        self.manager.current = 'information'

class MainApp(App):
    def build(self):     
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TakeTheQueueScreen(name='takethequeue'))
        sm.add_widget(InfoQueueScreen(name= 'information'))
        sm.add_widget(HistoryScreen(name= 'history'))
        sm.add_widget(ProfilScreen(name= 'profil'))
        sm.add_widget(NotificationScreen(name= 'notification'))
        return sm

if __name__ == '__main__':
        MainApp().run()