from kivy.app import App
from kivy.uix.screenmanager import  Screen
from kivy.core.window import Window
from kivy.lang import Builder
from Pasien.NavigasiBar.NotifikasiPasien import NotificationScreen

# Set the window size
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class InformasiAntrianScreen(Screen):
    def panggil_pasien(self):
        # Memanggil fungsi notifikasi dari NotifikasiPasien
        NotificationScreen.tampilkan_notifikasi("Pasien telah dipanggil")


Builder.load_file('NavigasiBar/InfoAntrianPetugas.kv')