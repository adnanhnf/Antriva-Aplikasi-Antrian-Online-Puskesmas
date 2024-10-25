from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.lang import Builder
import os
from NavigasiBar.InfoAntrianPetugas import InfoAntrianScreen
from NavigasiBar.KelolaPasien import KelolaPasienScreen

# Set window size   
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class WelcomeScreen(Screen): # Logika Tampilan Welcome Pasien
    def login(self):
        self.manager.current = 'login'

class LoginScreen(Screen): # Logika Tampilan Login Pasien
    def validate_credentials(self): 
        # Mendapatkan input dari user
        email = self.ids.email.text 
        password = self.ids.password.text 
        
        # Validasi email dan password
        if email == 'a' and password == 'a': 
            self.manager.current = 'home' 
        else: 
            self.ids.error_label.text = 'Emails atau password salah.' 
    
    def go_back(self):
        self.manager.current = 'welcome'

class HomeScreen(Screen):
    pass

class MainApp(App):
    def build(self):     
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(InfoAntrianScreen(name='information'))
        sm.add_widget(KelolaPasienScreen(name='kelola'))
        return sm

if __name__ == '__main__':
    MainApp().run()
