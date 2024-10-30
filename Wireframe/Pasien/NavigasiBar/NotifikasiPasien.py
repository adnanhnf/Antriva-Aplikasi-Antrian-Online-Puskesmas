from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)

class NotificationScreen(Screen):
    @staticmethod
    def tampilkan_notifikasi(pesan):
        print(f"Notifikasi: {pesan}")

Builder.load_file('NavigasiBar/NotifikasiPasien.kv')