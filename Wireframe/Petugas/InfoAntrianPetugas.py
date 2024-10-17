from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size
Window.size = (400, 700)

class InfoAntrianScreen(BoxLayout):
    def detail(self, row_number):
        print(f"Detail button clicked for row {row_number}")

class InfoAntrianPetugas(App):
    def build(self):
        return InfoAntrianScreen()

if __name__ == '__main__':
    InfoAntrianPetugas().run()