from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from firebase_admin import auth,db
import os

current_user_uid = ""  # Untuk menyimpan UID pengguna yang sedang login

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'RiwayatPasien.kv')
Builder.load_file(kv_path)

class HistoryScreen(Screen):
    def on_enter(self):
        self.load_history_data()

    def load_history_data(self):
        # Ambil UID pengguna yang sedang login
        user_email = App.get_running_app().current_user_email
        user = auth.get_user_by_email(user_email)
        global current_user_uid
        current_user_uid = user.uid  # Menyimpan UID pengguna yang sedang login

        # Ambil data riwayat pasien dari Firebase Realtime Database
        riwayat_ref = db.reference(f'riwayat_pasien/{current_user_uid}')
        
        try:
            riwayat_data = riwayat_ref.get()

            if not riwayat_data:
                print("Tidak ada data riwayat.")
                return

            # Hapus widget lama sebelum menampilkan yang baru
            self.ids.history_grid.clear_widgets()

            for idx, (antrian_uid, data) in enumerate(riwayat_data.items(), start=1):
                self.add_history_row(idx, data)

        except Exception as e:
            print(f"Error memuat data riwayat: {e}")

    def add_history_row(self, index, data):
        # Tampilkan No
        no_label = Label(
            text=str(index),
            color=(0, 0, 0, 1),
            size_hint_x=0.25,
            halign='center',
            valign='middle',
            font_size='12sp'
        )
        self.ids.history_grid.add_widget(no_label)

        # Tampilkan Nama (Ambil dari data pasien)
        name_label = Label(
            text=data.get('nama_lengkap', '--'),
            color=(0, 0, 0, 1),
            size_hint_x=0.35,
            halign='left',
            valign='middle',
            padding_x=dp(10),
            font_size='12sp'
        )
        self.ids.history_grid.add_widget(name_label)

        # Tampilkan Tanggal Antrian
        date_label = Label(
            text=data.get('tanggal_antrian', '--'),
            color=(0, 0, 0, 1),
            size_hint_x=0.3,
            halign='center',
            valign='middle',
            font_size='12sp'
        )
        self.ids.history_grid.add_widget(date_label)

        # Tampilkan Poli
        poli_label = Label(
            text=data.get('poli', '--'),
            color=(0, 0, 0, 1),
            size_hint_x=0.3,
            halign='center',
            valign='middle',
            font_size='12sp'
        )
        self.ids.history_grid.add_widget(poli_label)