from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
# Set the window size
Window.size = (400, 700)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'NotifikasiPasien.kv')
Builder.load_file(kv_path)

class NotificationScreen(Screen):
    pass