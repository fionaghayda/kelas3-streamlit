import streamlit as st
from utils import check_password

st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", page_icon="📘")

st.markdown("## 📘 Dokumentasi Akademik Kelas 3")
st.markdown("**SDN Wonoplintahan 1 – Kecamatan Prambon, Sidoarjo**")
st.markdown("👩‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd")

if not check_password("kelas3ku"):
    st.stop()

st.success("Silakan gunakan menu di sebelah kiri untuk mengakses halaman Nilai, Galeri, atau Komentar.")
