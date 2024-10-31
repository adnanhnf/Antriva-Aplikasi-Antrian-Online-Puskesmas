from kivy.app import App
from kivy.uix.screenmanager import  Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class InformasiAntrianScreen(Screen):
    def panggil_pasien(self):
        # Print a notification message to the terminal
        print("Pasien telah dipanggil !!")

Builder.load_file('NavigasiBar/InfoAntrianPetugas.kv')