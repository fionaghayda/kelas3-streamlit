import streamlit as st
from utils import check_teacher_password, check_guest_password
from pages.nilai import show_nilai_page
from pages.galeri import show_galeri_page
from pages.komentar import show_komentar_page

st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", layout="wide")

st.title("📘 Dokumentasi Akademik Kelas 3")
st.write("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.write("🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd")

menu = st.sidebar.selectbox("📂 Pilih Halaman", [
    "Beranda",
    "Nilai & Data",
    "Galeri",
    "Komentar"
])

if menu == "Beranda":
    st.header("Selamat Datang! 👋")
    st.markdown("""
    Aplikasi ini digunakan untuk mendokumentasikan kegiatan akademik kelas 3 SDN Wonoplintahan 1.

    📌 Silakan pilih menu di samping untuk mengakses informasi.

    - **Nilai & Data**: hanya dapat diakses oleh Bu Rini.
    - **Galeri & Komentar**: dapat diakses oleh orang tua dan guru.
    """)

elif menu == "Nilai & Data":
    if check_teacher_password():
        show_nilai_page()

elif menu == "Galeri":
    if check_guest_password():
        show_galeri_page()

elif menu == "Komentar":
    if check_guest_password():
        show_komentar_page()
