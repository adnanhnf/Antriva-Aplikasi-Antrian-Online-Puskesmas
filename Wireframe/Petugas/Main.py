from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from NavigasiBar.InfoAntrianPetugas import InformasiAntrianScreen
from NavigasiBar.KelolaPasien import KelolaPasienScreen
from DetaildanTambah.DetailAntrian import DetailAntrianScreen
from DetaildanTambah.DetailPasien import DetailPasienScreen
from DetaildanTambah.TambahPasien import TambahPasienScreen

# Set window size   
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class HalamanAwalScreen(Screen): # Logika Tampilan Welcome Pasien
    def login(self):
        self.manager.current = 'login'

class LoginScreen(Screen): # Logika Tampilan Login Pasien
    def validasi_kredensial(self): 
        # Mendapatkan input dari user
        email = self.ids.email.text 
        password = self.ids.password.text 
        
        # Validasi Email dan Password
        if email == 'a' and password == 'a': 
            self.manager.current = 'beranda_petugas' 
        else: 
            self.ids.error_label.text = 'Email atau password salah.' 
    
    def kembali(self):
        self.manager.current = 'halaman_awal'

class BerandaPetugasScreen(Screen):
    pass

class MainApp(App):
    def build(self):     
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(HalamanAwalScreen(name='halaman_awal'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(BerandaPetugasScreen(name='beranda_petugas'))
        sm.add_widget(InformasiAntrianScreen(name='informasi_antrian'))
        sm.add_widget(DetailAntrianScreen(name='detail_antrian'))
        sm.add_widget(KelolaPasienScreen(name='kelola_pasien'))
        sm.add_widget(DetailPasienScreen(name='detail_pasien'))
        sm.add_widget(TambahPasienScreen(name='tambah_pasien'))
        return sm

if __name__ == '__main__':
    MainApp().run()
