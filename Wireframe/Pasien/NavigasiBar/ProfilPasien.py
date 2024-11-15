from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from firebase_admin import db

# Set the window size
Window.size = (400, 700)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'ProfilPasien.kv')
Builder.load_file(kv_path)

class ProfilScreen(Screen):
    current_uid = None  # UID pengguna saat ini

    def on_enter(self):
        """Dipanggil setiap kali layar ProfilScreen dibuka."""
        if self.current_uid:
            print(f"Memuat data profil untuk UID: {self.current_uid}")
            self.load_profile_data(self.current_uid)
        else:
            print("UID tidak tersedia. Mengatur label ke default.")
            self.reset_labels()

    def load_profile_data(self, uid):
        """Mengambil data pengguna dari Firebase berdasarkan UID"""
        try:
            user_ref = db.reference(f'users/{uid}')
            user_data = user_ref.get()

            if user_data:
                # Periksa apakah pengguna adalah 'Pasien'
                if user_data.get('role') == 'Pasien':
                    self.ids.nik_label.text = user_data.get('nik', '--')
                    self.ids.name_label.text = user_data.get('name', '--')
                    self.ids.email_label.text = user_data.get('email', '--')
                    self.ids.phone_label.text = user_data.get('no_telp', '--')
                    self.ids.address_label.text = user_data.get('alamat', '--')
                else:
                    print(f"UID {uid} bukan Pasien. Peran: {user_data.get('role', 'Tidak Diketahui')}")
                    self.reset_labels()
            else:
                print(f"Tidak ada data pengguna dengan UID {uid}")
                self.reset_labels()

        except Exception as e:
            print(f"Error mengambil data profil: {e}")
            self.reset_labels()

    def reset_labels(self):
        """Reset semua label ke nilai default"""
        self.ids.nik_label.text = '--'
        self.ids.name_label.text = '--'
        self.ids.email_label.text = '--'
        self.ids.phone_label.text = '--'
        self.ids.address_label.text = '--'

