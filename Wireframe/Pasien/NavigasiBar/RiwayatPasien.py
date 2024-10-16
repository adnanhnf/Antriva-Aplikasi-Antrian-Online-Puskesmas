from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size to match your previous settings
Window.size = (400, 700)

class HistoryScreen(Screen):
    pass

Builder.load_file('NavigasiBar/RiwayatPasien.kv')