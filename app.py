import streamlit as st
import pandas as pd
import os
import datetime
from utils import check_password

# Konfigurasi halaman
st.set_page_config(page_title="Dokumentasi Akademik Kelas 3", layout="wide")

# Header utama
st.markdown("""
<div style='text-align: center;'>
    <h1 style='margin-bottom: 5px;'>📘 Dokumentasi Akademik Kelas 3</h1>
    <h4 style='margin-top: 0px;'>SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo</h4>
    <h5>🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd</h5>
    <hr style='border: 2px solid #000;'>
</div>
""", unsafe_allow_html=True)

# Menu navigasi
menu = st.sidebar.selectbox("Navigasi", [
    "Beranda",
    "Nilai Siswa",
    "Jadwal Pelajaran",
    "Data Siswa",
    "Komentar Orang Tua",
    "Galeri Foto"
])

# Halaman Beranda
if menu == "Beranda":
    st.image("https://i.ibb.co/jz7xzzN/classroom.jpg", use_column_width=True)
    st.write("""
        Selamat datang di platform dokumentasi akademik untuk kelas 3 SDN Wonoplintahan 1.
        Aplikasi ini dirancang untuk memudahkan guru dan orang tua dalam memantau perkembangan akademik siswa.
    """)

# Halaman Nilai
elif menu == "Nilai Siswa":
    if check_password("nilai"):
        st.subheader("📊 Data Nilai Siswa")
        try:
            df = pd.read_csv("pages/data/nilai.csv")
            st.dataframe(df, use_container_width=True)
        except:
            st.error("Gagal memuat data nilai.")

# Halaman Jadwal
elif menu == "Jadwal Pelajaran":
    st.subheader("📅 Jadwal Pelajaran Kelas 3")
    try:
        df = pd.read_csv("pages/data/jadwal_pelajaran.csv")
        st.dataframe(df, use_container_width=True)
    except:
        st.error("Data jadwal tidak ditemukan.")

# Halaman Data Siswa
elif menu == "Data Siswa":
    if check_password("data"):
        st.subheader("👨‍👩‍👧‍👦 Data Siswa")
        try:
            df = pd.read_csv("pages/data/data_siswa.csv")
            st.dataframe(df, use_container_width=True)
        except:
            st.error("Data siswa tidak ditemukan.")

# Halaman Komentar Orang Tua
elif menu == "Komentar Orang Tua":
    if check_password("komentar"):
        st.subheader("💬 Komentar dan Usulan Orang Tua")
        nama = st.text_input("Nama Orang Tua")
        komentar = st.text_area("Komentar atau Usulan")
        if st.button("Kirim Komentar"):
            if nama and komentar:
                waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                komentar_file = "pages/data/komentar.csv"
                if os.path.exists(komentar_file):
                    df = pd.read_csv(komentar_file)
                else:
                    df = pd.DataFrame(columns=["timestamp", "nama", "komentar"])
                df.loc[len(df.index)] = [waktu, nama, komentar]
                df.to_csv(komentar_file, index=False)
                st.success("Komentar berhasil dikirim!")
            else:
                st.warning("Isi semua kolom terlebih dahulu.")

        st.markdown("### 🗒️ Komentar Terkirim:")
        try:
            df = pd.read_csv("pages/data/komentar.csv")
            for _, row in df.iterrows():
                st.write(f"🕒 {row['timestamp']} - ✍️ {row['nama']}: {row['komentar']}")
        except:
            st.info("Belum ada komentar.")

# Halaman Galeri Foto
elif menu == "Galeri Foto":
    if check_password("galeri"):
        st.subheader("🖼️ Galeri Foto Kegiatan")

        galeri_folder = "pages/data/galeri"
        if not os.path.exists(galeri_folder):
            os.makedirs(galeri_folder)

        uploaded_file = st.file_uploader("Unggah Foto", type=["jpg", "jpeg", "png"])
        caption = st.text_input("Caption Foto")
        if st.button("Unggah"):
            if uploaded_file and caption:
                filepath = os.path.join(galeri_folder, uploaded_file.name)
                with open(filepath, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                with open(os.path.join(galeri_folder, "captions.txt"), "a") as f:
                    f.write(f"{uploaded_file.name}|{caption}\n")
                st.success("Foto berhasil diunggah.")
            else:
                st.warning("Lengkapi foto dan caption.")

        st.markdown("### 📸 Foto Tersimpan:")
        if os.path.exists(os.path.join(galeri_folder, "captions.txt")):
            with open(os.path.join(galeri_folder, "captions.txt")) as f:
                for line in f:
                    filename, cap = line.strip().split("|", 1)
                    path = os.path.join(galeri_folder, filename)
                    if os.path.exists(path):
                        st.image(path, caption=cap, use_column_width=True)
        else:
            st.info("Belum ada foto.")
