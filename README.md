<p align="center"><img src="https://imgur.com/CDyCXhR.png" width="300"></p>

# 🏥 Antriva - Aplikasi Antrian Online Puskesmas

> **Antriva** adalah aplikasi antrian online yang dirancang untuk mempermudah proses pendaftaran dan pengelolaan antrian di Puskesmas. Aplikasi ini dikembangkan menggunakan Python dan Kivy, dengan desain visual berbentuk wireframe, serta didukung oleh Firebase sebagai database utama. Antriva bertujuan memberikan pengalaman antrian yang lebih praktis dan efisien bagi pasien maupun petugas Puskesmas. Pengguna dapat mengambil nomor antrian secara online, melihat estimasi waktu, dan petugas dapat mengelola antrian secara langsung melalui aplikasi. Desain wireframe memudahkan pengembangan antarmuka pengguna yang sederhana dan intuitif.

---

## 🛠 Teknologi yang Digunakan

- Python + Kivy untuk antarmuka pengguna  
- Firebase Realtime Database untuk penyimpanan data antrian  
- Firebase Authentication untuk login pengguna dan petugas  

---

## 📌 Cara Menggunakan Aplikasi

1. Clone repositori ini ke komputer kamu.  
2. Buat project baru di **Firebase Console**.  
3. Aktifkan **Firebase Realtime Database** dan **Authentication (Email/Password)**.  
4. Buat **file kredensial (service account)** dari Firebase dan simpan di folder `firebase/`.  
5. Edit file `config.py` untuk mengatur koneksi ke Firebase, termasuk path file kredensial dan nama database.  
6. Install semua dependensi menggunakan perintah `pip install -r requirements.txt`.  
7. Jalankan aplikasi dengan menjalankan file `main.py`.  
8. **Tambahkan akun pasien dan petugas** melalui Firebase Authentication (manual via Firebase Console):  
   - Pastikan setiap user memiliki field **`role`** di Firebase Realtime Database:  
     - `role: pasien` untuk akun pasien  
     - `role: petugas` untuk akun petugas  
   - Aplikasi akan membaca role ini dan mengarahkan pengguna ke tampilan yang sesuai.  
9. Setelah login, pasien bisa mengambil nomor antrian, sedangkan petugas bisa memantau dan memanggil nomor antrian.

---

## 📂 Struktur Folder Proyek

- `main.py` – File utama aplikasi  
- `config.py` – Pengaturan Firebase dan path file kredensial  
- `screens/` – Folder berisi tampilan layar (login, antrian, dashboard petugas, dll)  
- `firebase/` – Folder tempat file JSON kredensial Firebase  
- `assets/` – Folder ikon, gambar, atau file pendukung  
- `requirements.txt` – Daftar dependensi Python  

---

## 📲 Contoh Tampilan Antarmuka

<p align="center"><img src="https://imgur.com/YBp4Hf1.png" width="300"></p>
<p align="center" style="font-size:12px; color:gray;">
Gambar 1. Tampilan Antarmuka Beranda Petugas
</p>

---

<p align="center"><img src="https://imgur.com/MrlKjFf.png" width="300"></p>
<p align="center" style="font-size:12px; color:gray;">
Gambar 2. Tampilan Antarmuka Beranda Pasien
</p>

---

## ⚙️ Fitur Utama

- Antrian online untuk pasien  
- Login dan otentikasi menggunakan Firebase  
- Sistem role (pasien & petugas) untuk membedakan tampilan  
- Pemanggilan dan penyelesaian antrian oleh petugas  
- Estimasi waktu tunggu bagi pasien  
- Desain wireframe yang sederhana dan mudah dikembangkan  
