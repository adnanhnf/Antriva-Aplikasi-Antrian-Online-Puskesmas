from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from firebase_admin import db, auth
from kivy.metrics import dp

Window.size = (800, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

current_dir = os.path.dirname(os.path.abspath(__file__))
kv_path = os.path.join(current_dir, 'KelolaPasien.kv')
Builder.load_file(kv_path)

class KelolaPasienScreen(Screen):
    def on_enter(self):
        self.load_patient_data()

    def load_patient_data(self):
        self.ids.patient_grid.clear_widgets()
        patients_ref = db.reference('users')
        try:
            patients = patients_ref.order_by_child('role').equal_to('Pasien').get()
            
            if not patients:
                print("Tidak ada data pasien.")
                return

            for idx, (uid, patient) in enumerate(patients.items(), start=1):
                self.add_patient_row(idx, uid, patient)
        except Exception as e:
            print(f"Error memuat data pasien: {e}")

    def add_patient_row(self, index, uid, patient):
        # No column
        no_label = Label(
            text=str(index),
            color=(0, 0, 0, 1),
            size_hint_x=0.25,
            halign='center',
            valign='middle',
            font_size='12sp'  # Smaller font
        )
        no_label.bind(size=no_label.setter('text_size'))
        self.ids.patient_grid.add_widget(no_label)

        # Name column
        name_label = Label(
            text=patient.get('name', '--'),
            color=(0, 0, 0, 1),
            size_hint_x=0.3,
            halign='left',
            valign='middle',
            padding_x=dp(25),
            font_size='12sp',  # Smaller font
            shorten=True,
            shorten_from='right'
        )
        name_label.bind(size=name_label.setter('text_size'))
        self.ids.patient_grid.add_widget(name_label)

        # Email column
        email_label = Label(
            text=patient.get('email', '--'),
            color=(0, 0, 0, 1),
            size_hint_x=0.5,
            halign='left',
            valign='middle',
            padding_x=dp(10),
            font_size='12sp',  # Smaller font
            shorten=True,
            shorten_from='right'
        )
        email_label.bind(size=email_label.setter('text_size'))
        self.ids.patient_grid.add_widget(email_label)

        # Action buttons column - Vertical layout
        action_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=0.2,  # Disesuaikan
            spacing=dp(5),
            padding=(dp(5), dp(5))
        )

        # Edit button
        edit_button = Button(
            text='Edit',
            size_hint_y=0.45,  # Takes 45% of the vertical space
            background_color=(0.2, 0.6, 1, 1),
            font_size='12sp'
        )
        edit_button.bind(on_press=lambda instance: self.edit_patient(uid))
        
        # Delete button
        delete_button = Button(
            text='Hapus',
            size_hint_y=0.45,  # Takes 45% of the vertical space
            background_color=(1, 0.2, 0.2, 1),
            font_size='12sp'
        )
        delete_button.bind(on_press=lambda instance: self.delete_patient(uid))
        
        action_layout.add_widget(edit_button)
        action_layout.add_widget(delete_button)
        self.ids.patient_grid.add_widget(action_layout)

        # Detail button - Disesuaikan
        detail_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=0.2,  # Disesuaikan agar sama dengan action_layout
            spacing=dp(5),
            padding=(dp(5), dp(5))
        )
        
        detail_button = Button(
            text='Detail',
            size_hint_y=1.0,  # Mengisi seluruh ruang vertikal
            background_color=(0.3, 0.3, 0.3, 1),
            font_size='12sp'  # Sama dengan tombol lain
        )
        detail_button.bind(on_press=lambda instance: self.view_patient_details(uid))
        detail_layout.add_widget(detail_button)
        self.ids.patient_grid.add_widget(detail_layout)

    def edit_patient(self, uid):
        edit_screen = self.manager.get_screen('edit_pasien')
        setattr(edit_screen, 'current_uid', uid)
        self.manager.current = 'edit_pasien'

    def delete_patient(self, uid):
        try:
            auth.delete_user(uid)
            db.reference(f'users/{uid}').delete()
            print("Pasien berhasil dihapus!")
            self.load_patient_data()
        except Exception as e:
            print(f"Error menghapus data pasien: {e}")

    def view_patient_details(self, uid):
        detail_screen = self.manager.get_screen('detail_pasien')
        setattr(detail_screen, 'current_uid', uid)
        self.manager.current = 'detail_pasien'