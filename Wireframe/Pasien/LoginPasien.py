from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# Set window size and color
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class LoginScreen(BoxLayout):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def login(self):
        # Add login logic here
        print(f"Login attempt with username: {self.username.text}")
        print(f"Password: {self.password.text}")

class LoginPasien(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginPasien().run()