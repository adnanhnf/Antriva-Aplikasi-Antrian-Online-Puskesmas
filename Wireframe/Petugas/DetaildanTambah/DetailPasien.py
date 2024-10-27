from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Atur Ukuran Layar
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class DetailPasienScreen(Screen):
    def kembali(self):
        self.manager.current = 'kelola_pasien'

# Memuat file KV
Builder.load_file('DetaildanTambah/DetailPasien.kv')
