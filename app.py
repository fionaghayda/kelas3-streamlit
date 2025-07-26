import streamlit as st
import pandas as pd
import os
from PIL import Image
from utils import check_password, simpan_komentar, simpan_foto

st.set_page_config(page_title="Dokumentasi Kelas 3", layout="centered")

# --- Header ---
st.markdown("""
<div style='text-align: center; border-top: 4px solid #004aad; padding-top: 10px;'>
    <h2>📘 Dokumentasi Akademik Kelas 3</h2>
    <h4>SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo</h4>
    <p>🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd</p>
</div>
<hr style='border:1px solid lightgray;'>
""", unsafe_allow_html=True)

# --- Navigasi ---
halaman = st.sidebar.radio("Pilih Halaman", ["Jadwal Pelajaran", "Nilai & Data", "Galeri Foto", "Komentar Orang Tua"])

# === 1. Jadwal Pelajaran ===
if halaman == "Jadwal Pelajaran":
    st.subheader("📅 Jadwal Pelajaran")
    try:
        df = pd.read_csv("data/jadwal_pelajaran.csv")
        st.dataframe(df)
    except:
        st.error("Jadwal belum tersedia.")

# === 2. Nilai & Data ===
elif halaman == "Nilai & Data":
    if check_password("nilai_data"):
        st.subheader("📊 Nilai dan Data Siswa")
        tab1, tab2 = st.tabs(["📄 Data Siswa", "📈 Nilai Harian"])
        with tab1:
            try:
                st.dataframe(pd.read_csv("data/data_siswa.csv"))
            except:
                st.warning("Data siswa belum tersedia.")
        with tab2:
            try:
                st.dataframe(pd.read_csv("data/nilai_siswa.csv"))
            except:
                st.warning("Data nilai belum tersedia.")

# === 3. Galeri Foto ===
elif halaman == "Galeri Foto":
    if check_password("galeri_komentar"):
        st.subheader("🖼️ Galeri Foto")
        uploaded_file = st.file_uploader("Unggah Foto", type=["png", "jpg", "jpeg"])
        caption = st.text_input("Caption Foto")
        if uploaded_file and caption:
            path = simpan_foto(uploaded_file, caption)
            st.success("Foto berhasil disimpan!")
        st.markdown("---")
        st.subheader("📸 Foto-Foto Tersimpan")
        folder = "data/galeri"
        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            for file in sorted(files, reverse=True):
                img_path = os.path.join(folder, file)
                caption_file = img_path + ".txt"
                caption_text = open(caption_file, "r", encoding="utf-8").read() if os.path.exists(caption_file) else ""
                st.image(img_path, width=300, caption=caption_text)

# === 4. Komentar Orang Tua ===
elif halaman == "Komentar Orang Tua":
    if check_password("galeri_komentar"):
        st.subheader("💬 Komentar dan Usulan Orang Tua")
        nama = st.text_input("Nama Orang Tua")
        komentar = st.text_area("Komentar atau Usulan")
        if st.button("Kirim Komentar"):
            if nama and komentar:
                simpan_komentar(nama, komentar)
                st.success("Komentar berhasil dikirim!")
            else:
                st.warning("Mohon lengkapi nama dan komentar.")
        st.markdown("---")
        st.subheader("🗒️ Komentar Terkirim:")
        try:
            df_komen = pd.read_csv("data/komentar.csv")
            for i, row in df_komen.iterrows():
                st.write(f"🕒 {row['timestamp']} - ✍️ {row['nama']}: {row['komentar']}")
        except:
            st.warning("Belum ada komentar.")
