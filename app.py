import streamlit as st
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Dokumentasi Kelas 3",
    layout="wide",
    page_icon="📘"
)

# Header utama
st.title("📘 Dokumentasi Akademik Kelas 3 SDN Wonoplintahan 1")
st.markdown("Selamat datang di aplikasi dokumentasi akademik kelas 3 yang dikelola oleh **Bu Rini Kus Endang, S.Pd.**")

# Sekat garis
st.markdown("---")

# 📂 Menampilkan Nilai Siswa
st.header("📝 Data Nilai Siswa")
try:
    df_nilai = pd.read_csv("pages/data/nilai.csv")
    st.dataframe(df_nilai, use_container_width=True)
except FileNotFoundError:
    st.error("File nilai.csv tidak ditemukan. Pastikan file ada di folder 'pages/data/'.")

# 📅 Menampilkan Jadwal Pelajaran
st.header("📅 Jadwal Pelajaran Kelas 3")

try:
    df_jadwal = pd.read_csv("pages/data/jadwal_pelajaran.csv")
    # Ganti nilai di kolom "Hari" dengan NaN jika sama dengan sebelumnya (biar tidak numpuk)
    df_jadwal["Hari"] = df_jadwal["Hari"].mask(df_jadwal["Hari"].duplicated(), "")
    st.dataframe(df_jadwal, use_container_width=True)
except FileNotFoundError:
    st.error("File jadwal_pelajaran.csv tidak ditemukan. Pastikan file ada di folder 'pages/data/'.")
