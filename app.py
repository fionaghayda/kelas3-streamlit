import streamlit as st
from utils import check_password
import pandas as pd
import os

# Konfigurasi halaman
st.set_page_config(page_title="Kelas 3 SDN Wonoplintahan 1", layout="wide")

# Gaya tampilan CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');

        html, body, [class*="css"] {
            font-family: 'Nunito', sans-serif;
        }

        .main {
            background-color: #f9fafb;
        }

        h1, h2, h3 {
            color: #005288;
            margin-bottom: 0.4rem;
            margin-top: 0.5rem;
        }

        .stSidebar {
            background-color: #f0f2f6;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        hr.top-line {
            border: none;
            height: 4px;
            background-color: #005288;
            margin-bottom: 0.4rem;
        }

        hr.custom-line {
            border: none;
            height: 2px;
            background-color: #005288;
            margin-top: 0.1rem;
            margin-bottom: 0.1rem;
        }

        .card {
            background-color: white;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.06);
        }

        .info-box {
            background-color: #e6f2ff;
            border-left: 6px solid #005288;
            padding: 1rem;
            margin-bottom: 1.5rem;
            border-radius: 8px;
        }

        .footer {
            margin-top: 3rem;
            padding-top: 1rem;
            font-size: 0.8rem;
            text-align: center;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# Header Halaman
st.markdown('<hr class="top-line">', unsafe_allow_html=True)
st.title("📘 Dokumentasi Akademik Kelas 3")
st.subheader("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.caption("🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd")
st.markdown('<hr class="custom-line">', unsafe_allow_html=True)

# Navigasi Sidebar
menu = st.sidebar.selectbox("📂 Pilih Halaman", [
    "Beranda", 
    "Informasi Umum", 
    "Data Siswa (Privat)", 
    "Rekap Nilai (Privat)",
    "Galeri Foto",
    "Komentar Orang Tua"
])

# ================== HALAMAN BERANDA ==================
if menu == "Beranda":
    st.markdown("### 👋 Selamat Datang!")
    st.markdown('<div class="info-box">Selamat datang di situs dokumentasi kegiatan kelas 3 SDN Wonoplintahan 1. Website ini ditujukan untuk orang tua dan wali murid agar dapat mengikuti perkembangan pembelajaran siswa.</div>', unsafe_allow_html=True)

    st.markdown("### 📆 Jadwal Pelajaran Mingguan")
    try:
        df_jadwal = pd.read_csv("data/jadwal_pelajaran.csv")
        st.dataframe(df_jadwal, use_container_width=True)
    except FileNotFoundError:
        st.warning("File `jadwal_pelajaran.csv` belum ditemukan di folder `data/`.")

# ================== HALAMAN INFORMASI UMUM ==================
elif menu == "Informasi Umum":
    st.markdown("### 📘 Informasi Umum")
    st.markdown("---")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("- 🗓️ Hari belajar: Senin - Jumat")
    st.write("- 👧👦 Jumlah siswa: 30 siswa")
    st.write("- 🎓 Tema: Kurikulum Merdeka")
    st.write("- 📌 Kegiatan rutin: Upacara, Literasi Pagi, Jumat Bersih")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== HALAMAN DATA SISWA ==================
elif menu == "Data Siswa (Privat)":
    if check_password():
        st.markdown("### 📋 Data Siswa (Privat)")
        st.markdown("---")
        try:
            df = pd.read_csv("data/siswa.csv")
            st.dataframe(df, use_container_width=True)
        except FileNotFoundError:
            st.error("❌ File data siswa belum tersedia di folder `data/`.")

# ================== HALAMAN NILAI SISWA ==================
elif menu == "Rekap Nilai (Privat)":
    if check_password():
        st.markdown("### 📊 Rekap Nilai Siswa")
        st.markdown("---")
        try:
            df_nilai = pd.read_csv("data/nilai.csv")
            st.dataframe(df_nilai, use_container_width=True)
        except FileNotFoundError:
            st.error("❌ File nilai.csv belum ditemukan di folder `data/`.")

# ================== HALAMAN GALERI FOTO ==================
elif menu == "Galeri Foto":
    st.markdown("### 🖼️ Galeri Foto")
    st.markdown("---")
    image_folder = "data/galeri"
    if os.path.isdir(image_folder):
        images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        if images:
            for i, img in enumerate(images):
                col1, col2 = st.columns(2)
                with col1:
                    st.image(f"{image_folder}/{img}", width=300)
                with col2:
                    st.markdown(f"**Foto {i+1}**")
        else:
            st.info("Belum ada gambar di folder `data/galeri/`.")
    else:
        st.info("Folder galeri belum dibuat.")

# ================== HALAMAN KOMENTAR ==================
elif menu == "Komentar Orang Tua":
    st.markdown("### 💬 Komentar & Usulan Orang Tua")
    st.markdown("---")
    st.markdown("Silakan berikan masukan atau komentar Anda:")
    nama = st.text_input("Nama Orang Tua")
    komentar = st.text_area("Komentar atau Usulan")
    if st.button("Kirim"):
        if nama and komentar:
            with open("data/komentar.csv", "a") as f:
                f.write(f"{nama},{komentar}\n")
            st.success("Terima kasih atas masukannya!")
        else:
            st.warning("Mohon lengkapi nama dan komentar.")

    st.markdown("---")
    st.markdown("#### Komentar Terkini")
    if os.path.exists("data/komentar.csv"):
        df_komen = pd.read_csv("data/komentar.csv", names=["Nama", "Komentar"])
        for _, row in df_komen.iterrows():
            st.markdown(f"**{row['Nama']}**: {row['Komentar']}")

# ================== FOOTER ==================
st.markdown("""
    <div class="footer">
        © 2025 - Dokumentasi Kelas 3 SDN Wonoplintahan 1 | Dibuat oleh Ibu Rini Kus Endang, S.Pd
    </div>
""", unsafe_allow_html=True)
