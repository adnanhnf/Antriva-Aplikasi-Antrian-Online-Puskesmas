import os
import sys
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, DictProperty, BooleanProperty
import pyrebase
from firebase_admin import credentials, initialize_app, db, auth
import firebase_admin

# Konfigurasi window
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

# Menambahkan path untuk mengimpor modul dari direktori lain
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mengimpor file konfigurasi Firebase
from config import get_firebase_config

# Mengimpor screen pasien
from Pasien.BerandaPasien import HomeScreen, TakeTheQueueScreen
from Pasien.NavigasiBar.InfoAntrian import InfoQueueScreen
from Pasien.NavigasiBar.RiwayatPasien import HistoryScreen
from Pasien.NavigasiBar.ProfilPasien import ProfilScreen
from Pasien.NavigasiBar.NotifikasiPasien import NotificationScreen

# Mengimpor screen petugas
from Petugas.BerandaPetugas import BerandaPetugasScreen
from Petugas.NavigasiBar.InfoAntrianPetugas import InformasiAntrianScreen
from Petugas.NavigasiBar.KelolaPasien import KelolaPasienScreen
from Petugas.DetaildanTambah.DetailAntrian import DetailAntrianScreen
from Petugas.DetaildanTambah.DetailPasien import DetailPasienScreen
from Petugas.DetaildanTambah.TambahPasien import TambahPasienScreen
from Petugas.DetaildanTambah.EditPasien import EditPasienScreen

# Inisialisasi Firebase
config = get_firebase_config()
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

class HalamanAwalScreen(Screen):
    """Logika Tampilan Welcome Pasien"""
    def login(self):
        self.manager.current = 'login'

class LoginScreen(Screen):
    def validasi_kredensial(self):
        email = self.ids.email.text
        password = self.ids.password.text

        # Validasi input dasar
        if not email or not password:
            self.ids.error_label.text = "Email dan password harus diisi"
            return

        login_success, message = self.login(email, password)
        if not login_success:
            self.ids.error_label.text = message

    def login(self, email, password):
        try:
            # Login ke Firebase Authentication
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']       # ID pengguna dari Firebase Authentication
            id_token = user['idToken']      # Token autentikasi untuk mengakses database

            # Ambil data pengguna dari Realtime Database
            user_data = db.child("users").child(user_id).get(token=id_token).val()
            print("Data Pengguna:", user_data)

            if not user_data:
                return False, "Data pengguna tidak ditemukan"
            elif 'role' not in user_data:
                return False, "Role tidak ditemukan dalam data pengguna"
            print("Role pengguna:", user_data['role'])

            # Lakukan tindakan berdasarkan role
            app = App.get_running_app()
            app.user_role = user_data['role']
            app.user_id = user_id
            app.current_user_email = user_data['email']

            if user_data['role'] == 'Petugas':
                self.manager.current = 'beranda_petugas'
                print("Berpindah ke beranda petugas")
            elif user_data['role'] == 'Pasien':
                # Set UID untuk ProfilScreen setelah login berhasil
                profil_screen = self.manager.get_screen('profil')  # Ambil instance ProfilScreen
                profil_screen.current_uid = user_id  # Simpan UID pengguna yang login

                self.manager.current = 'home'  # Pindah ke halaman beranda pasien
                print("Berpindah ke beranda pasien")
            else:
                return False, f"Role tidak dikenal: {user_data['role']}"

            return True, "Login berhasil"

        except Exception as e:
            print(f"Error login: {e}")
            return False, "Gagal login. Silakan coba lagi."

    def kembali(self):
        self.manager.current = 'halaman_awal'

class MainApp(App):
    def build(self):     
        # Initialize Firebase once in main.py
        if not firebase_admin._apps:
            cred = credentials.Certificate('D:/Projek Antrian Online Puskesmas/Wireframe/firebase_admin_sdk.json') # tempat lokasi file json
            initialize_app(cred, {
                'databaseURL': 'https://antrian-online-puskesmas-default-rtdb.firebaseio.com/' # isi url database di firebase
            })
            
        # Buat ScreenManager
        sm = ScreenManager()
        sm.add_widget(HalamanAwalScreen(name='halaman_awal'))
        sm.add_widget(LoginScreen(name='login'))
        # Screen pasien
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TakeTheQueueScreen(name='takethequeue'))
        sm.add_widget(InfoQueueScreen(name='information'))
        sm.add_widget(HistoryScreen(name='history'))
        sm.add_widget(ProfilScreen(name='profil'))
        sm.add_widget(NotificationScreen(name='notification'))
        # Screen petugas
        sm.add_widget(BerandaPetugasScreen(name='beranda_petugas'))
        sm.add_widget(InformasiAntrianScreen(name='informasi_antrian'))
        sm.add_widget(DetailAntrianScreen(name='detail_antrian'))
        sm.add_widget(KelolaPasienScreen(name='kelola_pasien'))
        sm.add_widget(DetailPasienScreen(name='detail_pasien'))
        sm.add_widget(TambahPasienScreen(name='tambah_pasien'))
        sm.add_widget(EditPasienScreen(name='edit_pasien'))
        return sm

if __name__ == '__main__':
    MainApp().run()
