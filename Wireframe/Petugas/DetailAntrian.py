from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Set the window size
Window.size = (400, 700)

class DetailAntrianScreen(BoxLayout):
    def go_to_beranda(self):
        # Navigasi ke halaman Beranda
        print("Navigating to Beranda")

    def go_to_info_antrian(self):
        # Navigasi ke halaman Info Antrian
        print("Navigating to Info Antrian")

    def go_to_kelola_pasien(self):
        # Navigasi ke halaman Kelola Pasien
        print("Navigating to Kelola Pasien")

    def pelayanan_selesai(self):
        # Logika ketika pelayanan selesai
        print("Pelayanan Selesai")

    def pelayanan_dibatalkan(self):
        # Logika ketika pelayanan dibatalkan
        print("Pelayanan Dibatalkan")

class DetailAntrian(App):
    def build(self):
        return DetailAntrianScreen()

if __name__ == '__main__':
    DetailAntrian().run()