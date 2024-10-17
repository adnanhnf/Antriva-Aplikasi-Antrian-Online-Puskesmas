from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)

class KelolaPasienScreen(BoxLayout):
    def kelola(self, row_number):
        print(f"Kelola button clicked for row {row_number}")

    def tambah_pasien(self):
        print("Tambah Pasien button clicked")

class KelolaPasien(App):
    def build(self):
        return KelolaPasienScreen()

if __name__ == '__main__':
    KelolaPasien().run()