from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size like in previous screens
Window.size = (400, 700)

class TambahPasienScreen(BoxLayout):
    def back(self):
        print("Back button pressed")
    
    def add_patient(self):
        print("Add patient button pressed")
    
    def cancel(self):
        print("Cancel button pressed")

class TambahPasien(App):
    def build(self):
        return TambahPasienScreen()

if __name__ == '__main__':
    TambahPasien().run()