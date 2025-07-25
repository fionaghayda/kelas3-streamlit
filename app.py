import streamlit as st
from utils import check_password
import pandas as pd

st.set_page_config(page_title="Kelas 3 SDN Wonoplintahan 1", layout="wide")

st.title("📘 Dokumentasi Akademik Kelas 3")
st.subheader("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.caption("Oleh: Ibu RINI KUS ENDANG, S.Pd")

menu = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Informasi Umum", "Data Siswa (Privat)"])

if menu == "Beranda":
    st.header("Selamat datang di dokumentasi akademik kelas 3!")
    st.write("""
        Website ini dibuat untuk mendokumentasikan kegiatan pembelajaran dan informasi penting 
        yang bisa diakses oleh orang tua murid dan wali kelas.
    """)

elif menu == "Informasi Umum":
    st.header("📚 Informasi Umum")
    st.write("- Hari belajar: Senin - Jumat")
    st.write("- Jumlah siswa: 30 siswa")
    st.write("- Tema Kurikulum Merdeka")
    st.write("- Kegiatan rutin: Upacara, Literasi Pagi, Jumat Bersih")

elif menu == "Data Siswa (Privat)":
    if check_password():
        st.header("📋 Data Siswa (Privat)")
        try:
            df = pd.read_csv("data/siswa.csv")
            st.dataframe(df)
        except FileNotFoundError:
            st.error("File data siswa belum tersedia.")
