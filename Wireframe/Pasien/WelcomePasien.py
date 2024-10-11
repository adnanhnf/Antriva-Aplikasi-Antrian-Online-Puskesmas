from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

# Set the window size to match a typical mobile screen
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class LoginScreen(BoxLayout):
    def login(self):
        # Add login logic here
        print("Login button pressed")

class WelcomePasien(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    WelcomePasien().run()