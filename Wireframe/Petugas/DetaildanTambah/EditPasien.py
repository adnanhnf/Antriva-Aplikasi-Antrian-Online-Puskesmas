from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import  Screen
from kivy.lang import Builder
import os
from firebase_admin import db

# Atur Ukuran Layar
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'EditPasien.kv')
Builder.load_file(kv_path)

class EditPasienScreen(Screen):
    def simpan(self):
        # Logika Untuk Menyimpan Data
        self.simpan_data()
        
        # Kembali ke Tampilan Kelola Pasien Setelah Simpan Perubahan Data
        App.get_running_app().root.current = 'kelola_pasien'

    def batal(self):
        # Tidak Menyimpan Perubahan Data, Langsung Kembali ke Tampilan Kelola Pasien
        App.get_running_app().root.current = 'kelola_pasien'
        
    def clear_form(self):
        # Kosongkan semua input
        self.ids.name_input.text = ""
        self.ids.nik_input.text = ""
        self.ids.jenis_kelamin_spinner.text = "Pilih"
        self.ids.no_telp_input.text = ""
        self.ids.alamat_input.text = ""
    
    def on_pre_enter(self):
        # Kosongkan formulir saat layar dimasuki
        self.clear_form()

    def simpan_data(self):
        # Ambil data dari input
        name = self.ids.name_input.text
        nik = self.ids.nik_input.text
        jenis_kelamin = self.ids.jenis_kelamin_spinner.text
        no_telp = self.ids.no_telp_input.text
        alamat = self.ids.alamat_input.text

        # Validasi data jika diperlukan
        if not name or not nik or jenis_kelamin == 'Pilih' or not no_telp or not alamat:
            print("Semua data wajib diisi!")
            return

        # Ambil UID pasien saat ini (diatur saat berpindah ke layar edit)
        uid = getattr(self, 'current_uid', None)
        if not uid:
            print("UID pasien tidak ditemukan!")
            return

        try:
            # Update data di Firebase Realtime Database
            pasien_ref = db.reference(f'users/{uid}')
            pasien_ref.update({
                'name': name,
                'nik': nik,
                'jenis_kelamin': jenis_kelamin,
                'no_telp': no_telp,
                'alamat': alamat,
            })
            print("Data pasien berhasil diperbarui!")

            # Kembali ke layar kelola pasien
            App.get_running_app().root.current = 'kelola_pasien'
        except Exception as e:
            print(f"Error memperbarui data pasien: {e}")
