from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, DictProperty, BooleanProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os
from datetime import datetime
from firebase_admin import auth, db
from Pasien.NavigasiBar.InfoAntrian import InfoQueueScreen
from Pasien.NavigasiBar.RiwayatPasien import HistoryScreen
from Pasien.NavigasiBar.ProfilPasien import ProfilScreen
from Pasien.NavigasiBar.NotifikasiPasien import NotificationScreen

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'BerandaPasien.kv')
Builder.load_file(kv_path)

# Set window size
Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class PoliBox(BoxLayout): # Logika Tampilan Beranda Pasien !!
    poli_id = StringProperty('')
    poli_name = StringProperty('')  # Properti untuk nama poli
    status_text = StringProperty('Tersedia')  # Default status
    is_available = BooleanProperty(True)

    def on_poli_id(self, instance, value):
        app = App.get_running_app()
        if app and app.root:
            poli_data = app.root.poli_status.get(value, {})
            self.poli_name = poli_data.get('name', '')  # Ambil nama poli
            self.update_status(poli_data.get('available', False))  # Perbarui status

    def update_status(self, status):
        self.is_available = status
        # Mengupdate status menjadi teks
        self.status_text = 'Tersedia' if status else 'Tidak\nTersedia'

class HomeScreen(Screen):
    poli_status = DictProperty({
        'A': {'name': 'Poli Umum', 'available': True},
        'B': {'name': 'Poli Gigi', 'available': True},
        'C': {'name': 'Poli Anak', 'available': True},
        'D': {'name': 'Poli KIA', 'available': False}
    })

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_number = 0
        # Memanggil on_poli_status pada inisialisasi
        self.on_poli_status(self, self.poli_status)

    def on_poli_status(self, instance, value):
        # Update semua PoliBox widget ketika poli_status berubah
        for poli_id in value:
            if hasattr(self.ids, f'poli_{poli_id.lower()}'):
                poli_box = getattr(self.ids, f'poli_{poli_id.lower()}')
                poli_box.poli_id = poli_id  # Menetapkan poli_id untuk setiap PoliBox
                poli_box.update_status(value[poli_id]['available'])
                poli_box.poli_name = value[poli_id]['name']  # Mengatur nama poli

class TakeTheQueueScreen(Screen):
    def go_back(self):
        self.manager.current = 'home'

    def cancel(self):
        self.manager.current = 'home'

    def get_current_queue_number(self, poli):
        # Ambil tanggal hari ini untuk key
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Reference ke antrian hari ini
        queue_ref = db.reference(f'antrian_harian/{today}/{poli}')
        current_data = queue_ref.get()
        
        if current_data is None:
            # Jika belum ada antrian hari ini, mulai dari 1
            return 1
        else:
            # Ambil nomor terakhir dan tambah 1
            return current_data.get('last_number', 0) + 1

    def update_current_queue_number(self, poli, nomor_antrian):
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            poli_ref = db.reference(f'antrian_harian/{today}/{poli}')
            
            # Ambil data poli
            poli_data = poli_ref.get() or {}
            current_number = poli_data.get('current_number', 0)
            
            # Tambah nomor antrian saat ini
            new_number = current_number + 1
            
            # Update di database
            poli_ref.update({
                'current_number': new_number
            })
            
            # Update status antrian yang sudah selesai
            antrian_ref = db.reference('antrian_aktif')
            antrian_snapshot = antrian_ref.get() or {}
            
            for uid, antrian in antrian_snapshot.items():
                if (antrian['poli'] == poli and 
                    antrian['tanggal_antrian'] == today and 
                    antrian['nomor_antrian'] == current_number):
                    
                    # Update status di antrian_aktif
                    antrian_ref.child(uid).update({
                        'status': 'selesai'
                    })
                    
                    # Update status di riwayat_pasien
                    riwayat_ref = db.reference(f'riwayat_pasien/{uid}')
                    riwayat_snapshot = riwayat_ref.get() or {}
                    
                    for rid, riwayat in riwayat_snapshot.items():
                        if (riwayat['nomor_antrian'] == current_number and 
                            riwayat['tanggal_antrian'] == today):
                            riwayat_ref.child(rid).update({
                                'status': 'selesai'
                            })
                        
            return True
            
        except Exception as e:
            print(f"Error updating current queue number: {e}")
            return False

    def ambil_antrian(self):
        try:
            # Ambil data input
            nama_lengkap = self.ids.nama_lengkap.text
            keluhan = self.ids.keluhan.text
            poli = self.ids.poli.text
            
            # Validasi input
            if not all([nama_lengkap, keluhan, poli != 'Pilih']):
                print("Semua field harus diisi!")
                return

            # Get current user
            app = App.get_running_app()
            user_email = app.current_user_email
            if not user_email:
                raise ValueError("Email pengguna tidak ditemukan! Harap login ulang.")
            
            user = auth.get_user_by_email(user_email)
            uid = user.uid

            # Generate timestamp
            timestamp = datetime.now()
            tanggal_antrian = timestamp.strftime('%Y-%m-%d')
            waktu_antrian = timestamp.strftime('%H:%M:%S')

            # Dapatkan nomor antrian
            nomor_antrian = self.get_current_queue_number(poli)
            
            # Update nomor antrian di database
            self.update_current_queue_number(poli, nomor_antrian)

            # Simpan data antrian
            antrian_ref = db.reference('antrian_aktif').child(uid)
            antrian_ref.set({
                'nama_lengkap': nama_lengkap,
                'keluhan': keluhan,
                'poli': poli,
                'nomor_antrian': nomor_antrian,
                'tanggal_antrian': tanggal_antrian,
                'waktu_antrian': waktu_antrian,
                'timestamp': str(timestamp),
                'status': 'menunggu'
            })

            # Simpan ke riwayat
            riwayat_ref = db.reference('riwayat_pasien').child(uid).push()
            riwayat_ref.set({
                'nama_lengkap': nama_lengkap,
                'keluhan': keluhan,
                'poli': poli,
                'nomor_antrian': nomor_antrian,
                'tanggal_antrian': tanggal_antrian,
                'waktu_antrian': waktu_antrian,
                'timestamp': str(timestamp),
                'status': 'menunggu',
                'uid': uid,
                'role': 'Pasien'
            })

            print("Antrian berhasil dibuat!")
            self.manager.current = 'information'

        except Exception as e:
            print(f"Terjadi kesalahan saat membuat antrian: {e}")
            
class BerandaPasien(App):
    current_user_email = StringProperty(None) 
    
    def build(self):     
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TakeTheQueueScreen(name='takethequeue'))
        sm.add_widget(InfoQueueScreen(name= 'information'))
        sm.add_widget(HistoryScreen(name= 'history'))
        sm.add_widget(ProfilScreen(name= 'profil'))
        sm.add_widget(NotificationScreen(name= 'notification'))
        return sm

if __name__ == '__main__':
        BerandaPasien().run()