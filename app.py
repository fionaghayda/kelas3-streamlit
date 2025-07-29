import streamlit as st
from utils import login_user, logout_user, get_session
from pages.nilai import show_nilai_page
from pages.galeri import show_galeri_page
from pages.komentar import show_komentar_page

st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", layout="wide")

session = get_session()

st.title("📘 Dokumentasi Akademik Kelas 3")
st.write("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.write("🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd")

if not session.get("logged_in", False):
    login_user()
else:
    st.sidebar.write(f"👤 Login sebagai: {session['username']}")
    if st.sidebar.button("Logout"):
        logout_user()
        st.experimental_rerun()

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

        - **Nilai & Data**: hanya dapat diakses oleh Bu Rini.
        - **Galeri & Komentar**: dapat diakses oleh orang tua dan guru.
        """)

    elif menu == "Nilai & Data":
        if session['role'] == "guru":
            show_nilai_page()
        else:
            st.error("🔒 Hanya Bu Rini yang bisa mengakses halaman ini.")

    elif menu == "Galeri":
        show_galeri_page(session['role'])

    elif menu == "Komentar":
        show_komentar_page(session['username'])
