from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)

class DetailPasienScreen(Screen):
    def go_back(self):
        # Fungsi ini akan digunakan untuk aksi tombol back, misalnya untuk kembali ke layar sebelumnya
        print("Back button pressed")

class DetailPasien(App):
    def build(self):
        return DetailPasienScreen()

# Load the KV file
Builder.load_file('DetailPasien.kv')

if __name__ == "__main__":
    DetailPasien().run()