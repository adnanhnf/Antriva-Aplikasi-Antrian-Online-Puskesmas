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
        self.antrian_selesai()
        
        # Kembali ke Tampilan Informasi Antrian Setelah Pelayanan Selesai
        App.get_running_app().root.current = 'informasi_antrian'

    def pelayanan_dibatalkan(self):
        # Logika untuk menyimpan data
        self.antrian_batal()
        
        # Kembali ke Tampilan Informasi Antrian Setelah Pelayanan Dibatalkan
        App.get_running_app().root.current = 'informasi_antrian'

    def antrian_selesai(self):
        # Contoh Logika Penyimpanan Data
        print("Antrian ini telah selesai !!")
    
    def antrian_batal(self):
        # Contoh Logika Penyimpanan Data
        print("Antrian ini telah dibatalkan !!")
    
    def kembali(self):
        self.manager.current = 'informasi_antrian'

Builder.load_file('DetaildanTambah/DetailAntrian.kv')