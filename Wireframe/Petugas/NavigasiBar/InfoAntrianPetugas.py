from kivy.app import App
from kivy.uix.screenmanager import  Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from kivy.uix.label import Label
from kivy.uix.button import Button
from firebase_admin import db

# Set the window size
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'InfoAntrianPetugas.kv')
Builder.load_file(kv_path)

class InformasiAntrianScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.antrian_data = []

    def ambil_data_antrian(self):
        ref = db.reference("riwayat_pasien")
        data = ref.get()  # Ambil semua data riwayat pasien
        
        if data:
            for uid_pasien, antrian_data in data.items():
                for uid_antrian, detail_antrian in antrian_data.items():
                    nama = detail_antrian.get("nama_lengkap", "--")
                    tanggal_antrian = detail_antrian.get("tanggal_antrian", "--")
                    self.antrian_data.append((nama, tanggal_antrian))
        
        # Memperbarui tabel di layar
        self.tampilkan_data_antrian()

    def tampilkan_data_antrian(self):
        grid_layout = self.ids.tabel_antrian  # Pastikan ID ini diatur pada GridLayout di KV file
        grid_layout.clear_widgets()

        for i, (nama, tanggal_antrian) in enumerate(self.antrian_data, start=1):
            grid_layout.add_widget(Label(text=str(i), color=(0, 0, 0, 1), size_hint_x=0.1, font_size='12sp'))
            grid_layout.add_widget(Label(text=nama, color=(0, 0, 0, 1), size_hint_x=0.3, font_size='12sp'))
            grid_layout.add_widget(Label(text=tanggal_antrian, color=(0, 0, 0, 1), size_hint_x=0.2, font_size='12sp'))
            grid_layout.add_widget(Label(text="Menunggu", color=(0, 0, 0, 1), size_hint_x=0.2, font_size='12sp'))
            grid_layout.add_widget(Button(text="Detail", size_hint_x=0.2, font_size='12sp',
                                        on_press=lambda x, uid_antrian=i: self.detail_antrian(uid_antrian)))


    def detail_antrian(self, uid_antrian):
        self.manager.current = "detail_antrian"

    def on_enter(self):
        self.ambil_data_antrian()