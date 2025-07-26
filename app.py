# File: app.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils import check_password

st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", layout="centered")
st.markdown("""
    <h1 style='text-align: center;'>📘 Dokumentasi Akademik Kelas 3</h1>
    <h4 style='text-align: center;'>SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo</h4>
    <h5 style='text-align: center;'>🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd</h5>
    <hr style='border: 2px solid #4a4a4a;'>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Navigasi", ["Beranda", "Nilai Siswa", "Jadwal Pelajaran", "Komentar Orang Tua", "Galeri Foto"])

if menu == "Beranda":
    st.subheader("Selamat datang di Dokumentasi Akademik Kelas 3!")
    st.markdown("Silakan gunakan menu di sebelah kiri untuk menjelajahi data akademik, komentar orang tua, dan galeri kegiatan siswa.")

elif menu == "Nilai Siswa":
    if check_password("nilai"):
        df = pd.read_csv("pages/data/nilai.csv")
        st.subheader("📊 Data Nilai Siswa")
        st.dataframe(df, use_container_width=True)

elif menu == "Jadwal Pelajaran":
    df_jadwal = pd.read_csv("pages/data/jadwal_pelajaran.csv")
    st.subheader("📅 Jadwal Pelajaran Kelas 3")
    for hari in df_jadwal['Hari'].unique():
        st.markdown(f"### 📘 {hari}")
        st.dataframe(df_jadwal[df_jadwal['Hari'] == hari].drop(columns=['Hari']), use_container_width=True)

elif menu == "Komentar Orang Tua":
    if check_password("komentar"):
        komentar_path = "pages/data/komentar_ortu.csv"
        st.subheader("💬 Komentar dan Usulan Orang Tua")
        with st.form("form_komentar"):
            nama = st.text_input("Nama Orang Tua")
            komentar = st.text_area("Komentar atau Usulan")
            submit = st.form_submit_button("Kirim")
            if submit and nama.strip() and komentar.strip():
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_entry = pd.DataFrame([[timestamp, nama, komentar]], columns=["timestamp", "nama", "komentar"])
                if os.path.exists(komentar_path):
                    existing = pd.read_csv(komentar_path)
                    updated = pd.concat([existing, new_entry], ignore_index=True)
                else:
                    updated = new_entry
                updated.to_csv(komentar_path, index=False)
                st.success("Komentar berhasil dikirim!")

        if os.path.exists(komentar_path):
            df_komentar = pd.read_csv(komentar_path)
            st.markdown("### 🗒️ Komentar Terkirim:")
            for _, row in df_komentar.iterrows():
                st.write(f"🕒 {row['timestamp']} - ✍️ {row['nama']}: {row['komentar']}")

elif menu == "Galeri Foto":
    if check_password("galeri"):
        galeri_dir = "pages/data/galeri"
        if not os.path.exists(galeri_dir):
            os.makedirs(galeri_dir)

        st.subheader("🖼️ Unggah Foto Galeri")
        with st.form("unggah_foto"):
            file = st.file_uploader("Pilih foto", type=["jpg", "png", "jpeg"])
            caption = st.text_input("Keterangan Foto")
            kirim = st.form_submit_button("Unggah")
            if kirim and file is not None:
                file_path = os.path.join(galeri_dir, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                meta_path = os.path.join(galeri_dir, "galeri.csv")
                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                entry = pd.DataFrame([[file.name, waktu, caption]], columns=["filename", "timestamp", "caption"])
                if os.path.exists(meta_path):
                    existing = pd.read_csv(meta_path)
                    updated = pd.concat([existing, entry], ignore_index=True)
                else:
                    updated = entry
                updated.to_csv(meta_path, index=False)
                st.success("Foto berhasil diunggah!")

        st.markdown("### 📷 Galeri Foto:")
        meta_path = os.path.join(galeri_dir, "galeri.csv")
        if os.path.exists(meta_path):
            df_foto = pd.read_csv(meta_path)
            for _, row in df_foto.iterrows():
                img_path = os.path.join(galeri_dir, row['filename'])
                if os.path.exists(img_path):
                    st.image(img_path, caption=f"{row['caption']} | 🕒 {row['timestamp']}", use_column_width=True)
