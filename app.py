import streamlit as st
from utils import check_password_kelas, check_password_galeri
import pandas as pd
import os
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(page_title="Kelas 3 SDN Wonoplintahan 1", layout="wide")

# Gaya CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');
        html, body, [class*="css"] {
            font-family: 'Nunito', sans-serif;
        }
        .main { background-color: #f9fafb; }
        h1, h2, h3 {
            color: #005288;
            margin-bottom: 0.4rem;
            margin-top: 0.5rem;
        }
        .stSidebar { background-color: #f0f2f6; }
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
st.title("📘 Dokumentasi Akademik Kelas 3")
st.subheader("SDN Wonoplintahan 1 - Kecamatan Prambon, Sidoarjo")
st.caption("🧑‍🏫 Oleh: Ibu RINI KUS ENDANG, S.Pd")
st.markdown('<hr class="custom-line">', unsafe_allow_html=True)

# Sidebar Navigasi
menu = st.sidebar.selectbox("📂 Pilih Halaman", [
    "Beranda",
    "Informasi Umum",
    "Data Siswa (Privat)",
    "Rekap Nilai (Privat)",
    "Galeri & Komentar (Privat)"
])

# ================== HALAMAN BERANDA ==================
if menu == "Beranda":
    st.markdown("### 👋 Selamat Datang!")
    st.write("""
        Website ini dibuat untuk mendokumentasikan kegiatan pembelajaran dan informasi penting 
        yang bisa diakses oleh orang tua murid dan wali kelas.
    """)

    st.markdown("---")
    st.markdown("### 📆 Jadwal Pelajaran Mingguan")

    try:
        df_jadwal = pd.read_csv("data/jadwal_pelajaran.csv")
        st.dataframe(df_jadwal, use_container_width=True)
    except FileNotFoundError:
        st.warning("File jadwal_pelajaran.csv belum ditemukan di folder `data/`.")

# ================== INFORMASI UMUM ==================
elif menu == "Informasi Umum":
    st.markdown("### 📘 Informasi Umum")
    st.markdown("---")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("- 🗓️ Hari belajar: Senin - Jumat")
    st.write("- 👧👦 Jumlah siswa: 30 siswa")
    st.write("- 🎓 Tema: Kurikulum Merdeka")
    st.write("- 📌 Kegiatan rutin: Upacara, Literasi Pagi, Jumat Bersih")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== DATA SISWA ==================
elif menu == "Data Siswa (Privat)":
    if check_password_kelas():
        st.markdown("### 📋 Data Siswa (Privat)")
        st.markdown("---")
        try:
            df = pd.read_csv("data/siswa.csv")
            st.dataframe(df, use_container_width=True)
        except FileNotFoundError:
            st.error("❌ File data siswa belum tersedia di folder `data/`.")

# ================== NILAI SISWA ==================
elif menu == "Rekap Nilai (Privat)":
    if check_password_kelas():
        st.markdown("### 📊 Rekap Nilai Siswa")
        st.markdown("---")
        try:
            df_nilai = pd.read_csv("data/nilai.csv")
            st.dataframe(df_nilai, use_container_width=True)
        except FileNotFoundError:
            st.error("❌ File nilai.csv belum ditemukan di folder `data/`.")

# ================== GALERI & KOMENTAR ==================
elif menu == "Galeri & Komentar (Privat)":
    if check_password_galeri():
        st.markdown("### 🖼️ Galeri Kelas & Komentar Orang Tua")
        st.markdown("---")

        galeri_path = "data/galeri"
        komentar_file = "data/komentar.csv"
        os.makedirs(galeri_path, exist_ok=True)

        # Form upload gambar
        with st.form("upload_form"):
            uploaded = st.file_uploader("📤 Unggah foto kegiatan (jpg/png)", type=["jpg", "png"])
            caption = st.text_input("📝 Keterangan foto (caption)")
            submitted = st.form_submit_button("Unggah")

            if submitted and uploaded:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{galeri_path}/{timestamp}_{uploaded.name}"
                with open(filename, "wb") as f:
                    f.write(uploaded.getbuffer())
                st.success("✅ Foto berhasil diunggah!")

                # Simpan caption
                with open(f"{filename}.txt", "w", encoding="utf-8") as cap:
                    cap.write(caption)

        # Tampilkan galeri
        st.markdown("#### 📸 Galeri Foto")
        for file in sorted(os.listdir(galeri_path)):
            if file.endswith((".jpg", ".png")):
                img_path = os.path.join(galeri_path, file)
                cap_file = img_path + ".txt"
                caption = ""
                if os.path.exists(cap_file):
                    with open(cap_file, encoding="utf-8") as cf:
                        caption = cf.read()
                st.image(img_path, caption=caption, use_column_width=True)

        st.markdown("---")

        # Komentar orang tua
        st.markdown("#### 💬 Komentar & Usulan Orang Tua")
        with st.form("form_komentar"):
            nama = st.text_input("Nama Orang Tua")
            isi = st.text_area("Komentar atau Usulan")
            kirim = st.form_submit_button("Kirim")

            if kirim and nama and isi:
                waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(komentar_file, "a", encoding="utf-8") as f:
                    f.write(f"{waktu},{nama},{isi.replace(',', ';')}\n")
                st.success("✅ Komentar berhasil dikirim!")

        # Tampilkan komentar
        if os.path.exists(komentar_file):
            df_komen = pd.read_csv(komentar_file, names=["Waktu", "Nama", "Komentar"])
            st.dataframe(df_komen, use_container_width=True)

# ================== FOOTER ==================
st.markdown("""
    <div class="footer">
        © 2025 - Dokumentasi Kelas 3 SDN Wonoplintahan 1 | Dibuat oleh Ibu Rini Kus Endang, S.Pd
    </div>
""", unsafe_allow_html=True)
