import streamlit as st
from utils import check_password, check_gallery_password, check_comment_password
import pandas as pd
from datetime import datetime
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

        .stCaption {
            margin-top: -0.5rem;
            font-size: 0.85rem;
            color: #444;
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
st.title("\U0001F4D8 Dokumentasi Akademik Kelas 3")
st.subheader("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.caption("\U0001F9D1‍\U0001F3EB Oleh: Ibu RINI KUS ENDANG, S.Pd")
st.markdown('<hr class="custom-line">', unsafe_allow_html=True)

# Navigasi Sidebar
menu = st.sidebar.selectbox("\U0001F4C2 Pilih Halaman", [
    "Beranda", 
    "Informasi Umum", 
    "Galeri Foto", 
    "Komentar Orang Tua",
    "Data Siswa (Privat)", 
    "Rekap Nilai (Privat)"
])

# ================== HALAMAN BERANDA ==================
if menu == "Beranda":
    st.markdown("### \U0001F44B Selamat Datang!")
    st.write("""
        Website ini dibuat untuk mendokumentasikan kegiatan pembelajaran dan informasi penting 
        yang bisa diakses oleh orang tua murid dan wali kelas.
    """)

    st.markdown("---")
    st.markdown("### \U0001F4C6 Jadwal Pelajaran Mingguan")

    try:
        df_jadwal = pd.read_csv("data/jadwal_pelajaran.csv")
        st.dataframe(df_jadwal, use_container_width=True)
    except FileNotFoundError:
        st.warning("File jadwal_pelajaran.csv belum ditemukan di folder data/.")

# ================== HALAMAN INFORMASI UMUM ==================
elif menu == "Informasi Umum":
    st.markdown("### \U0001F4D8 Informasi Umum")
    st.markdown("---")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("- \U0001F5D3️ Hari belajar: Senin - Jumat")
    st.write("- \U0001F467\U0001F466 Jumlah siswa: 30 siswa")
    st.write("- \U0001F393 Tema: Kurikulum Merdeka")
    st.write("- \U0001F4CC Kegiatan rutin: Upacara, Literasi Pagi, Jumat Bersih")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== HALAMAN GALERI FOTO ==================
elif menu == "Galeri Foto":
    if check_gallery_password():
        st.markdown("### \U0001F5BC️ Galeri Foto")
        st.markdown("---")

        folder = "data/galeri"
        os.makedirs(folder, exist_ok=True)

        uploaded_file = st.file_uploader("Unggah foto kegiatan:", type=["jpg", "jpeg", "png"])
        caption = st.text_input("Tambahkan caption untuk foto ini")

        if uploaded_file:
            filepath = os.path.join(folder, uploaded_file.name)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.getbuffer())
            with open("data/captions.csv", "a") as f:
                f.write(f"{uploaded_file.name},{caption}\n")
            st.success("\u2705 Foto berhasil diunggah!")

        if os.path.exists(folder):
            captions = {}
            if os.path.exists("data/captions.csv"):
                with open("data/captions.csv", "r") as f:
                    for line in f:
                        nama_file, teks = line.strip().split(",", 1)
                        captions[nama_file] = teks

            for file in os.listdir(folder):
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    st.image(os.path.join(folder, file), width=500)
                    st.caption(captions.get(file, ""))
                    st.markdown("---")

# ================== HALAMAN KOMENTAR ORANG TUA ==================
elif menu == "Komentar Orang Tua":
    if check_comment_password():
        st.markdown("### \U0001F4AC Komentar dan Usulan Orang Tua")
        st.markdown("---")

        komentar_file = "data/komentar.csv"
        nama = st.text_input("Nama Orang Tua")
        komentar = st.text_area("Komentar atau Usulan")

        if st.button("Kirim Komentar"):
            if nama and komentar:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                df_komen = pd.DataFrame([[nama, komentar, timestamp]], columns=["nama", "komentar", "timestamp"])
                if os.path.exists(komentar_file):
                    df_komen.to_csv(komentar_file, mode='a', header=False, index=False)
                else:
                    df_komen.to_csv(komentar_file, index=False)
                st.success("\u2705 Komentar berhasil dikirim!")
            else:
                st.warning("Harap isi nama dan komentar.")

        if os.path.exists(komentar_file):
            st.markdown("#### \U0001F5D2️ Komentar Terkirim:")
            df_all = pd.read_csv(komentar_file)
            for _, row in df_all.iterrows():
                st.write(f"\U0001F552 {row['timestamp']} - \u270D️ {row['nama']}: {row['komentar']}")

# ================== HALAMAN DATA SISWA ==================
elif menu == "Data Siswa (Privat)":
    if check_password():
        st.markdown("### \U0001F4CB Data Siswa (Privat)")
        st.markdown("---")
        try:
            df = pd.read_csv("data/siswa.csv")
            st.dataframe(df, use_container_width=True)
        except FileNotFoundError:
            st.error("\u274C File data siswa belum tersedia di folder data/.")

# ================== HALAMAN NILAI SISWA ==================
elif menu == "Rekap Nilai (Privat)":
    if check_password():
        st.markdown("### \U0001F4CA Rekap Nilai Siswa")
        st.markdown("---")
        try:
            df_nilai = pd.read_csv("data/nilai.csv")
            st.dataframe(df_nilai, use_container_width=True)
        except FileNotFoundError:
            st.error("\u274C File nilai.csv belum ditemukan di folder data/.")

# ================== FOOTER ==================
st.markdown("""
    <div class="footer">
        © 2025 - Dokumentasi Kelas 3 SDN Wonoplintahan 1 | Dibuat oleh Ibu Rini Kus Endang, S.Pd
    </div>
""", unsafe_allow_html=True)
