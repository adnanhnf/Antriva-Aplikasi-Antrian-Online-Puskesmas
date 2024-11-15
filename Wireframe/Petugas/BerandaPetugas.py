from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from Petugas.NavigasiBar.InfoAntrianPetugas import InformasiAntrianScreen
from Petugas.NavigasiBar.KelolaPasien import KelolaPasienScreen
from Petugas.DetaildanTambah.DetailAntrian import DetailAntrianScreen
from Petugas.DetaildanTambah.DetailPasien import DetailPasienScreen
from Petugas.DetaildanTambah.TambahPasien import TambahPasienScreen
from Petugas.DetaildanTambah.EditPasien import EditPasienScreen

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'BerandaPetugas.kv')
Builder.load_file(kv_path)

# Set window size   
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class BerandaPetugasScreen(Screen):
    pass

class BerandaPetugas(App):
    def build(self):     
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(BerandaPetugasScreen(name='beranda_petugas'))
        sm.add_widget(InformasiAntrianScreen(name='informasi_antrian'))
        sm.add_widget(DetailAntrianScreen(name='detail_antrian'))
        sm.add_widget(KelolaPasienScreen(name='kelola_pasien'))
        sm.add_widget(DetailPasienScreen(name='detail_pasien'))
        sm.add_widget(TambahPasienScreen(name='tambah_pasien'))
        sm.add_widget(EditPasienScreen(name='edit_pasien'))
        return sm

if __name__ == '__main__':
    BerandaPetugas().run()
