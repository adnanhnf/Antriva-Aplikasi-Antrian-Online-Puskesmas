from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from firebase_admin import db

# Atur Ukuran Layar
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'DetailPasien.kv')
Builder.load_file(kv_path)

class DetailPasienScreen(Screen):
    current_uid = None  # Menyimpan UID pasien saat ini

    def on_enter(self):
        # Memuat data pasien saat layar dimasuki
        self.load_patient_details()

    def load_patient_details(self):
        if not self.current_uid:
            print("UID pasien tidak tersedia!")
            return

        # Ambil data pasien dari Firebase Realtime Database
        try:
            patient_ref = db.reference(f'users/{self.current_uid}')
            patient_data = patient_ref.get()
            if patient_data:
                self.ids.email_label.text = patient_data.get('email', '--')
                self.ids.nik_label.text = patient_data.get('nik', '--')
                self.ids.name_label.text = patient_data.get('name', '--')
                self.ids.jenis_kelamin_label.text = patient_data.get('jenis_kelamin', '--')
                self.ids.no_telp_label.text = patient_data.get('no_telp', '--')
                self.ids.alamat_label.text = patient_data.get('alamat', '--')
            else:
                print("Data pasien tidak ditemukan.")
        except Exception as e:
            print(f"Error memuat detail pasien: {e}")

    def kembali(self):
        self.manager.current = 'kelola_pasien'