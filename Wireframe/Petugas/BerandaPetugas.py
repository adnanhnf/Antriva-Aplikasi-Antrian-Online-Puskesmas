from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size like the WelcomePetugas screen
Window.size = (400, 700)

class BerandaScreen(BoxLayout):
    def go_to_info_antrian(self):
        print("Navigating to Info Antrian")

    def go_to_kelola_pasien(self):
        print("Navigating to Kelola Pasien")

class BerandaPetugas(App):
    def build(self):
        return BerandaScreen()

if __name__ == '__main__':
    BerandaPetugas().run()