from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os
from firebase_admin import auth, db

# Atur Ukuran Layar
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'TambahPasien.kv')
Builder.load_file(kv_path)

class TambahPasienScreen(Screen):
    def simpan(self):
        # Logika Untuk Menyimpan Data
        self.simpan_data()
        
        # Kembali ke Tampilan Kelola Pasien Setelah Menyimpan Data
        App.get_running_app().root.current = 'kelola_pasien'

    def batal(self):
        # Tidak Menyimpan Data, Langsung Kembali ke Tampilan Kelola Pasien
        App.get_running_app().root.current = 'kelola_pasien'
    
    def clear_form(self):
        # Kosongkan semua input
        self.ids.name.text = ""
        self.ids.email.text = ""
        self.ids.password.text = ""
        self.ids.nik.text = ""
        self.ids.jenis_kelamin.text = "Pilih"
        self.ids.no_telp.text = ""
        self.ids.alamat.text = ""
    
    def on_pre_enter(self):
        # Kosongkan formulir saat layar dimasuki
        self.clear_form()

    def simpan_data(self):
        # Ambil data input dari pengguna
        name = self.ids.name.text
        email = self.ids.email.text
        password = self.ids.password.text
        nik = self.ids.nik.text
        jenis_kelamin = self.ids.jenis_kelamin.text
        no_telp = self.ids.no_telp.text
        alamat = self.ids.alamat.text

        # Pertama, buat pengguna di Firebase Authentication
        try:
            user = auth.create_user(
                email=email,
                password=password
            )
            print(f"Pengguna berhasil dibuat: {user.uid}")

            # Sekarang, simpan data pasien di Firebase Realtime Database
            patient_ref = db.reference('users').child(user.uid)  # Menggunakan user.uid dari Firebase Auth
            patient_ref.set({
                'name': name,
                'email': email,
                'nik': nik,
                'jenis_kelamin': jenis_kelamin,
                'no_telp': no_telp,
                'alamat': alamat,
                'uid': user.uid,  # Menghubungkan data pasien dengan UID pengguna
                'role': 'Pasien'  # Menambahkan role sebagai Pasien
            })

            print("Data pasien berhasil disimpan !!")

            # Setelah menyimpan data pasien, Anda bisa menambahkan role di Firebase Authentication
            # Update custom claim role pada pengguna di Firebase Authentication
            auth.set_custom_user_claims(user.uid, {'role': 'Pasien'})
            print(f"Role 'Pasien' berhasil ditambahkan ke pengguna: {user.uid}")
            
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
