from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import  Screen
from kivy.lang import Builder

# Atur Ukuran Layar
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class TambahPasienScreen(Screen):
    def simpan(self):
        # Logika Untuk Menyimpan Data
        self.simpan_data()
        
        # Kembali ke Tampilan Kelola Pasien Setelah Menyimpan Data
        App.get_running_app().root.current = 'kelola_pasien'

    def batal(self):
        # Tidak Menyimpan Data, Langsung Kembali ke Tampilan Kelola Pasien
        App.get_running_app().root.current = 'kelola_pasien'

    def simpan_data(self):
        # Contoh Logika Penyimpanan Data
        print("Data Pasien telah disimpan")

Builder.load_file('DetaildanTambah/TambahPasien.kv')