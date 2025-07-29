import streamlit as st
from utils import login_user, is_logged_in, get_user_role
from pages.nilai import show_nilai_page
from pages.galeri import show_galeri_page
from pages.komentar import show_komentar_page

st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", layout="wide")
login_user()

if is_logged_in():
    role = get_user_role()

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

        📌 Silakan pilih menu di samping untuk mengakses informasi sesuai login Anda.
        """)

    elif menu == "Nilai & Data":
        if role == "guru":
            show_nilai_page()
        else:
            st.warning("Halaman ini hanya bisa diakses oleh guru.")

    elif menu == "Galeri":
        if role in ["guru", "orangtua"]:
            show_galeri_page()

    elif menu == "Komentar":
        if role in ["guru", "orangtua"]:
            show_komentar_page()
else:
    st.warning("Silakan login terlebih dahulu melalui sidebar.")
