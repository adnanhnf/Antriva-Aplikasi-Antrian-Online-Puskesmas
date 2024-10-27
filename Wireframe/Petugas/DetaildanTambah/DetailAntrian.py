from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class DetailAntrianScreen(Screen):
    def pelayanan_selesai(self):
        # Logika untuk menyimpan data
        self.simpan_data()
        
        # Kembali ke Tampilan Informasi Antrian Setelah Menyimpan Data
        App.get_running_app().root.current = 'informasi_antrian'

    def pelayanan_dibatalkan(self):
        # Tidak Menyimpan Data, Langsung Kembali ke Tampilan Informasi Antrian
        App.get_running_app().root.current = 'informasi_antrian'

    def simpan_data(self):
        # Contoh Logika Penyimpanan Data
        print("Data telah disimpan")

Builder.load_file('DetaildanTambah/DetailAntrian.kv')