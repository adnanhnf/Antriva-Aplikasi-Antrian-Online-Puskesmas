from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size like in previous screens
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class AmbilAntrianScreen(BoxLayout):
    def back(self):
        print("Back button pressed")
    
    def ambil_antrian(self):
        print("Ambil antrian button pressed")
    
    def cancel(self):
        print("Cancel button pressed")

class AmbilAntrianApp(App):
    def build(self):
        return AmbilAntrianScreen()

if __name__ == '__main__':
    AmbilAntrianApp().run()