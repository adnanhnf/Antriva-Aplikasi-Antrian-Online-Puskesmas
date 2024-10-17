from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)

class KelolaPasienScreen(Screen):
    pass

Builder.load_file('NavigasiBar/KelolaPasien.kv')