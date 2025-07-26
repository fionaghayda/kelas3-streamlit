import streamlit as st
from utils import check_password
import pandas as pd

st.set_page_config(page_title="Kelas 3 SDN Wonoplintahan 1", layout="wide")

# Gaya sederhana (disempurnakan untuk memperkecil jarak judul/subjudul)
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f8;
        }
        .stSidebar {
            background-color: #f0f2f6;
        }
        h1, h2, h3 {
            color: #005288;
            margin-bottom: 0.4rem;
            margin-top: 0.5rem;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .stCaption {
            margin-top: -0.5rem;
            font-size: 0.85rem;
            color: #444;
        }
    </style>
""", unsafe_allow_html=True)

# Judul Halaman
st.title("📘 Dokumentasi Akademik Kelas 3")
st.subheader("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.caption("Oleh: Ibu RINI KUS ENDANG, S.Pd")

# Menu navigasi
menu = st.sidebar.selectbox("Pilih Halaman", [
    "Beranda", 
    "Informasi Umum", 
    "Data Siswa (Privat)", 
    "Rekap Nilai (Privat)"
])

# Beranda (Dashboard + Jadwal)
if menu == "Beranda":
    st.header("Selamat datang di dokumentasi akademik kelas 3!")
    st.write("""
        Website ini dibuat untuk mendokumentasikan kegiatan pembelajaran dan informasi penting 
        yang bisa diakses oleh orang tua murid dan wali kelas.
    """)

    st.subheader("📆 Jadwal Pelajaran Mingguan")
    try:
        df_jadwal = pd.read_csv("data/jadwal_pelajaran.csv")

        # Kosongkan nilai Hari yang duplikat agar tidak menumpuk
        df_jadwal["Hari"] = df_jadwal["Hari"].mask(df_jadwal["Hari"].duplicated(), "")

        st.table(df_jadwal)
    except FileNotFoundError:
        st.error("File jadwal_pelajaran.csv belum ditemukan di folder 'data/'.")

# Informasi Umum
elif menu == "Informasi Umum":
    st.header("📚 Informasi Umum")
    st.write("- Hari belajar: Senin - Jumat")
    st.write("- Jumlah siswa: 30 siswa")
    st.write("- Tema: Kurikulum Merdeka")
    st.write("- Kegiatan rutin: Upacara, Literasi Pagi, Jumat Bersih")

# Data Siswa (Privat)
elif menu == "Data Siswa (Privat)":
    if check_password():
        st.header("📋 Data Siswa (Privat)")
        try:
            df = pd.read_csv("data/siswa.csv")
            st.dataframe(df)
        except FileNotFoundError:
            st.error("File data siswa belum tersedia.")

# Rekap Nilai (Privat)
elif menu == "Rekap Nilai (Privat)":
    if check_password():
        st.header("📊 Rekap Nilai Siswa")
        try:
            df_nilai = pd.read_csv("data/nilai.csv")
            st.dataframe(df_nilai)
        except FileNotFoundError:
            st.error("File nilai.csv belum ditemukan.")
